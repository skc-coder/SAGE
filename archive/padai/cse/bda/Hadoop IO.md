## 1. Hadoop I/O Overview

> Hadoop I/O deals with how data is **read, written, serialized, and compared** across nodes in a distributed cluster.

Key concepts:

- **Writable** — interface for serialization/deserialization
- **WritableComparable** — Writable + Comparable (used for keys)
- **RawComparator** — compares keys at byte level (faster than object-level comparison)

---

## 2. Writable Interface

```java
public interface Writable {
    void write(DataOutput out);       // Serialize → write to network/disk
    void readFields(DataInput in);    // Deserialize → read from network/disk
}
```

- Every type in Hadoop **must implement** `Writable`
- Replaces Java's built-in serialization (which is too heavy)
- Values in MapReduce must implement `Writable`

### Why Writable over Java Serialization?

|Feature|Java Serialization|Hadoop Writable|
|---|---|---|
|Serialized size (int 100)|43 bytes|4 bytes|
|Speed|Slow|Fast|
|Overhead|High|Minimal|
|Shuffle/Sort support|No|Yes|

---

## 3. WritableComparable

```java
public interface WritableComparable extends Writable, Comparable {
    void write(DataOutput out);
    void readFields(DataInput in);
    int compareTo(WritableComparable o);   // Required for key comparison
}
```

- Keys in MapReduce **must implement** `WritableComparable`
- Needed for the **shuffle and sort** phase
- Without it, keys cannot be compared → sort fails

### MapReduce Data Flow

```
(K1, V1) → Map → (K2, V2)
              ↓
        Shuffle & Sort   ← WritableComparable used here
              ↓
(K2, List[V2]) → Reduce → (K3, V3)
```

---

## 4. Writable Classes

### 4.1 Primitive Writable Wrappers

|Java Type|Hadoop Writable|
|---|---|
|`int`|`IntWritable`|
|`long`|`LongWritable`|
|`float`|`FloatWritable`|
|`double`|`DoubleWritable`|
|`boolean`|`BooleanWritable`|
|`byte`|`ByteWritable`|
|`int` (variable)|`VIntWritable`|
|`long` (variable)|`VLongWritable`|

All have `get()` and `set()` methods.

---

### 4.2 Text

