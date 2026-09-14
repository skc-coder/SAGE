## 3. Driver

The **Driver** is the control center of a MapReduce job. It runs on the **client machine** and configures everything before submitting the job to the cluster.

#### Responsibilities

1. Parse command-line input/output paths
2. Create `Job` / `JobConf` object
3. Set all components (Mapper, Reducer, Combiner, Partitioner)
4. Define input/output key-value types and formats
5. Submit job and wait for completion
6. Return success/failure to the caller

#### Complete New API Driver

```java
public class AverageDriver {
    public static void main(String[] args) throws Exception {

        // Validate arguments
        if (args.length != 2) {
            System.err.println("Usage: AverageDriver <input> <output>");
            System.exit(-1);
        }

        // Create Configuration and Job
        Configuration conf = new Configuration();
        Job job = new Job(conf, "Average Temperature");

        // Identify the JAR to distribute to cluster nodes
        job.setJarByClass(AverageDriver.class);

        // Set Mapper and Reducer
        job.setMapperClass(AverageMapper.class);
        job.setReducerClass(AverageReducer.class);

        // Set output types
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        // Set input and output paths
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        // Submit and wait
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

#### Key `Job` Methods

| Method                        | Purpose                             |
| ----------------------------- | ----------------------------------- |
| `Job.getInstance(conf, name)` | Create job with configuration       |
| `setJarByClass(Class)`        | Locate JAR for cluster distribution |
| `setMapperClass(Class)`       | Set mapper implementation           |
| `setReducerClass(Class)`      | Set reducer implementation          |
| `setCombinerClass(Class)`     | Set optional combiner               |
| `setPartitionerClass(Class)`  | Set partitioner                     |
| `setOutputKeyClass(Class)`    | Final output key type               |
| `setOutputValueClass(Class)`  | Final output value type             |
| `setNumReduceTasks(int)`      | Number of reducers                  |
| `waitForCompletion(verbose)`  | Submit and block until done         |
## 4. Mapper

> The **Mapper** reads input as `<K1, V1>` pairs and emits intermediate `<K2, V2>` pairs. One mapper runs per record reader per input split.

### New API Mapper

```java
public class MyMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    @Override
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString());
        while (itr.hasMoreTokens()) {
            word.set(itr.nextToken());
            context.write(word, one);
        }z
    }
}
```

### Old API Mapper

```java
public class MyMapper extends MapReduceBase
        implements Mapper<LongWritable, Text, Text, IntWritable> {
    public void map(LongWritable key, Text value,
            OutputCollector<Text, IntWritable> output, Reporter reporter)
            throws IOException {
        output.collect(key, value);
    }
}
```

### Mapper Generic Types

```
Mapper<InputKey, InputValue, OutputKey, OutputValue>
  K1 = LongWritable  (byte offset of line)
  V1 = Text          (line content)
  K2 = Text          (word)
  V2 = IntWritable   (count = 1)
```

---

## 5. Reducer

> The **Reducer** takes the sorted/grouped `<K2, List[V2]>` pairs from mappers and emits final `<K3, V3>` pairs.

### New API Reducer

```java
public class MyReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();

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
}
```

### Old API Reducer

```java
public class MyReducer extends MapReduceBase
        implements Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterator<IntWritable> values,
            OutputCollector<Text, IntWritable> output, Reporter reporter)
            throws IOException {
        output.collect(key, value);
    }
}
```

### Core Methods of Reducer

|Method|Description|
|---|---|
|`setup(Context)`|Called once before reduce tasks begin|
|`reduce(Key, Iterable<Values>, Context)`|Called once per unique key|
|`cleanup(Context)`|Called once after all reduce tasks complete|
|`run(Context)`|Controls the entire execution flow|

---

## 6. RecordReader

> **RecordReader** reads raw input data and converts it into `<Key, Value>` pairs fed to the Mapper. It is the first phase of MapReduce.

### How it Works

- Part of the `InputFormat` class
- Default: `TextInputFormat` → creates `<LongWritable, Text>` pairs
    - Key = byte offset of the line from start of file
    - Value = the actual line of text

### Example Input → RecordReader Output

```
Input file lines:
  "What do you mean by Object"    →  <1, "What do you mean by Object">
  "What do you know about Java"   →  <2, "What do you know about Java">
  "What is Java Virtual Machine"  →  <3, "What is Java Virtual Machine">
```

### Custom RecordReader (New API)

```java
public class MyRecordReader extends RecordReader<LongWritable, Text> {
    @Override
    public void initialize(InputSplit split, TaskAttemptContext context) { ... }

    @Override
    public boolean nextKeyValue() throws IOException { ... }

    @Override
    public LongWritable getCurrentKey() { ... }

    @Override
    public Text getCurrentValue() { ... }

    @Override
    public float getProgress() { ... }

    @Override
    public void close() { ... }
}
```

---

## 7. Combiner

> A **Combiner** (also called semi-reducer) performs local aggregation on Mapper output before sending data over the network to Reducers. It is **optional** but greatly reduces network traffic.

### Why Use a Combiner?

- Map output can be very large
- Sending all map output over network = expensive
- Combiner pre-aggregates locally on the same node
- Reduces volume of data transferred to Reducer

### Rules

- Must implement the `Reducer` interface
- Input types must match Mapper output types
- Output types must match Reducer input types
- Must be **commutative** and **associative** (e.g., sum, max — not average)

### Combiner Phase Flow

```
Mapper Output:
<What,1> <do,1> <you,1> <What,1> <do,1> <Java,1> <What,1> <Java,1>
                         ↓ (Combiner runs locally)
