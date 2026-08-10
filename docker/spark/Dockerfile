FROM apache/spark:4.0.0

USER root

ARG SPARK_VERSION=4.0.0
ARG SCALA_VERSION=2.13
ARG DELTA_VERSION=4.0.0
ARG KAFKA_CLIENT_VERSION=3.6.1
ARG COMMONS_POOL_VERSION=2.12.0

COPY docker/spark/requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt


# Download Spark 4.0.0 + Delta 4.0.0 + Kafka Streaming Runtime JARs
RUN curl -L \
https://repo1.maven.org/maven2/io/delta/delta-spark_${SCALA_VERSION}/${DELTA_VERSION}/delta-spark_${SCALA_VERSION}-${DELTA_VERSION}.jar \
-o /opt/spark/jars/delta-spark.jar && \

curl -L \
https://repo1.maven.org/maven2/io/delta/delta-storage/${DELTA_VERSION}/delta-storage-${DELTA_VERSION}.jar \
-o /opt/spark/jars/delta-storage.jar && \

curl -L \
https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_${SCALA_VERSION}/${SPARK_VERSION}/spark-sql-kafka-0-10_${SCALA_VERSION}-${SPARK_VERSION}.jar \
-o /opt/spark/jars/spark-sql-kafka.jar && \

curl -L \
https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_${SCALA_VERSION}/${SPARK_VERSION}/spark-token-provider-kafka-0-10_${SCALA_VERSION}-${SPARK_VERSION}.jar \
-o /opt/spark/jars/spark-token-provider-kafka.jar && \

curl -L \
https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/${KAFKA_CLIENT_VERSION}/kafka-clients-${KAFKA_CLIENT_VERSION}.jar \
-o /opt/spark/jars/kafka-clients.jar && \

curl -L \
https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/${COMMONS_POOL_VERSION}/commons-pool2-${COMMONS_POOL_VERSION}.jar \
-o /opt/spark/jars/commons-pool2.jar

COPY docker/spark/entrypoint.sh /entrypoint.sh

COPY docker/spark/log4j2.properties /opt/spark/conf/log4j2.properties

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]

