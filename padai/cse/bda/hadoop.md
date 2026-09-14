---
tags:
---
## 1. Google File System (GFS)

> **GFS** is a scalable distributed file system developed by Google for large, data-intensive applications. It runs on inexpensive commodity hardware and provides fault tolerance and high aggregate performance.

### Key Properties

- Provides a **familiar file system interface** (not POSIX standard)
- Files organized **hierarchically** in directories with path names
- Operations: create, delete, open, close, read, write
- Special operations: **Snapshot** and **Record Append**
    - **Snapshot** — low-cost copy of a file or directory tree
    - **Record Append** — multiple clients append concurrently with atomicity guaranteed

---

### GFS Architecture
![](attachments/Pasted%20image%2020260420202729.png)

**Components:**

- **Single Master** — stores all metadata; directs clients to chunk servers
- **Chunk Servers** — store actual data as Linux files on local disk
- **Clients** — interact with master for metadata; directly with chunk servers for data

---

### GFS Chunk Size

- Default chunk size: **64 MB** (much larger than traditional file systems)
- Each chunk identified by a **globally unique 64-bit chunk handle**
- Each chunk stored as a plain Linux file on a chunk server
- Default replication: **3 replicas** per chunk

### Advantages of Large Chunk Size (64 MB)

| Advantage                 | Detail                                                            |
| ------------------------- | ----------------------------------------------------------------- |
| Fewer master interactions | One request to master for chunk location covers many reads/writes |
| Reduced network overhead  | Client keeps persistent TCP connection to chunk server longer     |
| Less metadata             | Master stores less metadata → can keep it all in memory           |

### Disadvantages of Large Chunk Size

| Disadvantage           | Detail                                                     |
| ---------------------- | ---------------------------------------------------------- |
| Internal fragmentation | Small files waste space (1 file = 1 chunk, chunk is 64 MB) |
| Hot spots              | Chunk servers storing small popular files get overwhelmed  |

---

### GFS Metadata

The master stores **3 types of metadata** (all in memory):

1. File and chunk **namespaces**
2. **Mapping** from files to chunks
3. **Locations** of each chunk's replicas

- First two types also persisted via **Operation Log** on local disk
- Chunk location info is **NOT stored persistently** — master asks chunk servers at startup

### GFS Operation Log

- Historical record of critical metadata changes
- Serves as a **logical timeline** for concurrent operations
- Central to GFS — only persistent record of metadata

### GFS Consistency Model

- **Relaxed consistency model** — suitable for large distributed applications
- Balances simplicity and efficiency

---

## 2. Hadoop Distributed File System (HDFS)

> **HDFS** is a distributed file system written in **Java**, residing in **user space** (unlike FAT, NTFS, ext2 which are in kernel space). Designed to store terabytes and petabytes of data.

![](attachments/Pasted%20image%2020260420202938.png)
### HDFS vs Traditional File Systems

| Feature         | Traditional FS | HDFS                 |
| --------------- | -------------- | -------------------- |
| Location        | Kernel space   | User space           |
| Scale           | GB range       | TB/PB range          |
| Language        | C/C++          | Java                 |
| Block size      | 4 KB typical   | 64–128 MB            |
| Replication     | None           | 3x default           |
| Fault tolerance | Hardware RAID  | Software replication |

### HDFS Inspiration

- Built based on Google's GFS paper
- First major adoption: **Yahoo Inc.**
- Later adopted by: LinkedIn, Facebook, Netflix, and many more

### How HDFS Stores Files

1. File placed in HDFS → broken into **blocks** (64 MB default)
2. Blocks **replicated** across DataNodes (default: 3 copies)
3. Block locations tracked by **NameNode**

### Basic HDFS Commands

```bash
hadoop fs -ls /                      # List directory
hadoop fs -put localfile /hdfs/path  # Upload file
hadoop fs -get /hdfs/path localfile  # Download file
hadoop fs -cat /hdfs/path/file       # Print file content
hadoop fs -rmr /hdfs/path            # Delete directory
```

Advantages
- **Fault tolerance** — automatic data replication
- **Scalability** — add nodes without downtime
- **Cost-effective** — runs on commodity hardware
- **Flexibility** — handles structured, semi-structured, unstructured data
- **Data locality** — computation moves to data
- **Open-source** — Apache licensed
---

## 3. Building Blocks of Hadoop

> Hadoop follows a **Master-Slave architecture**.

![](attachments/Pasted%20image%2020260420203302.png)

### A. NameNode