<What,3> <do,2> <you,1> <Java,2>
                         ↓ (only this goes over the network)
                       Reducer
```

### Setting Combiner in Job

```java
job.setCombinerClass(IntSumReducer.class);
```

> ✅ Combiner = same class as Reducer when operation is sum/max/min ❌ Cannot use Combiner for average (it's not associative)

---

## 8. Partitioner

> The **Partitioner** determines which reducer receives which key-value pair after the Map phase.

**Default (HashPartitioner):**
- HashPartitioner — default
- Formula: partition = (key.hashCode() & Integer.MAX_VALUE) % numReduceTasks
- Ensures all values for a given key go to the same reducer
```java
public int getPartition(K key, V value, int numReduceTasks) {
    return (key.hashCode() & Integer.MAX_VALUE) % numReduceTasks;
}
```

**Custom Partitioner Example:**

```java
public class FirstLetterPartitioner extends Partitioner<Text, IntWritable> {
    @Override
    public int getPartition(Text key, IntWritable value, int numReduceTasks) {
        char c = key.toString().toLowerCase().charAt(0);
        if (c < 'i') return 0 % numReduceTasks;       // a-h → Reducer 0
        else if (c < 'q') return 1 % numReduceTasks;  // i-p → Reducer 1
        else return 2 % numReduceTasks;                // q-z → Reducer 2
    }
}
```

**Register:**

```java
job.setPartitionerClass(FirstLetterPartitioner.class);
job.setNumReduceTasks(3);
```

**Why Custom Partitioners?**

- Prevent **data skew** (one reducer overloaded)
- Group related keys (same region, same date range)
- Enable **secondary sort** patterns
- Ensure sorted output across reducer files
---

## 9. Weather Dataset Example (NCDC)

> Goal: Find the **average temperature per year** from NCDC weather sensor data.

### Data Format (fixed-width fields)

```
Characters 15-19  → Year
Character  87     → Sign of temperature (+ or -)
Characters 87-92  → Temperature value
Characters 92-93  → Quality flag (valid: 0,1,4,5,9)
```

### AverageMapper.java

```java
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import java.io.IOException;

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

### AverageReducer.java

```java
import org.apache.hadoop.mapreduce.*;
import java.io.IOException;

public class AverageReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        int total = 0;
        int count = 0;
        for (IntWritable value : values) {
            total += value.get();
            count++;
        }
        context.write(key, new IntWritable(total / count));
    }
}
```

### AverageDriver.java

