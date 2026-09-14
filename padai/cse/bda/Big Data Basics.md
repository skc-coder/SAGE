## 1 to 4 basic [[java]]
## 5. Introduction to Big Data

> **Big Data** refers to extremely large datasets that cannot be processed, stored, or analyzed using traditional data management tools due to their volume, velocity, and variety.

### What is Big Data?

- Data sets that exceed the capacity of conventional database systems
- Generated from: social media, sensors, machines, transactions, web logs
- Requires specialized tools like **Hadoop**, **Spark**, **NoSQL** databases

### Web Data

- Data generated through internet activities: browsing, clicking, searching, social interactions
- Sources: web logs, cookies, social media posts, e-commerce transactions
- Characteristics: high volume, continuous stream, semi-structured or unstructured

### How Big Data Adds Value to Business

1. **Better decision making** — data-driven insights replace guesswork
2. **Customer personalization** — understand behavior patterns
3. **Risk management** — fraud detection, credit scoring
4. **Operational efficiency** — optimize supply chains, reduce waste
5. **New revenue streams** — monetize data insights
6. **Competitive advantage** — faster adaptation to market changes
7. **Predictive analytics** — forecast trends and demand

---

## 6. Characteristics of Big Data (5 Vs)

> The **5 Vs** define the core challenges and properties of Big Data.
### Volume

- Enormous quantities of data (terabytes → petabytes → exabytes)
- Facebook generates 4 petabytes/day
- Requires distributed storage (HDFS) not single-server databases

### Velocity

- Speed at which data is generated and must be processed
- **Batch processing** — collect then process (Hadoop MapReduce)
- **Real-time/Stream processing** — process as it arrives (Apache Storm, Spark Streaming)
- Stock market: millions of trades per second

### Variety

- Multiple formats and types of data:
    - **Structured** — SQL databases, spreadsheets (20% of all data)
    - **Semi-structured** — XML, JSON, log files
    - **Unstructured** — images, video, audio, social media posts (80% of all data)

### Veracity

- Trustworthiness and accuracy of data
- Noisy data, inconsistent data, missing values
- Must filter unreliable sources before analysis

### Value

- The business insight derived from the data
- Raw data alone has no value — analysis creates value
- ROI from Big Data investment

---

## 7. Types and Sources of Big Data

### Types of Data

**1. Structured Data**

- Organized in rows and columns (relational format)
- Stored in RDBMS (MySQL, Oracle, SQL Server)
- Easy to query with SQL
- Examples: bank transactions, HR records, inventory

**2. Semi-structured Data**

- Has some organizational structure but not rigid schema
- Self-describing format
- Examples: XML files, JSON files, CSV files, log files, email headers

**3. Unstructured Data**

- No predefined format or schema
- Cannot be stored in traditional relational databases
- Makes up ~80% of all enterprise data
- Examples: social media posts, images, videos, audio, PDFs, Word documents

### Sources of Big Data

| Source         | Examples                                                 |
| -------------- | -------------------------------------------------------- |
| Social Media   | Facebook posts, tweets, Instagram photos, YouTube videos |
| Machine/Sensor | IoT devices, GPS, smart meters, RFID tags                |
| Web            | Server logs, clickstream, search queries, cookies        |
| Transactional  | E-commerce, banking, POS systems                         |
| Mobile         | App usage, location data, call records                   |
| Healthcare     | EHR records, medical images, genomic data                |
| Enterprise     | CRM, ERP, emails, documents                              |

### Sources of Unstructured Data

- Text documents (emails, chat logs, articles)
- Images and photographs
- Audio recordings
- Video files
- Social media content
- Sensor readings
- Satellite imagery
- Scientific data

---

## 8. Big Data Platforms

### What is a Big Data Platform?

A **Big Data Platform** is an integrated set of technologies, tools, and services that enables storage, processing, and analysis of massive datasets.

### Features of a Big Data Platform

1. **Scalability** — horizontal scaling (add more nodes)
2. **Fault tolerance** — continue operating despite hardware failures
3. **High availability** — minimal downtime
4. **Distributed processing** — parallel computation across nodes
5. **Support for multiple data types** — structured, semi-structured, unstructured
6. **Real-time and batch processing** — flexible processing models
7. **Security** — authentication, authorization, encryption
8. **Cost-effectiveness** — commodity hardware

