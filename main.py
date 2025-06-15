import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, round as spark_round
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = SparkSession.builder.appName("FirstTaskSandbox").getOrCreate()

# 1
users_df = spark.read.csv("./data/users.csv", header=True, inferSchema=True)
purchases_df = spark.read.csv("./data/purchases.csv", header=True, inferSchema=True)
products_df = spark.read.csv("./data/products.csv", header=True, inferSchema=True)

print("Users DataFrame:")
users_df.printSchema()
users_df.show(5)

print("Purchases DataFrame:")
purchases_df.printSchema()
purchases_df.show(5)

print("Products DataFrame:")
products_df.printSchema()
products_df.show(5)

# 2.

# Підрахунок початкової кількості рядків
print(f"Початкова кількість рядків:")
print(f"Users: {users_df.count()}")
print(f"Purchases: {purchases_df.count()}")
print(f"Products: {products_df.count()}")

# Видалення рядків з пропущеними значеннями
users_clean = users_df.dropna()
purchases_clean = purchases_df.dropna()
products_clean = products_df.dropna()

print(f"\nКількість рядків після очищення:")
print(f"Users: {users_clean.count()}")
print(f"Purchases: {purchases_clean.count()}")
print(f"Products: {products_clean.count()}")

# 3.
purchases_with_products = purchases_clean.join(products_clean, "product_id")

purchases_with_total = purchases_with_products.withColumn(
    "total_amount",
    col("quantity") * col("price")
)

total_by_category = purchases_with_total.groupBy("category") \
    .agg(spark_sum("total_amount").alias("total_sales")) \
    .orderBy(col("total_sales").desc())

print("3. Загальна сума покупок за категоріями:")
total_by_category.show()

# 4
purchases_with_users = purchases_with_total.join(users_clean, "user_id")

young_users_purchases = purchases_with_users.filter(
    (col("age") >= 18) & (col("age") <= 25)
)

young_by_category = young_users_purchases.groupBy("category") \
    .agg(spark_sum("total_amount").alias("young_sales")) \
    .orderBy(col("young_sales").desc())

print("4. Сума покупок за категоріями для віку 18-25:")
young_by_category.show()

# 5
total_young_sales = young_users_purchases.agg(spark_sum("total_amount").alias("total")).collect()[0]["total"]

print(f"5. Загальна сума покупок користувачів 18-25 років: {total_young_sales}")

young_percentage = young_by_category.withColumn(
    "percentage",
    spark_round((col("young_sales") / total_young_sales * 100), 2)
)

young_percentage.show()

# 6
top_3_categories = young_percentage.orderBy(col("percentage").desc()).limit(3)

print("6. Топ-3 категорії продуктів з найвищим відсотком витрат користувачів 18-25 років:")
top_3_categories.show()

top_3_list = [row.category for row in top_3_categories.collect()]
print(f"\nТоп-3 категорії: {top_3_list}")