```java
import org.apache.hadoop.io.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class AverageDriver {
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: AverageDriver <input> <output>");
            System.exit(-1);
        }
        Job job = new Job();
        job.setJarByClass(AverageDriver.class);
        job.setJobName("Average Temperature");

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        job.setMapperClass(AverageMapper.class);
        job.setReducerClass(AverageReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

### Data Flow

```
K1=LongWritable, V1=Text  →  [AverageMapper]  →  K2=Text(year), V2=IntWritable(temp)
K2=Text(year), List[V2]   →  [AverageReducer] →  K3=Text(year), V3=IntWritable(avg)
```

---

## 10. Complete Word Count Program

```java
import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {
            StringTokenizer itr = new StringTokenizer(value.toString());
            while (itr.hasMoreTokens()) {
                word.set(itr.nextToken());
                context.write(word, one);
            }
        }
    }

    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");
        job.setJarByClass(WordCount.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

### Word Count — Step by Step

```
Input:
  "What do you mean by Object"
  "What do you know about Java"

RecordReader → <1, "What do you mean by Object">
               <2, "What do you know about Java">

Mapper Output:
  <What,1> <do,1> <you,1> <mean,1> <by,1> <Object,1>
  <What,1> <do,1> <you,1> <know,1> <about,1> <Java,1>

Combiner Output (local):
  <What,2> <do,2> <you,2> <mean,1> <by,1> <Object,1> <know,1> <about,1> <Java,1>

Reducer Output:
  What    2
  Java    1
  do      2
  you     2
  ...
```

---

---

# Part-A Q&A (Short Answers)

---

### Q.1 What Do You Mean by Map Task?

A **Map Task** is the first major phase in MapReduce. It:

- Reads input data as `<Key, Value>` pairs from HDFS (via RecordReader)
- Processes each pair using the user-defined `map()` function
- Emits intermediate `<Key, Value>` pairs
- One map task runs per input split (typically one HDFS block = 128 MB)

```
(K1, V1) → map() → (K2, V2)
```

Example: In Word Count, the map task reads each line and emits `<word, 1>` for every word found.

---

### Q.2 What is Reduce Task? Explain.

A **Reduce Task** is the second major phase in MapReduce. It:

- Receives sorted and grouped intermediate `<Key, List[Values]>` pairs from all mappers
- Processes each group using the user-defined `reduce()` function
- Emits final `<Key, Value>` output written to HDFS

```
(K2, List[V2]) → reduce() → (K3, V3)
```

**Steps within a reduce task:**

1. **Fetch** — copies map outputs from mapper nodes (shuffle)
2. **Sort** — merges and sorts by key
3. **Reduce** — calls `reduce()` for each unique key

Example: In Word Count, reduce task receives `<"Java", [1,1,1]>` and emits `<"Java", 3>`.

---

### Q.3 What Main Configuration Parameters Are Specified in MapReduce?

The main configuration parameters set in the Driver class:

|Parameter|Method|
|---|---|
|Mapper class|`job.setMapperClass()`|
|Reducer class|`job.setReducerClass()`|
|Combiner class|`job.setCombinerClass()`|
|Partitioner class|`job.setPartitionerClass()`|
|Map output key type|`job.setMapOutputKeyClass()`|
|Map output value type|`job.setMapOutputValueClass()`|
|Final output key type|`job.setOutputKeyClass()`|
|Final output value type|`job.setOutputValueClass()`|
|Input path|`FileInputFormat.addInputPath()`|
|Output path|`FileOutputFormat.setOutputPath()`|
|Number of reducers|`job.setNumReduceTasks()`|
|Input format|`job.setInputFormatClass()`|
|Output format|`job.setOutputFormatClass()`|

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
```

- Replaced by the `Job` class in the New API
- Allows setting all job properties: mapper, reducer, combiner, partitioner, input/output formats and paths
- `JobClient.runJob(conf)` submits the job (Old API)

In the **New API**, `Configuration` + `Job.getInstance(conf)` replaces `JobConf`.

---

### Q.5 What is a MapReduce Combiner?

A **Combiner** (semi-reducer) is an optional optimization step that runs locally on each mapper node before data is sent to reducers.

- Reduces the **volume of data** transferred over the network
- Performs the same operation as the Reducer but on local map output
- Must be **associative** and **commutative** (works for: sum, max, min — not average)
- Configured via: `job.setCombinerClass(MyReducer.class)`

**Without Combiner:** All `<word, 1>` pairs sent to reducer **With Combiner:** Pre-aggregated `<word, count>` sent → much less data

---

### Q.6 What is RecordReader in MapReduce?

**RecordReader** is the component that reads raw input data and converts it into `<Key, Value>` pairs for the Mapper.

- Part of `InputFormat`
- Default: `TextInputFormat` creates `<LongWritable (byte offset), Text (line)>` pairs
- Custom RecordReaders can parse XML, JSON, binary, or fixed-width formats
- Reads one record at a time and feeds it to the `map()` function
- The Mapper never directly accesses files — always goes through RecordReader

---

### Q.7 Define Writable Data Types in MapReduce

Writable data types are Hadoop's serializable wrappers for Java types, used as keys and values in MapReduce:

|Writable Type|Java Equivalent|Use|
|---|---|---|
|`IntWritable`|`int`|Integer counts, IDs|
|`LongWritable`|`long`|Byte offsets, large numbers|
|`FloatWritable`|`float`|Decimal numbers|
|`DoubleWritable`|`double`|High-precision decimals|
|`BooleanWritable`|`boolean`|True/False flags|
|`Text`|`String`|Words, lines, labels|
|`NullWritable`|null|Ignored key or value|
|`BytesWritable`|`byte[]`|Raw binary data|

- **Values** implement `Writable`
- **Keys** implement `WritableComparable` (adds sorting capability)

---

### Q.8 How Hadoop MapReduce Works?

```
1. Input data stored in HDFS (split into blocks)
        ↓
2. InputFormat creates InputSplits (one per mapper)
        ↓
3. RecordReader converts each split into <K,V> pairs
        ↓
4. Mapper processes each <K,V> → emits intermediate <K,V>
        ↓
5. Partitioner routes each key to a specific reducer
        ↓
6. Combiner (optional) — local aggregation on mapper node
        ↓
7. Shuffle — intermediate data copied to reducer nodes
        ↓
8. Sort — keys sorted on reducer node
        ↓
9. Reducer processes <K, List[V]> → emits final <K,V>
        ↓
10. OutputFormat writes final output to HDFS
```

Key principle: **"Move computation to data"** — Hadoop sends the program jar to the data node, not data to the program.

---

### Q.9 Explain What is Shuffling in MapReduce

**Shuffling** is the process of transferring intermediate Map output to the appropriate Reducer nodes. It happens between the Map and Reduce phases.

Steps in Shuffle:

1. Mapper writes output to local disk (not HDFS)
2. Partitioner assigns each key to a reducer
3. Framework **copies** (shuffles) map outputs to reducer nodes over the network
4. Reducer **merges and sorts** the received data by key

**Why it matters:**

- Most network-intensive phase of MapReduce
- Combiner reduces shuffle data volume
- Efficient shuffle = faster overall job

---

### Q.10 Explain What is Distributed Cache in MapReduce Framework

**Distributed Cache** is a mechanism to distribute read-only files (lookup tables, jars, archives) to all nodes in the cluster before a job runs.

**Use cases:**

- Sharing a lookup file (e.g., country codes CSV) with all mappers
- Distributing third-party JARs

**How to use (New API):**

```java
// In Driver:
job.addCacheFile(new URI("/hdfs/path/to/lookup.txt"));

// In Mapper setup():
URI[] cacheFiles = context.getCacheFiles();
```

**Benefits:**

- File is copied once per node (not per task)
- Avoids repeated HDFS reads
- Available locally to all tasks on that node

---

### Q.11 How is Identity Mapper Different from Chain Mapper?

|Feature|Identity Mapper|Chain Mapper|
|---|---|---|
|Function|Passes input directly to output unchanged|Chains multiple mappers in sequence|
|Use case|Testing, debugging, pass-through|Complex multi-step transformations|
|Class|`Mapper` (default no-op behavior)|`ChainMapper` class|
|Data flow|Input → (unchanged) → Output|Input → Mapper1 → Mapper2 → ... → Output|
|Configuration|Default; no extra setup|`ChainMapper.addMapper()` for each step|

**Identity Mapper** — output = input, used when no mapping transformation is needed.

**Chain Mapper** — multiple mapper classes applied sequentially in a single Map phase.

---

### Q.12 Explain the Core Methods of a Reducer

```java
public class MyReducer extends Reducer<KIN, VIN, KOUT, VOUT> {

    // Called once before any reduce() calls
    protected void setup(Context context) throws IOException, InterruptedException { }

    // Called once per unique key — main logic goes here
    protected void reduce(KIN key, Iterable<VIN> values, Context context)
            throws IOException, InterruptedException { }

    // Called once after all reduce() calls complete
    protected void cleanup(Context context) throws IOException, InterruptedException { }

    // Controls entire reduce execution — override for custom flow
    public void run(Context context) throws IOException, InterruptedException {
        setup(context);
        while (context.nextKey()) {
            reduce(context.getCurrentKey(), context.getValues(), context);
        }
        cleanup(context);
    }
}
```

|Method|When Called|Purpose|
|---|---|---|
|`setup()`|Once at start|Initialize resources (DB connections, file handles)|
|`reduce()`|Once per unique key|Core aggregation logic|
|`cleanup()`|Once at end|Release resources, write summary data|
|`run()`|Controls lifecycle|Override for custom execution flow|

---

### Q.13 What Role Do RecordReader, Combiner and Partitioner Play?

**RecordReader:**

- Sits between InputFormat and Mapper
- Converts raw input bytes → `<Key, Value>` pairs
- Controls how input is parsed (line-by-line, XML, JSON, binary)
- One RecordReader per InputSplit

**Combiner:**

- Sits between Mapper and Shuffle
- Performs local, partial aggregation on mapper output
- Reduces network I/O by shrinking data before transfer
- Optional — only valid for associative, commutative operations

**Partitioner:**

- Sits between Mapper and Reducer
- Decides which reducer receives which key
- Default: `HashPartitioner` (hash of key % numReducers)
- Custom: route based on key range, category, etc.
- Ensures all values for a key go to the **same** reducer

```
Mapper → [Combiner] → [Partitioner] → Shuffle → Reducer
```

---

---

# Part-B Q&A (Medium Answers)

---

### Q.14 Explain MapReduce Program with Neat Figure

A MapReduce program processes data in the following stages:

```
┌─────────────┐
│  HDFS Input │  (e.g., large text file)
└──────┬──────┘
       │ split into InputSplits
       ↓
┌─────────────────────────────────────────┐
│           MAP PHASE                     │
│  RecordReader → map() → local output   │
└──────┬──────────────────────────────────┘
       │ intermediate <K,V> pairs written to local disk
       ↓
┌─────────────────────────────────────────┐
│       COMBINER (optional)               │
│  Local aggregation on mapper node       │
└──────┬──────────────────────────────────┘
       │
       ↓
┌─────────────────────────────────────────┐
│       SHUFFLE & SORT                    │
│  Copy map outputs → Sort by key         │
└──────┬──────────────────────────────────┘
       │ grouped <K, List[V]> pairs
       ↓
┌─────────────────────────────────────────┐
│           REDUCE PHASE                  │
│  reduce() → final output                │
└──────┬──────────────────────────────────┘
       │
       ↓
┌─────────────┐
│ HDFS Output │  (part-r-00000, part-r-00001, ...)
└─────────────┘
```

**Word Count Example:**

|Phase|Input|Output|
|---|---|---|
|RecordReader|Raw file lines|`<1, "What do you mean">`|
|Mapper|`<offset, line>`|`<"What",1> <"do",1> ...`|
|Combiner|`<word, [1,1,1]>`|`<word, 3>`|
|Shuffle|Map outputs|Sorted by key|
|Reducer|`<"Java",[1,1,1]>`|`<"Java", 3>`|
|RecordWriter|`<key, value>`|`Java 3` (text file)|

---

### Q.15 Explain the Process of Analyzing Data with Hadoop

1. **Data Ingestion** — Raw data loaded into HDFS using tools like `hdfs dfs -put`, Flume, Sqoop, or Kafka
    
2. **Data Storage** — HDFS stores data in blocks (128 MB default) replicated across nodes (3x default)
    
3. **Job Configuration** — Developer writes Driver, Mapper, Reducer code and configures the Job
    
4. **Job Submission** — Driver submits job to ResourceManager (YARN)
    
5. **Task Assignment** — ResourceManager assigns Map tasks to nodes where data resides (data locality)
    
6. **Map Phase** — Each mapper processes its input split, emits `<K,V>` pairs
    
7. **Shuffle & Sort** — Framework moves map output to correct reducer nodes, sorted by key
    
8. **Reduce Phase** — Reducers aggregate grouped values, write final output
    
9. **Output** — Results stored in HDFS output directory, readable as text or binary
    
10. **Analysis** — Output read via Hive, Pig, or direct HDFS reads for reporting/visualization
    

**Key Principle:** Move computation to data, not data to computation → minimizes network traffic.

---

### Q.16 Various Differences Between Old and New Java MapReduce API

|Aspect|Old API (mapred)|New API (mapreduce)|
|---|---|---|
|Package|`org.apache.hadoop.mapred`|`org.apache.hadoop.mapreduce`|
|Base class|Interface|Abstract Class|
|Communication|`OutputCollector` + `Reporter`|Single `Context` object|
|Job submission|`JobClient.runJob(conf)`|`job.waitForCompletion(true)`|
|Job config|`JobConf`|`Configuration` + `Job`|
|Mapper values|N/A|`Iterable<V>`|
|Reducer values|`Iterator<V>`|`Iterable<V>`|
|Execution control|`MapRunnable` (mapper only)|`run()` on both mapper/reducer|
|Output naming|`part-nnnnn`|`part-m-nnnnn` / `part-r-nnnnn`|
|Availability|Hadoop ≤ 0.20|Hadoop ≥ 0.21|

> 📌 Old API still works in modern Hadoop — not deprecated, just superseded.

---

### Q.17 Explain Mapper — How It Works

**Mapper** transforms input records into intermediate key-value pairs.

**Lifecycle:**

```
setup(context)   ← called once before processing
    ↓
map(key, value, context)   ← called for each input record
    ↓
cleanup(context)   ← called once after all records processed
```

**Working:**

1. `InputFormat` splits input into `InputSplit` (one per mapper)
2. `RecordReader` converts each split into `<K,V>` pairs
3. `map()` is called once per `<K,V>` pair
4. User logic processes the value and calls `context.write(outKey, outVal)`
5. Output is buffered in memory (100 MB default), then spilled to local disk
6. Multiple spills are merged and sorted before shuffle

**Example (Word Count):**

```java
// Input: <1, "Hello World Hello">
// Output: <"Hello",1> <"World",1> <"Hello",1>
public void map(Object key, Text value, Context context) {
    StringTokenizer itr = new StringTokenizer(value.toString());
    while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, one);   // emit <word, 1>
    }
}
```

**Key points:**

- One mapper per input split (typically 1 HDFS block)
- Mappers run in parallel across the cluster
- Output is written to **local disk**, not HDFS
- `setup()` and `cleanup()` used for initialization/finalization

---

### Q.18 Define Combiner

A **Combiner** is an optional, local mini-reducer that runs on each mapper node immediately after the map phase completes, before data is shuffled to reducers.

**Purpose:** Reduce the volume of intermediate data sent over the network.

**Characteristics:**

- Also called **semi-reducer**
- Implements the same `Reducer` interface
- Operates on the local map output of a single node
- Only valid for operations that are **associative** and **commutative**

**Valid operations:** sum, max, min, count **Invalid operations:** average, median (these are not associative)

**Without Combiner:**

```
Node 1 sends: <Java,1> <Java,1> <Java,1>   → 3 records
```

**With Combiner:**

```
Node 1 sends: <Java,3>   → 1 record (combined locally)
```

**Configuration:**

```java
job.setCombinerClass(IntSumReducer.class);  // same class as reducer for sum
```

---

### Q.19 Explain How MapReduce Works Diagrammatically with Example

**Input text:**

```
What do you mean by Object
What do you know about Java
What is Java Virtual Machine
How Java enabled High Performance
```

**Complete Flow:**

```
INPUT FILE
──────────
Line 1: "What do you mean by Object"
Line 2: "What do you know about Java"
Line 3: "What is Java Virtual Machine"
Line 4: "How Java enabled High Performance"

         ↓ RecordReader
