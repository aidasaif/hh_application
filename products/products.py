from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnull
import os
import pyspark
#
os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["PYSPARK_PYTHON"] = r"C:\Users\Admin\PycharmProjects\hh_application\.venv310\Scripts\python.exe"


session = SparkSession.builder \
    .appName("Products") \
    .config("spark.sql.broadcastTimeout", "600") \
    .config("spark.sql.shuffle.partitions", "8") \
    .config("spark.network.timeout", "10000000s") \
    .config("spark.driver.extraJavaOptions", "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED") \
    .getOrCreate()


products = session.createDataFrame([
    (1, 'Яблоко'),
    (2, 'Банан'),
    (3, 'Груша'),
    (4, 'Молоко'),
    (5, 'Сметана'),
    (6, 'Творог'),
    (7, 'Курица'),
    (8, 'Оливковое масло')
], ['product_id', 'product_name'])

categories = session.createDataFrame([
    (1, 'Молочные продукты'),
    (2, 'Фрукты'),
    (3, 'Овощи')
], ['category_id', 'category_name'])

prod_categ = session.createDataFrame([
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 1),
    (5, 1),
    (6, 1)
], ['product_id', 'category_id'])


prod_cat_temp = products.join(prod_categ, on='product_id', how='left')
prod_cat_join = prod_cat_temp.join(categories, on='category_id', how='left')

select_prod_categ = prod_cat_join.select(['product_name', 'category_name'])
select_prod_no_categ = prod_cat_join.filter(col('category_name').isNull()).select('product_name')

print('Продукт - Категория:')
select_prod_categ.show()

print('Продукты без категории:')
select_prod_no_categ.show()

# select_prod_categ.explain(True)
# select_prod_no_categ.explain(True)


session.stop()


