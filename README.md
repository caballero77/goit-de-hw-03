```
Users DataFrame:
root
 |-- user_id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- age: integer (nullable = true)
 |-- email: string (nullable = true)

+-------+------+---+-----------------+
|user_id|  name|age|            email|
+-------+------+---+-----------------+
|      1|User_1| 45|user1@example.com|
|      2|User_2| 48|user2@example.com|
|      3|User_3| 36|user3@example.com|
|      4|User_4| 46|user4@example.com|
|      5|User_5| 29|user5@example.com|
+-------+------+---+-----------------+
only showing top 5 rows

Purchases DataFrame:
root
 |-- purchase_id: integer (nullable = true)
 |-- user_id: integer (nullable = true)
 |-- product_id: integer (nullable = true)
 |-- date: date (nullable = true)
 |-- quantity: integer (nullable = true)

+-----------+-------+----------+----------+--------+
|purchase_id|user_id|product_id|      date|quantity|
+-----------+-------+----------+----------+--------+
|          1|     52|         9|2022-01-01|       1|
|          2|     93|        37|2022-01-02|       8|
|          3|     15|        33|2022-01-03|       1|
|          4|     72|        42|2022-01-04|       9|
|          5|     61|        44|2022-01-05|       6|
+-----------+-------+----------+----------+--------+
only showing top 5 rows

Products DataFrame:
root
 |-- product_id: integer (nullable = true)
 |-- product_name: string (nullable = true)
 |-- category: string (nullable = true)
 |-- price: double (nullable = true)

+----------+------------+-----------+-----+
|product_id|product_name|   category|price|
+----------+------------+-----------+-----+
|         1|   Product_1|     Beauty|  8.3|
|         2|   Product_2|       Home|  8.3|
|         3|   Product_3|Electronics|  9.2|
|         4|   Product_4|Electronics|  2.6|
|         5|   Product_5|Electronics|  9.4|
+----------+------------+-----------+-----+
only showing top 5 rows

Початкова кількість рядків:
Users: 100
Purchases: 200
Products: 50

Кількість рядків після очищення:
Users: 95
Purchases: 195
Products: 47
3. Загальна сума покупок за категоріями:
+-----------+------------------+
|   category|       total_sales|
+-----------+------------------+
|     Sports|1802.4999999999998|
|       Home|1523.4999999999998|
|Electronics|1174.7999999999997|
|   Clothing|             790.3|
|     Beauty| 459.8999999999999|
+-----------+------------------+

4. Сума покупок за категоріями для віку 18-25:
+-----------+------------------+
|   category|       young_sales|
+-----------+------------------+
|       Home|             361.1|
|     Sports|310.49999999999994|
|Electronics|             249.6|
|   Clothing|             245.0|
|     Beauty|41.400000000000006|
+-----------+------------------+

5. Загальна сума покупок користувачів 18-25 років: 1207.6
+-----------+------------------+----------+
|   category|       young_sales|percentage|
+-----------+------------------+----------+
|       Home|             361.1|      29.9|
|     Sports|310.49999999999994|     25.71|
|Electronics|             249.6|     20.67|
|   Clothing|             245.0|     20.29|
|     Beauty|41.400000000000006|      3.43|
+-----------+------------------+----------+

6. Топ-3 категорії продуктів з найвищим відсотком витрат користувачів 18-25 років:
+-----------+------------------+----------+
|   category|       young_sales|percentage|
+-----------+------------------+----------+
|       Home|             361.1|      29.9|
|     Sports|310.49999999999994|     25.71|
|Electronics|             249.6|     20.67|
+-----------+------------------+----------+


Топ-3 категорії: ['Home', 'Sports', 'Electronics']
```