MAPPER INPUT                    MAPPER OUTPUT
<1,"What do you mean by Object"> → <What,1><do,1><you,1><mean,1><by,1><Object,1>
<2,"What do you know about Java"> → <What,1><do,1><you,1><know,1><about,1><Java,1>
<3,"What is Java Virtual Machine"> → <What,1><is,1><Java,1><Virtual,1><Machine,1>
<4,"How Java enabled...">          → <How,1><Java,1><enabled,1><High,1><Performance,1>

         ↓ Combiner (local aggregation)
<What,3><do,2><you,2><Java,3><mean,1><by,1><Object,1>
<know,1><about,1><is,1><Virtual,1><Machine,1>
<How,1><enabled,1><High,1><Performance,1>

         ↓ Shuffle & Sort (group by key)
<Java,  [3]>    (all Java counts together)
<What,  [3]>
<do,    [2]>
...

         ↓ Reducer
FINAL OUTPUT
Java         3
What         3
do           2
you          2
mean         1
by           1
Object       1
...
```

---

---

# Part-C Q&A (Long Answers)

---

### Q.20 What is Java MapReduce? Explain in Detail

**Java MapReduce** is the native programming interface for writing MapReduce programs using the Java language in the Hadoop framework.

#### Core Concept

MapReduce breaks a large problem into two functions:

- **Map:** Transform input records → intermediate key-value pairs
- **Reduce:** Aggregate intermediate pairs → final output

#### Data Flow

```
(K1,V1) → Map → (K2,V2) → Shuffle/Sort → (K2,List[V2]) → Reduce → (K3,V3)
```

#### Components

**1. Driver Class**

- Contains `main()` method
- Creates `Job` object, configures all parameters
- Submits job to cluster via `job.waitForCompletion(true)`

**2. Mapper Class**

- Extends `Mapper<KEYIN, VALUEIN, KEYOUT, VALUEOUT>`
- Overrides `map()` method
- Emits `<K2, V2>` via `context.write()`

**3. Reducer Class**

- Extends `Reducer<KEYIN, VALUEIN, KEYOUT, VALUEOUT>`
- Overrides `reduce()` method
- Receives grouped `<K2, Iterable[V2]>`, emits `<K3, V3>`

**4. InputFormat / RecordReader**

- Defines how input is split and parsed
- Default: `TextInputFormat` → `<LongWritable, Text>`

**5. OutputFormat / RecordWriter**

- Defines how output is written
- Default: `TextOutputFormat` → tab-separated text

#### Job Execution Steps

1. Client submits jar + configuration to ResourceManager
2. ResourceManager schedules map tasks on DataNodes with local data
3. Each map task processes one InputSplit
4. Map output buffered locally, spilled to disk, sorted
5. Partitioner routes keys to correct reducers
6. Combiner runs locally (if configured)
7. Shuffle: map outputs copied to reducer nodes
8. Reducer sorts, merges, runs `reduce()`, writes to HDFS

#### Advantages of Java MapReduce

- Full control over processing logic
- Direct access to Hadoop APIs
- Best performance (native JVM execution)
- Supports all Hadoop features (Counters, Distributed Cache, etc.)

#### Limitations

- Verbose — even simple jobs require multiple classes
- Steep learning curve for non-Java developers
- Alternatives: Pig (scripting), Hive (SQL-like), Spark (faster)

---

### Q.21 Explain a Weather Dataset in Detail

#### Dataset Source

NCDC (National Climatic Data Center) — collects weather data from sensors worldwide. Data available at: `https://github.com/tomwhite/hadoop-book/tree/master/input/ncdc/all`

