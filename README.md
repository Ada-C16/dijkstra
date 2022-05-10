# Dijkstra's Algorithm

 Dijkstra's algorithm for finding the shortest path from a start node to all other nodes in a graph.

## Description

Given an adjacency matrix representation of the graph and the node to start the algorithm from, find the shortest path from a start node to all other nodes in the graph. 

### Example 1

Input:
    adjacency_matrix =[ 
      [0, 4, 0, 0],
      [4, 0, 12, 0],
      [0, 12, 0, 0],
      [0,  0, 0, 0]
    ]
Output:
    {
        "start_node": 3, 
        "parent_list": [None, None, None, None], 
        "shortest_distances": [float('inf'), float('inf'), float('inf'), 0]
    }

## Note

The unit tests provided don't cover all test cases needed to verify correctness.