- Writable equivalent of `java.lang.String`
- Max size: **2 GB**
- **Mutable** (unlike Java's String)
- Stored in **UTF-8** encoding

```java
Text t = new Text("hadoop");
t.set("new value");
int len = t.getLength();
```

---

### 4.3 BytesWritable

- Wrapper for an **array of binary data**
- Useful for raw byte manipulation

---

### 4.4 NullWritable

- Represents a **null value** — reads/writes zero bytes
- Used when a key or value is not needed

```java
NullWritable nw = NullWritable.get();
```

---

### 4.5 ObjectWritable

- General-purpose wrapper for: Java primitives, String, Enum, Writable, null, arrays
- Flexible but less efficient than specific types

---

### 4.6 GenericWritable

- Similar to `ObjectWritable` but supports only a **specified set of types**
- User must subclass it and define supported types

---

### 4.7 Writable Collections

|Class|Description|
|---|---|
|`ArrayWritable`|1D array of Writables|
|`TwoDArrayWritable`|2D array of Writables|
|`MapWritable`|Key-value map (Writable → Writable)|
|`SortedMapWritable`|Sorted version of MapWritable|
|`AbstractMapWritable`|Abstract base class for map writables|

> ⚠️ Array elements must be Writable types (e.g., `IntWritable`), **not** Java primitives.

---

## 5. Custom Writable

### Creating a Custom Writable (as Value)

```java
public class AddWritable implements Writable {
    public int a;
    public int b;

    public AddWritable() {}

    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(a);
        out.writeInt(b);
    }

    @Override
    public void readFields(DataInput in) throws IOException {
        a = in.readInt();
        b = in.readInt();
    }

    @Override
    public String toString() {
        return a + ", " + b;
    }
}
```

---

### Creating a Custom WritableComparable (as Key)

```java
public class AddWritable implements WritableComparable<AddWritable> {
    public int a;
    public int b;

    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(a);
        out.writeInt(b);
    }

    @Override
    public void readFields(DataInput in) throws IOException {
        a = in.readInt();
        b = in.readInt();
    }

    @Override
    public int compareTo(AddWritable o) {
        int presentValue = this.a;
        int compareValue = o.a;
        return (presentValue < compareValue ? -1 : (presentValue == compareValue ? 0 : 1));
    }

    @Override
    public int hashCode() {
        return Integer.toBinaryString(a).hashCode() ^ Integer.toBinaryString(b).hashCode();
    }
}
```

> 🔑 Use `WritableComparable` when the custom type is a **key**. Use `Writable` when it is a **value**.

---

## 6. RawComparator

### What is it?

- Compares keys **at the byte level** — no deserialization needed
- Implemented via `WritableComparator` (which extends `RawComparator`)
- Greatly speeds up the **sort phase**

### Example: IndexPair RawComparator

```java
public class IndexPairComparator extends WritableComparator {
    protected IndexPairComparator() {
        super(IndexPair.class);
    }

    @Override
    public int compare(byte[] b1, int s1, int l1,
                       byte[] b2, int s2, int l2) {
        int i1 = readInt(b1, s1);
        int i2 = readInt(b2, s2);
        int comp = (i1 < i2) ? -1 : (i1 == i2) ? 0 : 1;
        if (comp != 0) return comp;

        int j1 = readInt(b1, s1 + 4);
        int j2 = readInt(b2, s2 + 4);
        return (j1 < j2) ? -1 : (j1 == j2) ? 0 : 1;
    }
}
```

### Registering in MR Job

```java
job.setSortComparatorClass(IndexPairComparator.class);
```

### Performance Comparison

|Implementation|Avg Time (4M rows)|
|---|---|
|Without RawComparator|60.6 seconds|
|With RawComparator|31.1 seconds|

> ~2x speedup with statistical significance (p < 0.001)

---

## 7. Custom Comparators

- Used to override default `equals()` / `hashCode()` comparison
- Useful in **GroupBy** and **CoGroup** operations in Cascading
- Implement `java.util.Comparator` and attach via `Fields.setComparator()`

```java
public class CustomTextComparator extends WritableComparator {
    private Collator collator;

    public CustomTextComparator() {
        super(Text.class);
        final Locale locale = new Locale("pl");
        collator = Collator.getInstance(locale);
    }

    @Override
    public int compare(WritableComparable a, WritableComparable b) {
        synchronized (collator) {
            return collator.compare(
                ((Text) a).toString(), ((Text) b).toString());
        }
    }
}
```

- If hash code also needs customization → implement `cascading.tuple.Hasher`

---

---

# Part-A Q&A (Short Answers)

---

### Q.1 What is Writable?

**Writable** is an interface in Hadoop that every data type must implement for **serialization and deserialization**. It acts as a wrapper around Java primitive types (e.g., `IntWritable` wraps `int`). It provides two methods:

- `write(DataOutput out)` — serialize and write data
- `readFields(DataInput in)` — deserialize and read data

---

### Q.2 What is Serialization?

**Serialization** is the process of converting structured data (objects) into a **stream of bytes** so that it can be transmitted over a network or stored on disk. In Hadoop, Writables perform serialization in a compact, efficient format — much smaller than Java's default serialization.

---

### Q.3 Define Deserialization

**Deserialization** is the reverse of serialization — converting a **byte stream back into structured data/objects**. In Hadoop, `readFields(DataInput in)` performs deserialization, reconstructing the original data from bytes received over the network or read from disk.

---

### Q.4 Write the Specification of Writable Interface

```java
public interface Writable {
    void write(DataOutput out) throws IOException;
    void readFields(DataInput in) throws IOException;
}
```

- `write()` — serializes the object and writes it to a `DataOutput` stream
- `readFields()` — deserializes data from a `DataInput` stream into the object
- Both `DataInput` and `DataOutput` are from `java.io` package
- All Hadoop value types must implement this interface

---

### Q.5 Write the Specification of WritableComparable

```java
public interface WritableComparable extends Writable, Comparable {
    void write(DataOutput out) throws IOException;
    void readFields(DataInput in) throws IOException;
    int compareTo(WritableComparable o);
}
```

- Extends both `Writable` and `java.lang.Comparable`
- The `compareTo()` method enables key comparison during shuffle and sort
- All Hadoop **key** types must implement this interface

---




---

---

# Part-B Q&A (Medium Answers)

---

### Q.10 Short Note on Hadoop I/O

Hadoop I/O refers to the complete system that handles **data storage, retrieval, serialization, compression, and comparison** in the Hadoop ecosystem.

**Key components:**

- **Writable Interface** — provides serialization/deserialization for all Hadoop data types
- **WritableComparable** — extends Writable with comparison capability for keys
- **RawComparator** — byte-level key comparison for faster sorting
- **Codecs** — compression/decompression (GZip, BZip2, Snappy, LZO)
- **Checksums** — data integrity via CRC-32 checksums in HDFS
- **Sequence Files** — binary file format for storing key-value pairs
- **MapFile** — sorted sequence file with an index for random access

Hadoop I/O is optimized for **high throughput** over low latency, making it ideal for batch processing of large datasets across a distributed cluster.

---

### Q.11 Explain: (a) LocalFileSystem (b) ChecksumFileSystem

#### (a) LocalFileSystem

- Implements the Hadoop `FileSystem` API for the **local disk**
- Used in **standalone/local mode** (no cluster needed)
- Performs client-side **CRC-32 checksums** for data integrity
- Stores checksums in hidden `.crc` files alongside data files
- Useful for **testing** MapReduce jobs locally before deploying to a cluster

```java
FileSystem fs = FileSystem.getLocal(conf);
```

#### (b) ChecksumFileSystem

- A wrapper around any `FileSystem` that adds **checksum verification**
- `LocalFileSystem` extends `ChecksumFileSystem`
- On write: computes and stores a checksum for every chunk of data
- On read: recomputes the checksum and compares — throws `ChecksumException` if mismatch
- Checksum chunk size default: **512 bytes**
- Protects against **data corruption** during storage or transfer

---

### Q.12 Explain Writable Collections

Hadoop provides collection-type Writable classes for storing groups of Writables:

#### ArrayWritable

- Stores a **1D array** of Writable objects
- Must specify element type in constructor

```java
ArrayWritable a = new ArrayWritable(IntWritable.class);
a.set(new IntWritable[]{new IntWritable(10), new IntWritable(20)});
```

#### TwoDArrayWritable

- Stores a **2D array** of Writable objects

#### MapWritable

- Implements `java.util.Map<Writable, Writable>`
- General purpose key-value store

```java
MapWritable m = new MapWritable();
m.put(new IntWritable(1), new Text("one"));
```

#### SortedMapWritable

- Extends `MapWritable` and also implements `SortedMap`
- Keys are maintained in **sorted order**

#### AbstractMapWritable

- Abstract base class for `MapWritable` and `SortedMapWritable`

> ⚠️ All collection elements must be Writable types — not raw Java types.

---

### Q.13 Explain Custom Comparator

A **custom comparator** is a user-defined class to override default comparison logic in Hadoop. By default, Hadoop uses `equals()` and `hashCode()` for comparison.

**When to use:**

- When default comparison doesn't suit your sorting/grouping logic
- For locale-specific text comparison
- For secondary sort scenarios

**How to create:**

```java
public class CustomTextComparator extends WritableComparator {
    private Collator collator;

    public CustomTextComparator() {
        super(Text.class);
        collator = Collator.getInstance(new Locale("pl"));
    }

    @Override
    public int compare(WritableComparable a, WritableComparable b) {
        return collator.compare(a.toString(), b.toString());
    }
}
```

**Register in job:**

```java
job.setSortComparatorClass(CustomTextComparator.class);
```

You can also set a **default tuple element comparator** using:

```java
FlowProps.setDefaultTupleElementComparator(properties, comparatorClass);
```

---

### Q.14 Explain Why We Don't Use Java Object Serialization

Java's built-in `ObjectInputStream`/`ObjectOutputStream` serialization is **not suitable** for Hadoop because:

1. **Excessive overhead** — Java serialization includes class metadata, object graph info, and type hierarchy, inflating data size enormously:
    
    - Java serialized `int` (value 100): **43 bytes**
    - Hadoop `IntWritable` (value 100): **4 bytes**
2. **Slow performance** — Java serialization is orders of magnitude slower due to reflection
    
3. **No streaming support** — Java serialization is not designed for streaming large datasets
    
4. **No raw comparison** — cannot compare serialized bytes directly; full deserialization required
    
5. **Shuffle/Sort incompatibility** — Hadoop's shuffle and sort phase requires custom comparators that Java serialization cannot support
    
6. **Large network overhead** — the bloated byte size would slow down data transfer between nodes significantly
    

---

### Q.15 Why Do We Need WritableComparable? / What Happens If WritableComparable Is Not Present?

**Why we need it:**

- Keys in MapReduce must be **comparable** for the shuffle and sort phase
- `WritableComparable` combines serialization (`Writable`) with comparison (`Comparable`)
- Without it, the framework cannot sort keys between Mapper and Reducer

**What happens without it:**

| Scenario                         | Without WritableComparable            |
| -------------------------------- | ------------------------------------- |
| Custom key type                  | Cannot be sorted                      |
| Shuffle phase                    | Fails or produces incorrect results   |
| Reduce input                     | Keys may be unsorted/unordered        |
| Default types (IntWritable etc.) | These already implement it — no issue |

> 📌 Values do NOT need `WritableComparable` — only keys do. Values only need `Writable`.

**Rule:** If your custom type is used as a **key** → must implement `WritableComparable`. If used as a **value** → `Writable` is sufficient.

---

# Part-C Q&A (Long Answers)

### Q.19 Compression and Codec in Hadoop

#### Why Compression?

- Reduces disk storage space
- Reduces network I/O between nodes
- Speeds up MapReduce jobs (less data to read/write)

#### Compression Codecs in Hadoop

| Codec  | Extension | Splittable | Speed     | Ratio     |
| ------ | --------- | ---------- | --------- | --------- |
| GZip   | `.gz`     | No         | Medium    | High      |
| BZip2  | `.bz2`    | Yes        | Slow      | Very High |
| LZO    | `.lzo`    | Yes*       | Fast      | Medium    |
| Snappy | `.snappy` | No         | Very Fast | Medium    |
| LZ4    | `.lz4`    | No         | Very Fast | Medium    |

> ✅ **Splittable** means HDFS can split the file for parallel processing.

#### Codec API

```java
// Compress
CompressionCodec codec = new GzipCodec();
CompressionOutputStream out = codec.createOutputStream(fileOut);

// Decompress
CompressionInputStream in = codec.createInputStream(fileIn);
```

#### Where to Apply Compression

1. **Input files** — store source data compressed
2. **MapReduce output** — compress final output
3. **Intermediate output** (between Map and Reduce):

```java
conf.setBoolean("mapreduce.map.output.compress", true);
conf.setClass("mapreduce.map.output.compress.codec",
              SnappyCodec.class, CompressionCodec.class);
```

#### Codec Selection Guide

- **Snappy/LZ4** — best for intermediate data (speed > ratio)
- **BZip2** — best for archival (ratio > speed, splittable)
- **GZip** — balanced (common for final output)

---

### Q.20 Detailed Note on Writable Wrapper Classes

Hadoop provides Writable wrappers for all Java primitives in the `org.apache.hadoop.io` package.

#### Primitive Wrappers

All have `get()` to read and `set()` to write the wrapped value.

```java
IntWritable i = new IntWritable(42);
int val = i.get();       // 42
i.set(100);

LongWritable l = new LongWritable(9999999L);
FloatWritable f = new FloatWritable(3.14f);
DoubleWritable d = new DoubleWritable(3.14159);
BooleanWritable b = new BooleanWritable(true);
```

#### VIntWritable / VLongWritable

- Variable-length encoding — smaller numbers use fewer bytes
- Efficient when values cluster around small numbers

#### Text

```java
Text t = new Text("hadoop");
t.set("new text");            // mutable!
int len = t.getLength();      // byte length
byte[] bytes = t.getBytes();
```

- UTF-8 encoding
- Max 2 GB
- `find()`, `charAt()`, `append()` methods available

#### BytesWritable

```java
BytesWritable bw = new BytesWritable(new byte[]{1, 2, 3});
byte[] data = bw.getBytes();
int len = bw.getLength();
```

#### NullWritable

```java
NullWritable nw = NullWritable.get();  // singleton
```

- Used when key or value should be ignored
- Zero bytes read/written

#### ObjectWritable

- Wraps: primitives, String, Enum, Writable, null, arrays
- Uses class name metadata → larger overhead
- Useful for polymorphic values

#### GenericWritable

- Subclass and specify supported types
- More efficient than ObjectWritable for known type sets

---

