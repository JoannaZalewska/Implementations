from math import inf
from heapq import heappop, heappush

graph = { 'A': [('C', 3), ('F', 2)],
          'B': [('D', 1), ('E', 2), ('F', 6), ('G', 2)],
          'C': [('A', 3), ('D', 4), ('E', 1), ('F', 2)],
          'D': [('B', 1), ('C', 4)],
          'E': [('B', 2), ('C', 1), ('F', 3)],
          'F': [('A', 2), ('C', 2), ('E', 3), ('B', 6), ('G', 5)],
          'G': [('B', 2), ('F', 5)]
        }

graph2 = { 'A': [('B', 1), ('G', 7)],
          'B': [('C', 1)],
          'C': [('D', 1)],
          'D': [('E', 2)],
          'E': [('F', 10)],
          'F': [],
          'G': [('F', 3)]
        }


def find_the_shortest_way(graph, start, end):
    """
    Finds the shortest way between to nodes in the graph using Dijkstra's algorithm.
    We assume that a start and end exists in the given graph.
    :param graph:  A dictionary where keys are strings with nodes names and values are lists containing tuples with two elements.
                   First element is a node that is a neighbour of the node being the key and the second element is a distance between those nodes.
    :param start:  String with a name of the start node.
    :param end:    String with a name of the end node.
    :return path   Tuple with two elements: list containing nodes that create path and the length of the path.
    """

    explored = set() # This is a set with nodes in which we've already been. We start from the start node so initialy this node is in this set.
                          # We've already beed in the node if we've found the shortest way to this node.

    # Dictionary where our node names are keys and the values are distances from the start node.
    # Initialy every node, except for start node, has value infinity. Start node has value 0.
    distance = {node : inf for node in graph.keys()}
    distance[start] = 0

    # Dictionary where our node names are keys and the values are names of nodes from where we arrive to the node being the key.
    # Initialy every node has value None.
    previous = {node : None for node in graph.keys()}

    priority_queue = []
    current_node = (0, start) # The node in which we are right now with it's distance from the start.

    while True:
        if len(priority_queue) != 0:
            current_node = heappop(priority_queue)
        current_node_name = current_node[1]
        current_node_distance = distance[current_node_name]
        explored.add(current_node_name)

        if current_node_name == end:
            return current_node_distance, previous
        next_nodes = set(current_node_name)
        for next_node in graph[current_node_name]:
            distance_between_nodes = next_node[1]
            next_node_name = next_node[0]
            next_node_distance = current_node_distance + distance_between_nodes

            if next_node_name not in explored:
                if distance[next_node_name] > next_node_distance:
                    distance[next_node_name] = next_node_distance
                    previous[next_node_name] = current_node_name
                heappush(priority_queue, (distance[next_node_name], next_node_name))

def get_path(previous, start, end):
    path = []
    current_node = end
    while True:
        path.append(current_node)
        if current_node == start:
            path.reverse()
            return path
        next_node = previous[current_node]
        current_node = next_node

path, previous = find_the_shortest_way(graph, 'A', 'B')
print(path)
print(previous)
print(get_path(previous, 'A', 'B'))

path2, previous2 = find_the_shortest_way(graph, 'G', 'A')
print(path2)
print(previous2)
print(get_path(previous2, 'G', 'A'))

path3, previous3 = find_the_shortest_way(graph2, 'A', 'F')
print(path3)
print(previous3)
print(get_path(previous3, 'A', 'F'))