- **Master** node of HDFS
- Stores all **metadata** — location of every block of every file
- Maintains a mapping: `File → [DataNode1, DataNode2, DataNode3]`
- Example:
    
    ```
    File A → DataNode1, DataNode2, DataNode4File B → DataNode1, DataNode3, DataNode4File C → DataNode2, DataNode3, DataNode4
    ```
    
- **Single Point of Failure** for the cluster
- Does NOT store actual file data — only metadata

---

### B. DataNode

- **Slave** node; stores the actual file **blocks**
- Manages file blocks on local disk
- Sends block report and heartbeats to NameNode
- Responds to NameNode's filesystem operation instructions
- Multiple DataNodes can run on different machines

---

### C. Secondary NameNode

> ⚠️ **NOT a failover/backup for NameNode** — common misconception!

- Performs **periodic housekeeping** for the NameNode
- Creates **checkpoints** of the file system namespace
- Merges the edit log with the fsimage to prevent edit log from growing too large
- Helps NameNode recover faster after a crash (from the checkpoint)

---

### D. JobTracker

- **Master** for MapReduce job management
- Accepts job requests from clients
- Assigns **tasks** to TaskTrackers based on **data locality**
    - Prefers: same DataNode → same rack → any node
- Monitors task progress; re-assigns on failure
- Ensures job completion even if a node fails

---

### E. TaskTracker

- **Slave** for MapReduce task execution
- Accepts Map, Reduce, and Shuffle tasks from JobTracker
- Sends **heartbeat messages** to JobTracker (alive signal + free slot count)
- Starts and monitors Map & Reduce tasks
- Reports progress and status back to JobTracker
- All daemons run in their own **JVM**

---

### Typical Hadoop Job Flow

```
1. Client submits MapReduce job → JobTracker
2. JobTracker queries NameNode → gets block locations
3. JobTracker places jar file in HDFS
4. JobTracker assigns Map tasks to TaskTrackers (data locality)
5. TaskTrackers fetch jar from HDFS, start Map tasks
6. TaskTrackers report progress back to JobTracker
7. Map task completes → intermediate file on local FS
8. Results passed to Reduce tasks
9. Reduce tasks write final output to HDFS
10. Intermediate data deleted after job completion
```

> 🔑 Key principle: **"Program goes to the data"** — not data to program.

---

## 4. Hadoop Cluster Modes

### A. Local / Standalone Mode

- **Default mode** after Hadoop installation
- Runs as a **single Java process**
- No daemons running
- No HDFS — uses local file system
- Best for: **development and debugging** MapReduce programs
- Easy to test without cluster setup

```bash
# Run word count in standalone mode
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.2.0.jar \
  wordcount input output
```

---

### B. Pseudo-Distributed Mode

- Runs on a **single machine** but simulates a cluster
- Each daemon runs as a **separate Java process**
- Daemons: HDFS (NameNode, DataNode), YARN (ResourceManager, NodeManager)
- Uses actual HDFS (data stored on local disk)
- Best for: **development and testing** with HDFS

#### Setup Steps

**Step 1: Environment Variables** (`~/.bashrc`)

```bash
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
```

**Step 2: Format NameNode**

```bash
hdfs namenode -format
```

**Step 3: Start HDFS**

```bash
start-dfs.sh
```

**Step 4: Start YARN**

```bash
start-yarn.sh
```

**Step 5: Verify**

- HDFS Web UI: `http://localhost:50070/`
- YARN Web UI: `http://localhost:8088/`

---

### C. Fully Distributed Mode

- Runs on a **cluster of multiple machines** (2+ nodes)
- Used in **production environments**
- Each machine runs specific daemons (NameNode on master, DataNodes on slaves)

#### Compatibility Requirements

| Category  | Supported                                       |
| --------- | ----------------------------------------------- |
| Languages | Java, Python, Perl, Ruby                        |
| OS        | Linux (production), Windows (dev only), Solaris |
| Hardware  | 32-bit Linux; 64-bit for large deployments      |
| RAM       | At least 3 GB/node                              |
| Disk      | At least 1 TB (NameNode machine)                |

#### High-Level Installation Steps

```
1.  Bind IP addresses with hostnames (/etc/hosts)
2.  Set up passwordless SSH between nodes
3.  Install Java (JDK 1.6+)
4.  Install Hadoop
5.  Set JAVA_HOME and HADOOP_HOME
6.  Update .bash_profile
7.  Create required directories (namenode, datanode)
8.  Configure XML files (core-site, hdfs-site, mapred-site, yarn-site)
9.  Set masters and slaves files
10. Format the NameNode
11. Start DFS and MapReduce services
12. Verify via web interface
```

