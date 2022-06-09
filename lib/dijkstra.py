
from cmath import inf


def dijkstra(adjacency_matrix, start_node):
    shortest_distances = [float('inf')] * len(adjacency_matrix)
    parents = [None] * len(adjacency_matrix)
    visited = set()
    shortest_distances[start_node] = 0

    for j in range(len(adjacency_matrix) - 1):
        minimum_distance = float('inf')
        selected_node = None
        for i in range(len(shortest_distances)):
            if shortest_distances[i] < minimum_distance and i not in visited:
                minimum_distance = shortest_distances[i]
                selected_node = i
        
        if selected_node == None:
            break
        visited.add(selected_node)

        for i in range(len(adjacency_matrix)):
            neighbor_distance = adjacency_matrix[selected_node][i]
            if (neighbor_distance != 0) and (neighbor_distance + shortest_distances[selected_node] < shortest_distances[i]):
                shortest_distances[i] = neighbor_distance + shortest_distances[selected_node]
                parents[i] = selected_node

    return {
        "start_node": start_node, 
        "parent_list": parents, 
        "shortest_distances": shortest_distances
    }