### Major Big Data Platforms

**1. Apache Hadoop**

- Open-source distributed storage and processing
- HDFS + MapReduce
- Best for: batch processing of large files
- Strengths: fault tolerance, scalability, cost

**2. Apache Spark**

- In-memory distributed processing
- 10-100x faster than MapReduce for iterative jobs
- Supports: batch, streaming, ML, graph processing
- Languages: Java, Scala, Python, R

**3. Apache Kafka**

- Distributed event streaming platform
- Real-time data pipeline
- High throughput, low latency
- Used by: LinkedIn, Netflix, Uber

**4. Apache HBase**

- NoSQL database on top of HDFS
- Column-oriented store
- Random read/write access to large tables
- Inspired by Google's Bigtable

**5. Apache Hive**

- SQL-like interface to Hadoop (HiveQL)
- Translates SQL queries to MapReduce jobs
- Best for data warehouse/analytics use cases

**6. Apache Pig**

- High-level scripting language (Pig Latin)
- Abstracts MapReduce complexity
- Good for ETL pipelines

**7. MongoDB**

- Document-oriented NoSQL database
- Stores JSON-like documents
- Flexible schema

**8. Cassandra**

- Wide-column NoSQL database
- Masterless architecture
- High availability, no single point of failure
- Used by: Instagram, Netflix

---

## 9. Big Data Analytics

### What is Big Data Analytics?

The process of examining large and varied datasets to uncover hidden patterns, correlations, market trends, and other useful business information.

### Why is Big Data Analytics Important?

1. **Competitive advantage** — faster, better-informed decisions
2. **Cost reduction** — identify inefficiencies
3. **New product development** — understand customer needs
4. **Risk management** — predictive fraud detection
5. **Revenue optimization** — targeted marketing, dynamic pricing

### Best Practices of Big Data Analytics

1. Define clear business objectives before collecting data
2. Ensure data quality and governance
3. Use the right tools for the right job
4. Build scalable, reusable data pipelines
5. Combine real-time and batch analytics
6. Secure sensitive data
7. Establish data lineage and provenance
8. Iterate — start small, scale up
9. Involve domain experts alongside data scientists
10. Measure ROI continuously

### Types of Big Data Analytics

|Type|Description|Example|
|---|---|---|
|**Descriptive**|What happened?|Sales reports, dashboards|
|**Diagnostic**|Why did it happen?|Root cause analysis|
|**Predictive**|What will happen?|Churn prediction, demand forecast|
|**Prescriptive**|What should we do?|Recommendation engines|

### Applications of Big Data Analytics

1. **Healthcare** — disease prediction, drug discovery, patient monitoring
2. **Finance** — fraud detection, algorithmic trading, risk assessment
3. **Retail** — personalized recommendations, inventory optimization
4. **Manufacturing** — predictive maintenance, quality control
5. **Transportation** — route optimization, traffic prediction
6. **Telecom** — network optimization, customer churn prediction
7. **Government** — public safety, tax fraud detection
8. **Entertainment** — content recommendation (Netflix, Spotify)
9. **Agriculture** — crop yield prediction, precision farming
10. **Smart Cities** — energy management, traffic control

### Challenges of Big Data Analytics

1. **Data volume** — storing and processing petabytes
2. **Data velocity** — real-time processing requirements
3. **Data variety** — integrating diverse formats
4. **Data veracity** — ensuring data quality and accuracy
5. **Privacy and security** — protecting sensitive data
6. **Talent gap** — shortage of skilled data scientists
7. **Infrastructure cost** — hardware and software investment
8. **Data integration** — combining siloed data sources
9. **Governance and compliance** — GDPR, HIPAA regulations
10. **Latency** — reducing time from data to insight

---

# Part-A Q&A (Short Answers)

---

### Q.1 What Do You Mean by Web Data?

**Web data** is data generated through internet activities and interactions:

- Web server logs (page visits, click patterns, timestamps)
- Social media posts, likes, shares, comments
- Search engine queries
- E-commerce transactions and browsing history
- Cookie data and session information
- RSS feeds and web scraping output

Web data is typically **semi-structured or unstructured**, generated continuously at high velocity. It is one of the largest sources of Big Data today.

---

### Q.2 How Big Data Add Value to Business?