#### Passwordless SSH Setup

```bash
# On NameNode machine:
ssh-keygen -t rsa
ssh hadoop@Host2 mkdir -p .ssh
cat ~/.ssh/id_rsa.pub | ssh hadoop@Host2 'cat >> .ssh/authorized_keys'

# Set permissions:
chmod 700 ~/.ssh
chmod 640 ~/.ssh/authorized_keys
```

#### Directory Structure (Fully Distributed)

```bash
# NameNode directories:
mkdir -p /home/hadoop/data/1/dfs/nn

# DataNode directories:
mkdir -p /home/hadoop/data/1/dfs/dn
mkdir -p /home/hadoop/data/2/dfs/dn
mkdir -p /home/hadoop/data/3/dfs/dn

# MapReduce temporary directories:
mkdir -p /home/hadoop/data/1/mapred/local
mkdir -p /home/hadoop/mapred/system
```

#### Start/Stop Commands

```bash
# Start all services:
./bin/start-dfs.sh
./bin/start-mapred.sh

# Check status:
./bin/hadoop dfsadmin -report

# Stop all:
./bin/stop-all.sh
```

#### Web Interfaces

- DFS: `http://<namenode-ip>:50070/`
- MapReduce: `http://<namenode-ip>:50030/`

---

## 5. Configuring XML Files

> All configuration files are in `$HADOOP_HOME/etc/hadoop/` (new) or `$HADOOP_HOME/conf/` (old).

---

### hadoop-env.sh

- Sets environment variables for Hadoop daemons
- Most important: `$JAVA_HOME`

```bash
export JAVA_HOME=/usr/local/jdk1.7.0_71
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_HEAP=1000        # Heap size in MB
export HADOOP_LOG_DIR=/var/log/hadoop
```

---

### core-site.xml

- Configuration for **Hadoop Core** (common to HDFS and MapReduce)
- Tells daemons where **NameNode** runs

```xml
<configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
    <!-- Or: hdfs://hostname:8020 in fully distributed mode -->
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/home/hadoop/tmp</value>
  </property>
</configuration>
```

|Parameter|Description|
|---|---|
|`fs.default.name`|URL and port of NameNode|
|`hadoop.tmp.dir`|Temporary directory for Hadoop data|

---

### hdfs-site.xml

- Configuration for **HDFS daemons** (NameNode, Secondary NameNode, DataNodes)

```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>3</value>
    <!-- Number of replicas for each block -->
  </property>
  <property>
    <name>dfs.name.dir</name>
    <value>file:///home/hadoop/hadoopinfra/hdfs/namenode</value>
    <!-- Where NameNode stores metadata and edit logs -->
  </property>
  <property>
    <name>dfs.data.dir</name>
    <value>file:///home/hadoop/hadoopinfra/hdfs/datanode</value>
    <!-- Where DataNode stores blocks -->
  </property>
  <property>
    <name>dfs.permissions</name>
    <value>true</value>
    <!-- Enable/disable permission checking -->
  </property>
</configuration>
```

|Parameter|Description|
|---|---|
|`dfs.replication`|Number of block replicas (default 3)|
|`dfs.name.dir`|NameNode metadata storage path|
|`dfs.data.dir`|DataNode block storage path|
|`dfs.permissions`|Enable HDFS permission checking|

---

### mapred-site.xml

- Configuration for **MapReduce daemons** (JobTracker, TaskTrackers)

```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
    <!-- Use YARN as MapReduce framework -->
  </property>
  <property>
    <name>mapred.job.tracker</name>
    <value>hostname:9001</value>
    <!-- Host:port of JobTracker -->
  </property>
  <property>
    <name>mapred.local.dir</name>
    <value>/home/hadoop/data/1/mapred/local,
           /home/hadoop/data/2/mapred/local</value>
    <!-- TaskTracker temp and intermediate output dirs -->
  </property>
  <property>
    <name>mapred.system.dir</name>
    <value>/home/hadoop/mapred/system</value>
    <!-- System files for MapReduce jobs -->
  </property>
</configuration>
```

|Parameter|Description|
|---|---|
|`mapreduce.framework.name`|Framework: `yarn` or `classic`|
|`mapred.job.tracker`|Host:port of JobTracker|
|`mapred.local.dir`|TaskTracker temporary data dirs|
|`mapred.system.dir`|System file storage for MR jobs|

---

### yarn-site.xml

- Configuration for **YARN** (Yet Another Resource Negotiator)

