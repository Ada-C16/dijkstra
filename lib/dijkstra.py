
def dijkstra(adjacency_matrix, start_node):

    number_of_nodes = len(adjacency_matrix[0])
    parent_node = None 
    q = [(start_node, 0, parent_node)]
    visited = []
    parent_list = [None] * number_of_nodes
    shortest_distances = [float('inf')] * number_of_nodes

    while q:
        q.sort(key= lambda node: node[1])
        closest_node = q.pop(0)
        node = closest_node[0]
        distance = closest_node[1]
        parent_node = closest_node[2]
        visited.append(node)
        if distance < shortest_distances[node]:
            shortest_distances[node] = distance
            parent_list[node] = parent_node
        for other_node in range(number_of_nodes):
            if other_node not in visited:
                curr_distance = adjacency_matrix[node][other_node]
                if curr_distance > 0:
                    q.append((other_node, distance + curr_distance, node))

    return {
        "start_node": start_node,
        "parent_list": parent_list,
        "shortest_distances": shortest_distances
    }