#### Dataset Structure

- One file per year (e.g., `1901.gz`, `1902.gz`, ...)
- Each file contains millions of fixed-width records
- Each record = one sensor reading

#### Fixed-Width Record Format

```
Position  Field
0-3       STN (Station identifier)
4-8       WBAN
15-19     YEAR
87        Temperature sign (+ or -)
88-91     Temperature (tenths of degree Celsius)
92        Quality code
```

#### Sample Record

```
0057328999999193401010600004+51317+028783FM-12...+0024...
                 ^^^^                             ^^^^
                 YEAR=1934                        TEMP=+0024
```

#### Quality Codes (valid readings)

|Code|Meaning|
|---|---|
|0|Passed gross limits check|
|1|Passed all quality control checks|
|4|Passed extreme limits check|
|5|Passed all checks|
|9|Passed all checks (estimated)|

#### MapReduce Program Design for Weather Data

**Goal:** Find average temperature per year

**Map Phase:**

- Read each line
- Extract year (characters 15-19)
- Extract temperature (characters 87-92)
- Filter out missing values (9999) and bad quality codes
- Emit: `<year, temperature>`

**Reduce Phase:**

- Receive all temperatures for a year
- Compute: `sum / count`
- Emit: `<year, average_temperature>`

**Code Snippet — Mapper:**