```xml
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>
```

---

### masters (file)

- Lists hostname(s) of **Secondary NameNode** machines
- Located at `conf/masters`

```
secondary-namenode-hostname
```

- On slave nodes: this file is **blank**

---

### slaves (file)

- Lists hostnames of **DataNode and TaskTracker** machines (one per line)
- Located at `conf/slaves`

```
datanode1-hostname
datanode2-hostname
datanode3-hostname
```

- On each slave node: file contains **only its own IP**

---

### Directory Permissions

|Directory|Owner|Permissions|
|---|---|---|
|`dfs.name.dir`|`hdfs:hadoop`|`drwx------` (700)|
|`dfs.data.dir`|`hdfs:hadoop`|`drwx------` (700)|
|`mapred.local.dir`|`mapred:hadoop`|`drwxr-xr-x` (755)|

---

### Configuration File Summary

|File|Configures|Key Parameters|
|---|---|---|
|`hadoop-env.sh`|JVM environment|`JAVA_HOME`, heap size, log dir|
|`core-site.xml`|Hadoop Core (common)|NameNode URL, temp dir|
|`hdfs-site.xml`|HDFS daemons|Replication, name/data dirs|
|`mapred-site.xml`|MapReduce daemons|JobTracker, local dirs|
|`yarn-site.xml`|YARN|Shuffle service|
|`masters`|Secondary NameNode|Hostname|
|`slaves`|DataNodes/TaskTrackers|Hostnames|

---

---

# Part-A Q&A (Short Answers)

---

### Q.1 What Do You Mean by Map Task?

A **[map tasks](functional%20programming%20functions.md)** is the first processing phase in Hadoop MapReduce. It:

- Reads input data as `<Key, Value>` pairs from HDFS (via RecordReader)
- Applies the user-defined `map()` function to each pair
- Emits intermediate `<Key, Value>` pairs to local disk
- One map task executes per input split (one HDFS block, typically 64–128 MB)

```
(K1, V1) → map() → (K2, V2)
```

Map tasks run in **parallel** across multiple DataNodes.

---

### Q.2 What is Reduce Task? Explain

A **[[functional programming functions| reduce task]]** is the second processing phase in MapReduce. It:

- Receives all intermediate `<Key, List[Values]>` pairs with the same key from all mappers
- Applies the user-defined `reduce()` function
- Emits the final `<Key, Value>` pairs written to HDFS

```
(K2, List[V2]) → reduce() → (K3, V3)
```

Steps within a reduce task:

1. **Fetch (Shuffle)** — copies map outputs from all mapper nodes
2. **Sort/Merge** — merges and sorts received data by key
3. **Reduce** — calls `reduce()` for each unique key

---

### Q.3 What Main Configuration Parameters Are Specified in MapReduce?

| Parameter           | Method / File                            |
| ------------------- | ---------------------------------------- |
| NameNode URL        | `core-site.xml` → `fs.default.name`      |
| Replication factor  | `hdfs-site.xml` → `dfs.replication`      |
| JobTracker location | `mapred-site.xml` → `mapred.job.tracker` |
| Mapper class        | `job.setMapperClass()` in Driver         |
| Reducer class       | `job.setReducerClass()` in Driver        |
| Combiner class      | `job.setCombinerClass()` in Driver       |
| Output key type     | `job.setOutputKeyClass()`                |
| Output value type   | `job.setOutputValueClass()`              |
| Input/Output paths  | `FileInputFormat` / `FileOutputFormat`   |
| Number of reducers  | `job.setNumReduceTasks()`                |

---

### Q.4 Explain JobConf in MapReduce

`JobConf` is a class in the **Old MapReduce API** (`org.apache.hadoop.mapred`) used to configure a MapReduce job. It extends `Configuration`.

```java
JobConf conf = new JobConf(MyDriver.class);
conf.setJobName("MyJob");
conf.setMapperClass(MyMapper.class);
conf.setReducerClass(MyReducer.class);
conf.setOutputKeyClass(Text.class);
conf.setOutputValueClass(IntWritable.class);
conf.setInputFormat(TextInputFormat.class);
conf.setOutputFormat(TextOutputFormat.class);
FileInputFormat.setInputPaths(conf, new Path(args[0]));
FileOutputFormat.setOutputPath(conf, new Path(args[1]));
JobClient.runJob(conf);
```

- Allows configuration of Mapper, Reducer, Combiner, Partitioner, InputFormat, OutputFormat
- Replaced by `Configuration` + `Job` class in the New API

---


