from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def print_distinct_content_ratings(file_path):
    spark = SparkSession.builder.appName("DistinctContentRatings").getOrCreate()
    df = spark.read.option("header", "true").csv(file_path)
    known_ratings = ["Unrated", "Everyone", "Everyone 10+", "Teen", "Mature 17+", "Adults only 18+"]
    filtered_df = df.filter(col("Content Rating").isin(known_ratings))
    distinct_content_ratings = filtered_df.select("Content Rating").distinct().collect()
    print("Valori distinti sotto la colonna 'Content Rating':")
    for row in distinct_content_ratings:
        print(row["Content Rating"])
    spark.stop()

file_path = "../Google-Playstore.csv"  
print_distinct_content_ratings(file_path)

