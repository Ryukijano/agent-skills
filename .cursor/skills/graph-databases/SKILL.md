# Graph Databases and Knowledge Graphs for ML

## Description

Property graph models, Cypher/Gremlin querying, graph embeddings, GNNs on graph DBs, and knowledge graph completion for connected data.

## When to use

Your data is naturally connected (knowledge, supply chains, social/transactional networks) and you need traversal, reasoning, or graph ML.

## Key concepts

- **Property graph model**: nodes and edges with labels and key-value properties.
- **Cypher / Gremlin**: declarative and traversal graph query languages.
- **Knowledge graphs (KGs)**: semantic triples and ontologies for reasoning.
- **Graph databases**: Neo4j, TigerGraph, Amazon Neptune, ArangoDB, JanusGraph.
- **GNNs on graph DBs**: train graph neural networks by sampling from a graph DB query engine.

## Code pattern

```python
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

with driver.session() as session:
    session.run("""
        CREATE (a:Asset {id: $id})
        CREATE (s:Sensor {name: 'temp'})
        CREATE (a)-[:HAS_SENSOR]->(s)
    """, id="pump-01")

    result = session.run("""
        MATCH (a:Asset {id: 'pump-01'})-[:HAS_SENSOR]->(s:Sensor)
        RETURN s.name AS sensor
    """)
    for record in result:
        print(record["sensor"])
```

## Tuning notes

- Design the graph schema around query patterns, not just the source schema.
- Use indexes and constraints on high-cardinality properties.
- For GNN training, use graph DB sampling to avoid materializing the entire graph in memory.
- Choose between property graphs and RDF/KGs based on reasoning and inference needs.

## Verification

1. Model a small domain as a property graph and run multi-hop Cypher queries.
2. Train a GNN by sampling from a graph DB and evaluate node classification accuracy.
3. Perform knowledge graph completion and check hits@10 on a held-out test set.

## References

- https://arxiv.org/abs/2209.09732
- https://arxiv.org/abs/2411.11375
- https://arxiv.org/abs/2511.11399
- https://arxiv.org/abs/2504.05478
- https://arxiv.org/abs/2607.09666