1. **Customer understanding** — analyze buying patterns, preferences, behavior
2. **Personalization** — tailored recommendations (Amazon, Netflix)
3. **Fraud detection** — real-time pattern detection in financial transactions
4. **Operational efficiency** — optimize logistics, reduce waste, predict maintenance
5. **Risk management** — credit scoring, insurance underwriting
6. **New revenue streams** — sell data insights, create data-driven products
7. **Better forecasting** — demand prediction, inventory management
8. **Competitive intelligence** — monitor market trends faster than competitors

---

### Q.3 Why is Big Data Analytics Important?

1. **Data explosion** — 2.5 quintillion bytes created daily; traditional tools cannot handle it
2. **Business intelligence** — convert raw data into actionable decisions
3. **Competitive advantage** — companies using data analytics outperform peers
4. **Cost savings** — identify inefficiencies worth billions
5. **Innovation** — discover patterns humans cannot see manually
6. **Personalization at scale** — serve millions of unique customer experiences
7. **Predictive power** — anticipate problems before they occur

---

### Q.4 What Are the Sources of Unstructured Data in Big Data?

1. **Social media** — Facebook posts, tweets, Instagram photos, YouTube videos
2. **Emails** — body text, attachments
3. **Documents** — PDFs, Word files, presentations
4. **Images** — digital photos, medical scans, satellite imagery
5. **Audio** — call center recordings, podcasts, music
6. **Video** — surveillance footage, user-generated content
7. **Sensor data** — IoT readings, GPS trails
8. **Web pages** — HTML content, blog posts

Unstructured data accounts for approximately **80% of all enterprise data**.

---

### Q.5 What is HDFS?

**HDFS (Hadoop Distributed File System)** is a distributed, fault-tolerant file system designed to store very large files across clusters of commodity hardware.

Key features:

- Written in **Java**, runs in **user space**
- Files split into **blocks** (default 64–128 MB)
- Each block **replicated 3 times** by default
- **NameNode** stores metadata; **DataNodes** store actual blocks
- Optimized for **large sequential reads** (batch processing)
- Not suitable for low-latency random access

---


### Q.7 List Out the Best Practices of Big Data Analytics

1. Define clear business goals before starting
2. Ensure data quality — garbage in, garbage out
3. Start small, prove value, then scale
4. Choose the right tool for each job (Hadoop for batch, Kafka for streaming)
5. Secure data throughout its lifecycle
6. Build repeatable, automated data pipelines
7. Involve domain experts in interpretation
8. Establish data governance and ownership
9. Monitor and measure ROI continuously
10. Combine historical and real-time analytics

---

### Q.8 Write Down the Characteristics of Big Data Applications

1. **Data volume** — process TB to PB of data
2. **Distributed processing** — run across hundreds/thousands of nodes
3. **Fault tolerance** — continue despite node failures
4. **Horizontal scalability** — add nodes to increase capacity
5. **Real-time capability** — process streaming data with low latency
6. **Schema flexibility** — handle structured and unstructured data
7. **Cost efficiency** — run on commodity hardware
8. **Batch and stream support** — flexible processing models
9. **Data locality** — move computation to data
10. **High throughput** — process millions of records per second

---

### Q.9 Write Down the Four Computing Resources of Big Data Storage

1. **RAM** — fastest; used for in-memory processing (Spark); volatile
2. **Local disk (HDD/SSD)** — persistent, cost-effective; used by DataNodes
3. **Distributed file system (HDFS)** — scales across cluster; fault-tolerant via replication
4. **Cloud/Object storage (S3, Azure Blob)** — virtually unlimited; pay-per-use; for data lakes

---

### 
---

### Q.11 How Can You Restart NameNode and All the Daemons in Hadoop?

```bash
# Restart NameNode only:
hadoop-daemon.sh stop namenode
hadoop-daemon.sh start namenode

# Restart all daemons:
stop-all.sh
start-all.sh

# Or separately:
stop-dfs.sh  && start-dfs.sh    # HDFS daemons
stop-yarn.sh && start-yarn.sh   # YARN daemons
```

---



# Part-B Q&A (Medium Answers)

### Q.18 Explain Nature of Data and Its Properties

**Nature of Data in Big Data:**

Data is characterized by:

