def dijkstra(adjacency_matrix, start_node):
    parent_list = [None]*len(adjacency_matrix)
    shortest_distances = [float('inf')]*len(adjacency_matrix)

    traversal_queue = [start_node]
    visited_nodes = set()
    shortest_distances[start_node] = 0

    while traversal_queue:
        current_node = traversal_queue.pop(0) 

        # check if we looked at this node's adjacency list yet, if we have, skip
        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)

        # iterate through the current nodes adjacency matrix
        for node, cost in enumerate(adjacency_matrix[current_node]): 
            # if there is a relationship to another node, add it to queue
            if cost != 0:
                traversal_queue.append(node)

                # calculate the distance from current node to each additional connection
                # if the distance is less than shortest distance to that node already, or 
                # there is no recorded distance to that node, update distance list, and parent list
                current_distance = cost + shortest_distances[current_node] 
                if shortest_distances[node] == float('inf') or shortest_distances[node] > current_distance:
                    parent_list[node] = current_node 
                    shortest_distances[node] = current_distance

    return {"start_node": start_node, "parent_list": parent_list, "shortest_distances": shortest_distances}