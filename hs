
HADOOP_HOME=/usr/local/hadoop
HADOOP_CMD=$HADOOP_HOME/bin/hadoop
HADOOP_STREAMING=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar 

echo $0
echo $1
echo $2
echo $3

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-file $1 -mapper $1 \
-file $2 -reducer $2 \
-input $3 -output $4
