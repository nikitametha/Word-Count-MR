#### Word Count Map Reduce with HDFS
Simple MR job for word count, based on dataset with format as in ```data12``` file.

### CONFIGURE HADOOP
```  start-dfs.sh ```

```  start-yarn.sh ```

##### Meanwhile, make those two python files executable using
``` chmod +x /home/nikita/mapper.py ```


``` chmod +x /home/nikita/reducer.py ```

Change names accordingly, duh.

#### Load ``` data12 ``` to hdfs

``` cd $HADOOP_HOME ```

```  hdfs dfs -put ~/data12 /input ```

Assuming you have ``` /input ``` as a directory in hdfs, and the data12 file is in ``` home/user ``` directory

Now to run Map Reduce, using Hadoop Streaming

``` hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar -D mapreduce.job.reduces=2     -file /home/nikita/mapper.py    -mapper /home/nikita/mapper.py -file /home/nikita/reducer.py   -reducer '/home/nikita/reducer.py hi1' -input /input/data12  -output /input/data1out ```

Once done, view using
``` hdfs dfs -cat input/data1out/part-00000 ``` 

``` hdfs dfs -cat input/data1out/part-00001 ``` 

On running the second one, it should show you 

``` hi1   6 ```

I think.

Yayy done. :)

Note- You may have to 'leave safemode' for hadoop streaming to work (some 'NameNode: is in safemode' Exception thingy comes)

so like..use

``` hdfs dfsadmin -safemode leave ```

Or just google it idk :|