---

### Q.6 What is RecordReader in MapReduce?

**RecordReader** converts raw input bytes using metadata from an `InputSplit` into `<Key, Value>` pairs for the Mapper.

- Part of `InputFormat`
- Default (`TextInputFormat`) output: Key = byte offset (`LongWritable`), Value = line (`Text`)
- Mapper never directly reads HDFS — always through RecordReader
- One RecordReader per InputSplit

---

### Q.7 Define Writable Data Types in MapReduce
#important
Hadoop's serializable wrappers for Java types:

| Writable          | Java Type | Use              |
| ----------------- | --------- | ---------------- |
| `IntWritable`     | `int`     | Counts, integers |
| `LongWritable`    | `long`    | Byte offsets     |
| `FloatWritable`   | `float`   | Decimals         |
| `DoubleWritable`  | `double`  | High-precision   |
| `BooleanWritable` | `boolean` | Flags            |
| `Text`            | `String`  | Words, lines     |
| `NullWritable`    | null      | Ignored field    |
| `BytesWritable`   | `byte[]`  | Binary data      |

- **Keys** → `WritableComparable` (supports sorting)
- **Values** → `Writable` (serialization only)

---


### Q.9 Explain What is Shuffling in MapReduce

**Shuffling** is the process of transferring intermediate Map output from mapper nodes to the appropriate reducer nodes. It occurs between the Map and Reduce phases.

Steps:

1. Mapper writes output to **local disk** (not HDFS)
2. **Partitioner** determines which reducer gets which key
3. Framework **copies (shuffles)** map outputs over the network to reducer nodes
4. Reducer **merges and sorts** received data by key

This is the most **network-intensive** phase. Combiner reduces shuffle data volume.

---

### Q.10 Explain What is Distributed Cache in MapReduce Framework

**Distributed Cache** is a mechanism to share read-only files (lookup tables, JARs, archives) across all nodes in the cluster before a job runs.

**Use cases:**

- Sharing a country-code CSV with all mappers
- Distributing third-party library JARs

```java
// Driver:
job.addCacheFile(new URI("/hdfs/path/to/lookup.txt"));

// Mapper setup():
URI[] cacheFiles = context.getCacheFiles();
```

**Benefits:**

- File copied once per node (not per task)
- Available locally to all tasks on that node
- Avoids repeated HDFS reads during execution

---

### Q.11 How is Identity Mapper Different from Chain Mapper?

| Feature   | Identity Mapper                  | Chain Mapper                        |
| --------- | -------------------------------- | ----------------------------------- |
| Function  | Passes input unchanged to output | Chains multiple mappers in sequence |
| Use case  | Testing, pass-through, debugging | Multi-step transformation           |
| Data flow | Input → Output (unchanged)       | Input → M1 → M2 → ... → Output      |
| Setup     | Default; no configuration        | `ChainMapper.addMapper()` for each  |

**Identity Mapper** — no transformation; output equals input. **Chain Mapper** — multiple mapper classes applied sequentially within one Map phase.

---

### Q.12 Explain the Core Methods of a Reducer

```java
public class MyReducer extends Reducer<KIN, VIN, KOUT, VOUT> {

    // Called once before any reduce calls
    protected void setup(Context context) { }

    // Called once per unique key — core logic
    protected void reduce(KIN key, Iterable<VIN> values, Context context) { }

    // Called once after all reduce calls
    protected void cleanup(Context context) { }

    // Controls execution flow — override for custom behavior
    public void run(Context context) {
        setup(context);
        while (context.nextKey())
            reduce(context.getCurrentKey(), context.getValues(), context);
        cleanup(context);
    }
}
```

| Method      | When                | Purpose              |
| ----------- | ------------------- | -------------------- |
| `setup()`   | Once at start       | Initialize resources |
| `reduce()`  | Once per unique key | Core aggregation     |
| `cleanup()` | Once at end         | Release resources    |
| `run()`     | Controls lifecycle  | Custom flow          |

---

### Q.13 What Role Do RecordReader, Combiner and Partitioner Play?

**RecordReader** — sits between InputFormat and Mapper

- Converts raw bytes → structured `<K,V>` pairs
- Controls how input is parsed (text, binary, XML, JSON)
- One per InputSplit

**Combiner** — sits between Mapper and Shuffle

- Local pre-aggregation on mapper output
- Reduces network I/O significantly
- Optional; only for associative/commutative operations

**Partitioner** — sits between Mapper and Reducer

- Decides which reducer receives which key
- Default: `HashPartitioner`
- Ensures all values for a key go to the **same** reducer

