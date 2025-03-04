Cosmos Db (DocumentDb)

-> Diff editions
   - NoSQL (SQL) (default)
   - MongoDb 
   - Azure Cosmos DB for Table
   - Azure Cosmos DB for Apache Gremlin (graphs with billions of vertices and edge)
   - Azure Cosmos DB for Apache Cassandra (Key/Value)
   - Azure Cosmos DB for PostgreSQL (
   
-> Full indexing

-> Geo replication

Consistency levels:
  Strong
  Bounded staleness
  Session
  Consistent prefix
  Eventual

Partition


---------------------------
   Cosmos
             (javascript)
        stored procedure
             SP (across partitions)
        triggers (*) (inside partition)
        user-defined functions


