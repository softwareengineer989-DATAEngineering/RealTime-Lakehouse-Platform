from tempfile import TemporaryDirectory

from retaillake.spark.session.spark_session import get_spark

spark = get_spark()

tmp = TemporaryDirectory()

spark.range(10).write.format("delta").save(tmp.name)

spark.read.format("delta").load(tmp.name).show()