```
Mapper → [Combiner] → [Partitioner] → Shuffle/Sort → Reducer
```

---

---

# Part-B Q&A (Medium Answers)

### Q.15 Explain the Process of Analyzing Data with Hadoop

1. **Data Ingestion** — Raw data loaded into HDFS via `hdfs dfs -put`, Sqoop, Flume, or Kafka
2. **Storage** — HDFS stores data in blocks (128 MB), replicated 3x across DataNodes
3. **Job Configuration** — Developer writes Driver, Mapper, Reducer; configures the Job
4. **Job Submission** — Driver submits job to JobTracker (old) / ResourceManager (YARN)
5. **Task Scheduling** — JobTracker assigns map tasks to nodes where data is local (data locality)
    
6. **Map Phase** — Each mapper reads its split, processes records, emits intermediate `<K,V>`
    
7. **Shuffle & Sort** — Intermediate data moved to correct reducer nodes and sorted
    
8. **Reduce Phase** — Reducers aggregate grouped values, write final output to HDFS
    
9. **Output** — Results available in HDFS output directory as `part-r-nnnnn` files
    
10. **Analysis** — Output read via Hive (SQL), Pig (scripting), or custom tools
    

Key advantage: **Data locality** — computations moved to data, not data to computations.

---

### Q.16 Differences Between Old and New Java MapReduce API

| Aspect            | Old API (`mapred`)             | New API (`mapreduce`)           |
| ----------------- | ------------------------------ | ------------------------------- |
| Package           | `org.apache.hadoop.mapred`     | `org.apache.hadoop.mapreduce`   |
| Mapper/Reducer    | Interface                      | Abstract Class                  |
| Communication     | `OutputCollector` + `Reporter` | Single `Context` object         |
| Job submission    | `JobClient.runJob(conf)`       | `job.waitForCompletion(true)`   |
| Job config        | `JobConf`                      | `Configuration` + `Job`         |
| Reducer values    | `Iterator<V>`                  | `Iterable<V>`                   |
| Execution control | `MapRunnable` (mapper only)    | `run()` on both                 |
| Output naming     | `part-nnnnn`                   | `part-m-nnnnn` / `part-r-nnnnn` |
| Hadoop version    | ≤ 0.20                         | ≥ 0.21                          |

> Old API still works in modern Hadoop — not removed, just superseded.

---

### Q.17 Explain Mapper — How It Works

The **Mapper** transforms input records into intermediate key-value pairs.

**Lifecycle:**

```
setup(context)       ← once before processing
    ↓
map(key, value, context)  ← once per input record
    ↓
cleanup(context)     ← once after all records
```

**Internal Working:**

1. InputFormat creates InputSplits (one per mapper)
2. RecordReader converts split → `<K,V>` pairs
3. `map()` called once per pair
4. Output buffered in memory (100 MB ring buffer)
5. Buffer spills to local disk when 80% full (sorted)
6. Multiple spills merged into one sorted file
7. Partitioner tags each record with destination reducer

**New API:**

```java
public class WordMapper extends Mapper<Object, Text, Text, IntWritable> {
    private Text word = new Text();
    private final static IntWritable one = new IntWritable(1);

    public void map(Object key, Text value, Context context)
            throws IOException, InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString());
        while (itr.hasMoreTokens()) {
            word.set(itr.nextToken());
            context.write(word, one);
        }
    }
}
```

---

### Q.18 Define Combiner

A **Combiner** is an optional component that performs **local aggregation** of Map output on each mapper node before data is sent over the network to reducers.

Also called: **Semi-reducer** or **Mini-reducer**

**Rules:**

- Must implement `Reducer` interface
- Input types = Mapper output types
- Output types = Reducer input types
- Operation must be **associative** and **commutative**

**Valid:** sum, count, max, min **Invalid:** average, median

**Example — Without Combiner:**

```
Node sends: <Java,1> <Java,1> <Java,1>   (3 records over network)
```

**With Combiner:**

```
Combiner runs: <Java,3>   (1 record over network — 3x less data)
```

```java
job.setCombinerClass(IntSumReducer.class);
```

---

# Part-C Q&A (Long Answers)

### Q.21 Explain a Weather Dataset in Detail

#### Source

NCDC (National Climatic Data Center) — worldwide weather sensor data. Available: `https://github.com/tomwhite/hadoop-book/tree/master/input/ncdc/all`

#### Structure

- One compressed file per year (e.g., `1901.gz`)
- Fixed-width format records (not CSV)
- Each record = one weather reading from one sensor

