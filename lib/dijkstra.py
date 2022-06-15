def dijkstra(adjacency_matrix, start_node):
    parent_list = [None]*len(adjacency_matrix)
    shortest_distances = [float('inf')]*len(adjacency_matrix)

    traversal_queue = [start_node]
    visited_nodes = set()
    shortest_distances[start_node] = 0

    while traversal_queue:
        current_node = traversal_queue.pop(0) 
        
        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)

        for node, cost in enumerate(adjacency_matrix[current_node]): 
            if cost != 0:
                traversal_queue.append(node)

                current_distance = cost + shortest_distances[current_node] 
                if shortest_distances[node] == float('inf') or shortest_distances[node] > current_distance:
                    parent_list[node] = current_node 
                    shortest_distances[node] = current_distance

    return {"start_node": start_node, "parent_list": parent_list, "shortest_distances": shortest_distances}