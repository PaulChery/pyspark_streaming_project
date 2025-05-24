from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

# 1. Create Spark session
spark = SparkSession.builder \
    .appName("Socket Streaming Demo") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 2. Define schema for incoming JSON data
schema = StructType([
    StructField("user_id", StringType()),
    StructField("amount", DoubleType()),
    StructField("timestamp", TimestampType())
])

# 3. Read streaming data from a socket
raw_df = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# 4. Parse each line as JSON and extract fields
json_df = raw_df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# 5. Perform windowed aggregation by user and 1-minute time window
agg_df = json_df.groupBy(
    window(col("timestamp"), "1 minute"),
    col("user_id")
).sum("amount")

# 6. Output results to the console
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()