#### Record Format

```
Position   Field
0-5        Station ID
15-18      Year (4 digits)
87         Temperature sign (+ or -)
88-91      Temperature (tenths of Celsius, 4 digits)
92         Quality code
```

#### Sample Record

```
0057328999999193401010600004+51317+028783FM-12+0024...
                 ^^^^                       ^^^^
                 YEAR=1934                  TEMP=+0024 (=+0.24°C)
```

#### Valid Quality Codes

|Code|Meaning|
|---|---|
|0|Passed gross limits|
|1|Passed all checks|
|4|Passed extreme limits|
|5|Passed all checks|
|9|Estimated — passed|

#### MapReduce Design

**Mapper (AverageMapper.java):**

```java
public class AverageMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    public static final int MISSING = 9999;

    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        String line = value.toString();
        String year = line.substring(15, 19);

        int temperature;
        if (line.charAt(87) == '+')
            temperature = Integer.parseInt(line.substring(88, 92));
        else
            temperature = Integer.parseInt(line.substring(87, 92));

        String quality = line.substring(92, 93);
        if (temperature != MISSING && quality.matches("[01459]"))
            context.write(new Text(year), new IntWritable(temperature));
    }
}
```

**Reducer (AverageReducer.java):**

```java
public class AverageReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        int total = 0, count = 0;
        for (IntWritable value : values) {
            total += value.get();
            count++;
        }
        context.write(key, new IntWritable(total / count));
    }
}
```

**Sample Output:**

```
1901    -6
1902     3
1950    14
2000    21
```

#### Why This Dataset?

- Real-world semi-structured data (not clean CSV)
- Demonstrates fixed-width parsing
- Shows quality filtering in `map()`
- Multi-file input → natural parallelism (one file per year)
- Classic example in "Hadoop: The Definitive Guide"

---

### Q.22 Notes on: (a) Reducer (b) Partitioner

#### (a) Reducer

The **Reducer** processes grouped intermediate key-value pairs from all mappers and produces final output.

**Declaration:**

```java
public class MyReducer extends Reducer<KIN, VIN, KOUT, VOUT>
```

**Four Generic Types:**

1. Input Key (= Mapper output key)
2. Input Value (= Mapper output value)
3. Output Key
4. Output Value

**Complete Example:**

```java
public static class IntSumReducer
        extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();

    @Override
    protected void setup(Context context) throws IOException {
        // Initialize once before reduce tasks
    }

    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable val : values) {
            sum += val.get();
        }
        result.set(sum);
        context.write(key, result);
    }

    @Override
    protected void cleanup(Context context) throws IOException {
        // Finalize once after reduce tasks
    }
}
```

**Output Files:**

- One file per reducer: `part-r-00000`, `part-r-00001`, ...
- Combined = complete output of the job

**Setting Reducer Count:**

```java
job.setNumReduceTasks(3);   // default = 1; 0 = no reduce phase
```

---

#### (b) Partitioner



---


### Q.24 Explain RecordReader in Detail

**RecordReader** is responsible for reading raw input data from an `InputSplit` and converting it into `<Key, Value>` pairs that are fed one-by-one to the Mapper.

#### Position in Pipeline

```
HDFS Block → InputFormat → InputSplit → RecordReader → <K,V> → Mapper
```

#### Default RecordReader — LineRecordReader

Used by `TextInputFormat`:

- **Key:** `LongWritable` — byte offset of the line from start of file
- **Value:** `Text` — the raw line content

```
File line "Hello World" at byte 42:
  Key   = LongWritable(42)
  Value = Text("Hello World")
```

#### Custom RecordReader (New API)

```java
public class MyRecordReader extends RecordReader<LongWritable, Text> {
    private long start, end, pos;
    private LineReader reader;
    private LongWritable currentKey = new LongWritable();
    private Text currentValue = new Text();

    @Override
    public void initialize(InputSplit split, TaskAttemptContext ctx)
            throws IOException {
        FileSplit fileSplit = (FileSplit) split;
        start = fileSplit.getStart();
        end = start + fileSplit.getLength();
        Path path = fileSplit.getPath();
        FileSystem fs = path.getFileSystem(ctx.getConfiguration());
        FSDataInputStream in = fs.open(path);
        reader = new LineReader(in);
        pos = start;
    }

    @Override
    public boolean nextKeyValue() throws IOException {
        currentKey.set(pos);
        int bytesRead = reader.readLine(currentValue);
        if (bytesRead == 0) return false;
        pos += bytesRead;
        return true;
    }

    @Override
    public LongWritable getCurrentKey() { return currentKey; }

    @Override
    public Text getCurrentValue() { return currentValue; }

    @Override
    public float getProgress() {
        return (float)(pos - start) / (end - start);
    }

    @Override
    public void close() throws IOException { reader.close(); }
}
```