```java
String year = line.substring(15, 19);
int temperature;
if (line.charAt(87) == '+')
    temperature = Integer.parseInt(line.substring(88, 92));
else
    temperature = Integer.parseInt(line.substring(87, 92));

String quality = line.substring(92, 93);
if (temperature != MISSING && quality.matches("[01459]"))
    context.write(new Text(year), new IntWritable(temperature));
```

**Sample Output:**

```
1901   -6
1902   3
1903   -2
1950   14
2000   21
```

#### Why This Dataset?

- Real-world semi-structured data (not perfectly clean)
- Demonstrates fixed-width parsing in `map()`
- Shows quality filtering logic
- Multi-file input (one per year) → natural parallelism
- Classic example from "Hadoop: The Definitive Guide"

---

### Q.22 Notes on: (a) Reducer (b) Partitioner

#### (a) Reducer

The **Reducer** consolidates intermediate key-value pairs produced by Mappers into final output.

**Class Declaration:**

```java
public class MyReducer extends Reducer<TEXT, IntWritable, Text, IntWritable>
```

**Four Generic Types:**

1. Input Key type (= Mapper output key type)
2. Input Value type (= Mapper output value type)
3. Output Key type
4. Output Value type

**Lifecycle Methods:**

```java
// 1. setup() — runs once before any reduce calls
protected void setup(Context context) {
    // Open database connections, load lookup files
}

// 2. reduce() — runs once per unique key
protected void reduce(Text key, Iterable<IntWritable> values, Context context) {
    int sum = 0;
    for (IntWritable val : values) sum += val.get();
    context.write(key, new IntWritable(sum));
}

// 3. cleanup() — runs once after all reduce calls
protected void cleanup(Context context) {
    // Close resources
}
```

**Number of Reducers:**

```java
job.setNumReduceTasks(3);  // default = 1
```

- More reducers → more parallelism but more overhead
- 0 reducers → no reduce phase, map output = final output

**Output:**

- Written to HDFS as `part-r-00000`, `part-r-00001`, etc.
- One output file per reducer

---

#### (b) Partitioner

The **Partitioner** determines which Reducer receives a given key-value pair after the Map phase.

**Default Partitioner — HashPartitioner:**

