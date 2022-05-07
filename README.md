# Dijkstra's Algorithm

 Dijkstra's algorithm for finding the shortest path from a start node to all other nodes in a graph.

## Description

Given an adjacency matrix representation of the graph and the node to start the algorithm from, find the shortest path from a start node to all other nodes in the graph. 

### Example 1

```
Input: 
    adjacency_matrix =[ 
      [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
      [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
      [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
      [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
      [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
      [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
      [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
      [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
      [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] 
    ]
    start_node = 0

Output:
    {
        "start_node": 0, 
        "parent_list": [None, 0, 1, 2, 5, 6, 7, 0, 2], 
        "shortest_distances": [0, 4, 12, 19, 21, 11, 9, 8, 14]
    }
```

## Note

More tests beyond what is provided are needed to verify correctness.