#### InputFormat Types

|InputFormat|Key|Value|Use Case|
|---|---|---|---|
|`TextInputFormat`|`LongWritable` (offset)|`Text` (line)|Default; text files|
|`KeyValueTextInputFormat`|`Text`|`Text`|Tab-separated key-value|
|`SequenceFileInputFormat`|custom|custom|Binary sequence files|
|`NLineInputFormat`|`LongWritable`|`Text`|Fixed N lines per split|

#### Key Roles

1. Reads assigned `InputSplit` without re-reading other splits
2. Decodes raw bytes → meaningful `<K,V>` pairs
3. Reports progress via `getProgress()`
4. Each Mapper gets exactly one RecordReader instance
5. Handles record boundary detection across block boundaries

---

### Q.25 Explain MapReduce in Detail

#### Definition

MapReduce is a distributed computing paradigm for processing massive datasets in parallel across commodity hardware clusters. Developed by Google; implemented in Hadoop as the primary processing framework.

#### Fundamental Principle

```
"Divide the computation across many machines,
 each processing a small portion of the data,
 then combine the results."
```

#### Complete Architecture

![](attachments/Pasted%20image%2020260420153243.png)

![](attachments/Pasted%20image%2020260420153302.png)
#### All 7 Phases Explained
![](attachments/Pasted%20image%2020260420153431.png)
![](attachments/Pasted%20image%2020260420153443.png)
**Phase 1 — Input Splitting**

- HDFS file divided into InputSplits (≈ 1 block each = 128 MB)
- Each split assigned to one mapper
- More splits = more parallelism

**Phase 2 — Map**

- RecordReader parses split → `<K1,V1>` pairs
- `map()` processes each pair → emits `<K2,V2>`
- Output written to local memory ring buffer (100 MB)
- Buffer spills to local disk when 80% full (sorted by key+partition)
- Multiple spills merged into one sorted file

**Phase 3 — Combiner (optional)**

- Runs on sorted mapper output on same node
- Pre-aggregates values for same key locally
- Dramatically reduces shuffle data volume

**Phase 4 — Partitioning**

- Every `<K2,V2>` pair tagged with destination reducer ID
- `HashPartitioner` by default: `hash(K2) % numReducers`
- Ensures all values for a key go to **one** reducer

**Phase 5 — Shuffle**

- HTTP-based data transfer from mapper nodes to reducer nodes
- Each reducer fetches the data meant for it from all mappers
- Most network-intensive phase

**Phase 6 — Sort/Merge**

- Reducer receives multiple sorted files (one from each mapper)
- Merges them into one sorted stream
- All values for a key contiguous and grouped

**Phase 7 — Reduce**

- `reduce()` called once per unique key
- Processes `Iterable<V2>` → emits final `<K3,V3>`
- Output written to HDFS via RecordWriter

#### Word Count — Full Trace

```
Input:        "Hello World Hello"
              "World Java Hello"

Map Output:   <Hello,1><World,1><Hello,1>
              <World,1><Java,1><Hello,1>

After Sort:   <Hello,[1,1,1]><Java,[1]><World,[1,1]>

Reduce Out:   <Hello,3><Java,1><World,2>

HDFS Output:
Hello   3
Java    1
World   2
```

#### MapReduce Counters (built-in monitoring)

```
Map input records      = 2
Map output records     = 6
Reduce input records   = 6
Reduce output records  = 3
```

#### Fault Tolerance

- **Map failure** → JobTracker reschedules on another node (input still in HDFS)
- **Reduce failure** → Reschedules on another node (re-fetches map outputs)
- **Node failure** → Data replica used from another DataNode
- Default retry: 4 attempts per task

#### Limitations of MapReduce

| Limitation           | Impact                                     |
| -------------------- | ------------------------------------------ |
| High disk I/O        | Intermediate data always written to disk   |
| High latency         | Not suitable for real-time processing      |
| Iterative algorithms | Each iteration = new job; very slow for ML |
| Code verbosity       | Simple tasks = many classes                |

> Modern alternatives: **Apache Spark** (in-memory, 10-100x faster for iterative), **Apache Flink** (true streaming). But MapReduce remains the backbone of Hadoop batch processing.

---