```java
public int getPartition(K key, V value, int numReduceTasks) {
    return (key.hashCode() & Integer.MAX_VALUE) % numReduceTasks;
}
```

**Custom Partitioner Example:**

```java
public class RangePartitioner extends Partitioner<Text, IntWritable> {
    @Override
    public int getPartition(Text key, IntWritable value, int numReduceTasks) {
        char firstChar = key.toString().charAt(0);
        if (firstChar < 'M')
            return 0 % numReduceTasks;   // Reducer 0: A-L
        else
            return 1 % numReduceTasks;   // Reducer 1: M-Z
    }
}
```

**Register:**

```java
job.setPartitionerClass(RangePartitioner.class);
job.setNumReduceTasks(2);
```

**Why Custom Partitioners?**

- Default hash may create **skewed** partitions (one reducer overloaded)
- Need to group related keys together (e.g., same region, same date range)
- Secondary sort patterns (sort by composite key)
- Ensuring sorted output across reducer files

**Key rule:** Number of partitions must equal `numReduceTasks`.

---

### Q.23 Explain the Component Driver

The **Driver** is the entry point and controller of a MapReduce job. It runs on the **client machine** (not on cluster nodes).

#### Responsibilities

1. Parse command-line arguments (input/output paths)
2. Create and configure the `Job` object
3. Set all MapReduce components (Mapper, Reducer, Combiner, Partitioner)
4. Define input/output types and formats
5. Submit the job and wait for completion
6. Report success or failure

#### Complete Driver Example (New API)

```java
public class WordCountDriver {
    public static void main(String[] args) throws Exception {

        // Step 1: Create configuration
        Configuration conf = new Configuration();

        // Step 2: Create job instance
        Job job = Job.getInstance(conf, "Word Count");

        // Step 3: Set the main jar class
        job.setJarByClass(WordCountDriver.class);

        // Step 4: Set Mapper and Reducer
        job.setMapperClass(TokenizerMapper.class);
        job.setReducerClass(IntSumReducer.class);

        // Step 5: (Optional) Set Combiner
        job.setCombinerClass(IntSumReducer.class);

        // Step 6: Set output types for Map phase
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);

        // Step 7: Set output types for Reduce phase
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        // Step 8: Set number of reducers
        job.setNumReduceTasks(1);

        // Step 9: Set input and output paths
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        // Step 10: Submit and wait
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

#### Key Methods of Job Class

|Method|Purpose|
|---|---|
|`Job.getInstance(conf, name)`|Create new job instance|
|`setJarByClass(Class)`|Locate the jar containing the class|
|`setMapperClass(Class)`|Set mapper implementation|
|`setReducerClass(Class)`|Set reducer implementation|
|`setCombinerClass(Class)`|Set combiner (optional)|
|`setOutputKeyClass(Class)`|Final output key type|
|`setOutputValueClass(Class)`|Final output value type|
|`setNumReduceTasks(int)`|Number of reducer tasks|
|`waitForCompletion(boolean)`|Submit job and block until done|

#### Hadoop Data Locality

Hadoop sends the **program jar** to the nodes where data lives (not the other way around). `setJarByClass()` tells Hadoop which jar to distribute. This avoids massive data movement across the network.

---

### Q.24 Explain RecordReader in Detail

**RecordReader** is the bridge between raw input data (files on HDFS) and the Mapper. It is responsible for reading an `InputSplit` and converting it into `<Key, Value>` pairs.

#### Position in MapReduce Pipeline

```
HDFS Block → InputFormat → InputSplit → RecordReader → <K,V> → Mapper
```

#### Default RecordReader — LineRecordReader

Used by `TextInputFormat`:

- **Key:** `LongWritable` — byte offset of the line from start of file
- **Value:** `Text` — the entire line as a string

```java
// Default behavior:
// Line: "Hello World" at byte position 42
// Key  = LongWritable(42)
// Value = Text("Hello World")
```

#### Custom RecordReader (New API)

```java
public class MyRecordReader extends RecordReader<LongWritable, Text> {
    private long start, end, pos;
    private LineReader lineReader;
    private LongWritable key = new LongWritable();
    private Text value = new Text();

    @Override
    public void initialize(InputSplit split, TaskAttemptContext context)
            throws IOException {
        FileSplit fileSplit = (FileSplit) split;
        start = fileSplit.getStart();
        end = start + fileSplit.getLength();
        Path path = fileSplit.getPath();
        FileSystem fs = path.getFileSystem(context.getConfiguration());
        FSDataInputStream in = fs.open(path);
        lineReader = new LineReader(in);
        pos = start;
    }

    @Override
    public boolean nextKeyValue() throws IOException {
        key.set(pos);
        int bytesRead = lineReader.readLine(value);
        if (bytesRead == 0) return false;
        pos += bytesRead;
        return true;
    }

    @Override
    public LongWritable getCurrentKey() { return key; }

    @Override
    public Text getCurrentValue() { return value; }

    @Override
    public float getProgress() {
        return (pos - start) / (float)(end - start);
    }

