Hive uses a **Metastore** (e.g., Apache Derby, MySQL, PostgreSQL) for metadata.
Why not HDFS?
- HDFS lacks **ACID**, **transactional**, and **fast read/write** support for small files
- Metadata must be **fast, consistent, and reliable** — HDFS can’t provide that

- Stores:
    - Table names
    - Column definitions
    - Data types
    - File locations (HDFS paths)
    - Partition info
    - Table properties
- Accessed via **Hive Driver** → **Metastore Service** → **Database**