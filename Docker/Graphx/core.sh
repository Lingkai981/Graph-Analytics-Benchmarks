for dataset in Diameter; do
    # hdfs dfs -rm /graphx_data/input.txt
    # hdfs dfs -cp /graphx_data/graphx-weight-edges-8-${dataset}.txt /graphx_data/input.txt
    # hdfs dfs -ls /graphx_data

    # hdfs dfs -rm /graphx_data/input.txt
    # hdfs dfs -put /home/admin/GraphX/CoreDecomposition/input.txt /graphx_data
    for machines in 16; do
    threads=32
    tot_core=$((machines*threads))
    $SPARK_HOME/bin/spark-submit \
        --class CoreExample \
        --master spark://GraphK8sMaster:7077 \
        --conf spark.executor.instances=1 \
        --conf spark.executor.memory=480G \
        --total-executor-cores $tot_core \
        --conf spark.executor.cores=$threads \
        --driver-memory 480G \
        coreexample_2.11-0.1.jar $tot_core 3600000 \
        > aaa${dataset}-8-${machines}machines-${threads}threads.txt
    done
done