    @Override
    public void close() throws IOException { lineReader.close(); }
}
```

#### Important InputFormat Types

|InputFormat|RecordReader Output|Use Case|
|---|---|---|
|`TextInputFormat`|`<LongWritable, Text>`|Default; line-by-line text|
|`KeyValueTextInputFormat`|`<Text, Text>`|Tab-separated key-value text|
|`SequenceFileInputFormat`|`<K, V>` (binary)|Binary sequence files|
|`NLineInputFormat`|`<LongWritable, Text>`|Fixed N lines per split|
|Custom|Any `<K, V>`|XML, JSON, fixed-width, etc.|

#### Key Roles of RecordReader

1. Manages reading the assigned `InputSplit`
2. Handles split boundaries (doesn't re-read data in another split)
3. Decodes raw bytes into structured `<K,V>` pairs
4. Reports progress (`getProgress()`) to the framework
5. Each Mapper gets exactly one RecordReader

---

### Q.25 Explain MapReduce in Detail

#### Definition

MapReduce is a distributed programming model developed by Google and implemented in Hadoop for processing and generating large datasets across a cluster of commodity hardware. Every computation is expressed as two functions: **Map** and **Reduce**.

#### Core Principle

```
"Divide and Conquer at scale"
— Split big problem → many small parallel tasks → combine results
```

#### Complete Data Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                     CLIENT MACHINE                               │
│  Driver: configure Job → submit to ResourceManager               │
└──────────────────────────┬───────────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────────┐
│                     RESOURCE MANAGER (YARN)                      │
│  Schedules tasks, assigns containers on DataNodes                │
└──────────────────────────┬───────────────────────────────────────┘
                           │
     ┌─────────────────────┼──────────────────────┐
     ▼                     ▼                      ▼
┌─────────┐          ┌─────────┐           ┌─────────┐
│  NODE 1 │          │  NODE 2 │           │  NODE 3 │
│ Mapper  │          │ Mapper  │           │ Mapper  │
│ (split1)│          │ (split2)│           │ (split3)│
└────┬────┘          └────┬────┘           └────┬────┘
     │                    │                     │
     └────────────────────┼─────────────────────┘
              Shuffle & Sort (by key)
     ┌──────────────┬─────┴──────────────┐
     ▼              ▼                    ▼
┌─────────┐   ┌─────────┐         ┌─────────┐
│Reducer 0│   │Reducer 1│         │Reducer 2│
│(A-H keys│   │(I-P keys│         │(Q-Z keys│
└────┬────┘   └────┬────┘         └────┬────┘
     │              │                   │
     ▼              ▼                   ▼
  part-r-00000  part-r-00001       part-r-00002   (HDFS Output)
```

#### Phases in Detail

**Phase 1 — Input Splitting**

- HDFS file divided into `InputSplits` (one per mapper)
- Default split size = HDFS block size (128 MB)
- More splits = more parallelism

**Phase 2 — Map**

- Each mapper processes one InputSplit
- RecordReader converts raw bytes → `<K,V>` pairs
- `map()` function processes each pair, emits `<K2,V2>`
- Output buffered in memory ring buffer (100 MB)
- Buffer spills to local disk when 80% full (sorted)
- Multiple spills merged into single sorted file

**Phase 3 — Combiner (optional)**

- Runs on sorted mapper output
- Local pre-aggregation before network transfer
- Reduces shuffle data volume significantly

**Phase 4 — Shuffle**

- Framework copies map outputs to appropriate reducer nodes
- Uses HTTP for data transfer
- Partitioner determines which reducer gets which key

**Phase 5 — Sort (Merge)**

- Reducer receives multiple map outputs
- Merges them into a single sorted stream
- All values for a key grouped together

**Phase 6 — Reduce**

- `reduce()` called once per unique key
- Processes `<K2, Iterable[V2]>` → emits `<K3,V3>`
- Output written to HDFS

**Phase 7 — Output**

- RecordWriter writes each `<K,V>` to HDFS
- Default: `TextOutputFormat` (tab-separated text)
- One output file per reducer

#### MapReduce Counters

Built-in performance tracking:

```
Map-Reduce Framework
  Map input records=1000000
  Map output records=5000000
  Map output bytes=45000000
  Reduce input records=5000000
  Reduce output records=200000
```

#### Fault Tolerance

- If a Map task fails → ResourceManager reschedules it on another node
- If a Reduce task fails → same recovery
- Failed tasks retried up to 4 times (configurable)
- No data loss because input is still in HDFS

#### Limitations of MapReduce

|Limitation|Impact|
|---|---|
|High latency|Not suitable for real-time processing|
|Disk I/O heavy|Intermediate data written to disk|
|No iterative processing|ML algorithms inefficient|
|Verbose code|Simple tasks need many classes|

**Modern Alternatives:** Apache Spark (in-memory), Apache Flink (streaming) — but MapReduce remains the foundation of Hadoop's batch processing.

---

## 📎 Quick Reference Card

```
Driver        → configures and submits the job (main method)
Mapper        → reads <K1,V1>, emits <K2,V2>
Combiner      → optional local mini-reducer (reduces shuffle data)
Partitioner   → routes keys to correct reducer
Shuffle/Sort  → moves and sorts map output by key
Reducer       → reads <K2,List[V2]>, emits <K3,V3>
RecordReader  → converts raw input bytes to <K,V> pairs
RecordWriter  → writes final <K,V> to HDFS output

Old API: org.apache.hadoop.mapred   (JobConf, JobClient)
New API: org.apache.hadoop.mapreduce (Configuration, Job)

Output files:
  Map    → part-m-nnnnn
  Reduce → part-r-nnnnn
```

---

_Reference: Hadoop: The Definitive Guide — Tom White, 3rd Edition, O'Reilly_