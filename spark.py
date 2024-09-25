# Полагаю, в Задании 3 имеется в виду связь Продукты <> Категории (Один-ко-многим)
# Т.е таблицы имеют вид "Продукты" -< "Продукты_в_категориях" >- "Категории"
# Остальное см. в README
from pyspark.sql import SparkSession, Row
import os
import sys

if __name__ == "__main__":
    os.environ['PYSPARK_PYTHON'] = sys.executable
    spark = SparkSession.builder.getOrCreate()

    products = spark.createDataFrame([
        Row(id=1, product_name="Молоко"),
        Row(id=2, product_name="Нож"),
        Row(id=3, product_name="Вилка"),
        Row(id=4, product_name="Монитор"),
        Row(id=5, product_name="Сосиски")
    ])
    products.createOrReplaceTempView("products")

    categories = spark.createDataFrame([
        Row(id=1, category_name="Кухонные приборы"),
        Row(id=2, category_name="Еда"),
        Row(id=3, category_name="Книги"),
        Row(id=4, category_name="Молочные продукты")
    ])
    categories.createOrReplaceTempView("categories")

    products_categories = spark.createDataFrame([
        Row(product=1, category=2),
        Row(product=1, category=4),
        Row(product=5, category=2),
        Row(product=2, category=1),
        Row(product=3, category=1)
    ])
    products_categories.createOrReplaceTempView("products_categories")

    # 1 метод: чистый SQL
    spark.sql("select product_name, category_name from products p left join products_categories pc "
              "on p.id = pc.product left join categories c on pc.category == c.id").show()

    # 2 метод: функции pyspark
    (products.join(products_categories, products.id == products_categories.product, "left")
     .join(categories, products_categories.category == categories.id,"left")
     .select(products.product_name, categories.category_name)
     .show())