- **Origin** — machine-generated vs human-generated
- **Format** — binary, text, multimedia
- **Structure** — structured, semi-structured, unstructured
- **Temporal nature** — historical vs real-time vs streaming

**Properties of Data:**

|Property|Description|
|---|---|
|**Volume**|Amount/size of data|
|**Velocity**|Rate of data generation|
|**Variety**|Diversity of formats|
|**Veracity**|Accuracy and reliability|
|**Volatility**|How long data remains relevant|
|**Validity**|Correctness for intended purpose|
|**Visualization**|How data can be displayed meaningfully|

**Data Quality Properties:**

- **Accuracy** — free from errors
- **Completeness** — all required fields present
- **Consistency** — same data across systems
- **Timeliness** — data is up-to-date
- **Uniqueness** — no duplicate records
- **Integrity** — referential consistency maintained

---
### Q.20 What Are the Various Sources of Big Data?

**1. Social Media** Facebook (4 PB/day), Twitter (500M tweets/day), Instagram, YouTube

**2. Machine/Sensor Data** IoT devices, smart meters, industrial sensors, RFID, GPS trackers

**3. Web and Internet** Server logs, clickstreams, search queries, web scraping, cookies

**4. Transactional Systems** E-commerce orders, banking transactions, POS systems, airline reservations

**5. Mobile Devices** App usage data, call detail records, location data, accelerometer readings

**6. Healthcare** Electronic health records, medical imaging, genomic sequences, clinical trials

**7. Scientific Research** Telescope data, particle accelerators, climate sensors, genome sequencing

**8. Enterprise Systems** CRM, ERP, emails, documents, collaboration tools

**9. Government** Census data, tax records, traffic sensors, surveillance

**10. Financial Markets** Stock ticks, options data, news feeds, economic indicators

---

### Q.22 Explain the Role of a JobTracker

The **JobTracker** is the master daemon for MapReduce job management in Hadoop (old API).

**Functions:**

1. **Job receipt** — accepts job submissions from clients
2. **Data locality** — queries NameNode to find data locations; assigns tasks to closest nodes
3. **Task assignment** — assigns Map and Reduce tasks to TaskTrackers
4. **Progress monitoring** — receives heartbeats and task progress from TaskTrackers
5. **Fault recovery** — detects failed TaskTrackers; reassigns their tasks to other nodes
6. **Load balancing** — distributes tasks evenly using available slot counts

**Data Locality Priority:**

1. Same DataNode (ideal — data is local)
2. Same rack (one network hop)
3. Different rack (two network hops — last resort)

**Replaced by:** YARN ResourceManager in Hadoop 2.x

---

# Part-C Q&A (Long Answers)

---

### Q.27 Explain the Various Big [[Data Platforms]]

### Q.31 Challenges of Big Data Analytics in Detail

**1. Volume — Storage and Processing Scale**

- Petabyte-scale datasets overwhelm traditional systems
- Solution: HDFS, cloud object storage, columnar formats (Parquet/ORC)

**2. Velocity — Real-time Processing**

- Data arrives faster than batch systems can process
- Solution: Apache Kafka + Spark Streaming; Flink

**3. Variety — Data Integration**

- Combining structured DB data with unstructured text/images
- Solution: Data lakes (HDFS/S3); schema-on-read; ETL pipelines

**4. Veracity — Data Quality**

- Noisy, incomplete, inconsistent data produces wrong insights
- Solution: Data cleansing, validation rules, master data management

**5. Privacy and Security**

- GDPR, HIPAA require strict data protection
- Anonymization/pseudonymization required
- Solution: Ranger, Kerberos, encryption

**6. Talent Gap**

- Shortage of data engineers, data scientists, ML engineers
- Solution: Training programs; AutoML tools; managed platforms

**7. Infrastructure Cost**

- Hardware, software licensing, power, cooling
- Solution: Cloud (AWS/Azure/GCP) reduces CapEx to OpEx

**8. Data Silos**

- Data trapped in departmental systems that don't communicate
- Solution: Enterprise data lakes; API integrations; master data management

**9. Regulatory Compliance**

- Data residency laws, right to erasure (GDPR Article 17)
- Solution: Data governance tools, audit trails, access controls

**10. Latency and Performance**

- Users expect results in seconds; data is in petabytes
- Solution: Caching (Redis), indexing (Elasticsearch), in-memory computing (Spark)

---

