
HADOOP_HOME=/usr/local/hadoop

$HADOOP_HOME/bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar \
-file $0    -mapper $0 \ -file $1   -reducer $1 \
-input $2 -output $3
