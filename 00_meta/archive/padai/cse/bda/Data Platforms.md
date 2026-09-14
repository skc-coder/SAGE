**1. Apache Hadoop**

- Architecture: HDFS + MapReduce + YARN
- Strength: mature, fault-tolerant, large ecosystem
- Weakness: high latency batch only; complex setup
- Use case: large-scale batch ETL, data warehouse

**2. Apache Spark**

- Architecture: In-memory RDD/DataFrame processing
- Strength: 10-100x faster than Hadoop MapReduce
- Supports: batch, streaming, ML (MLlib), graph (GraphX)
- Languages: Java, Scala, Python, R
- Use case: machine learning, iterative analytics, real-time

**3. Apache Kafka**

- Architecture: distributed log-based messaging
- Strength: 1M+ messages/second per broker; persistent logs
- Use case: real-time data pipelines, event sourcing

**4. Apache Flink**

- Architecture: true streaming (event-time processing)
- Strength: lowest latency; exactly-once semantics
- Use case: complex event processing, fraud detection

**5. Apache Storm**

- Architecture: distributed real-time computation
- Strength: simple streaming topology model
- Use case: real-time analytics, online ML

**6. Cassandra**

- Architecture: masterless distributed NoSQL
- Strength: no single point of failure; linear scale
- Use case: write-heavy workloads (IoT, time-series)

**7. MongoDB**

- Architecture: document-oriented NoSQL
- Strength: flexible JSON schema; rich query language
- Use case: content management, catalogs, user data

**8. Amazon EMR / Azure HDInsight / Google Dataproc**

- Managed cloud Hadoop/Spark clusters
- Auto-scaling; pay-per-use
- Eliminates infrastructure management

**1. HDFS (Hadoop Distributed File System)**

- Distributed across commodity hardware
- Default block size: 128 MB
- Replication: 3 copies
- Best for: large sequential reads, batch analytics

**2. NoSQL Databases**

- HBase (column-family), Cassandra (wide-column), MongoDB (document)
- Schema-less, horizontally scalable
- Best for: random read/write, real-time access

**3. Object Storage (Cloud)**

- S3, Azure Blob, Google Cloud Storage
- Virtually unlimited capacity
- Pay-per-use pricing
- Best for: data lakes, archival

**4. In-Memory Stores**

- Redis, Memcached, Apache Ignite
- Microsecond latency
- Best for: caching, session management, real-time analytics