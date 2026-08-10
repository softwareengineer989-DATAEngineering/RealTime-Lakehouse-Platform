from pyspark.sql.types import *

ORDER_SCHEMA = StructType([
    StructField("order_id", IntegerType()),
    StructField("user_id", IntegerType()),
    StructField("eval_set", StringType()),
    StructField("order_number", IntegerType()),
    StructField("order_dow", IntegerType()),
    StructField("order_hour_of_day", IntegerType()),
    StructField("days_since_prior_order", DoubleType())
])