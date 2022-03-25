# TODO: Figure out how the input is given
from Q2 import fromFile, asciindex, find_prev
import sys

'''
Idea 1:
    Check list of unvisited nodes
    Calculate the distance to each node from everywhere along current path
    Take smallest

Idea 2:
    Brute force it
    Take all the paths of length n-1 that go through all nodes
    Find the shortest

Idea 3:
    Find the 2 nodes that have the longest shortest distance between them?
    They are the start & end?
'''

'''def find_leaves(alist):
    leaf1 = -1  # Index of Leaf with the highest cost
    leaf1_cost = -1
    leaf2 = -1  # Index of Leaf with the second highest cost
    leaf2_cost = -1
    for idx in range(0, len(alist)):
        if (len(idx)==4):   # [node, connection, clear, traverse] -> length is 4
            if leaf1==-1 or idx[3]+idx[4]>leaf1_cost:
                leaf2 = leaf1
                leaf2_cost = leaf1_cost
                leaf1 = idx
                leaf1_cost = idx[3]+idx[4]
            elif leaf2==-1 or idx[3]+idx[4]>leaf2_cost:
                leaf2 = idx
                leaf2_cost = idx[3]+idx[4]
    return [leaf1, leaf2]

def find_ends(alist):
    # Sums the effort to clear and traverse a path and returns the index of the node with the highest minimum
    highest_min_out = 0
    high_min_out2 = 0
    min_in_out = -1
    leaf1 = -1  # Index of Leaf with the highest cost
    leaf1_cost = -1
    leaf2 = -1  # Index of Leaf with the second highest cost
    leaf2_cost = -1
    start_idx = -1
    end_idx = -1
    for idx in range(0, len(alist)):
        for dist_idx in range(2, len(alist[idx])-1, 3):
            if (alist[idx][dist_idx]+alist[idx][dist_idx+1])<min_in_out or min_in_out<0:
                min_in_out = alist[idx][dist_idx]+alist[idx][dist_idx+1]    # Calculates the minimum clear/traverse total to/from that node
        if min_in_out>highest_min_out:
            highest_min_out = min_in_out    # Finds the max min clear/traverse of the whole graph
            start_idx = idx
        min_in_out = -1
    return [start_idx, end_idx]'''

def find_ends(alist):
    start_idx = 0
    end_idx = 0
    total = 0
    min_path = []
    for node_idx in range(0, len(alist)):
        min_path = find_min_path(alist, node_idx)
        if min_path[2]>total:
            start_idx = min_path[0]
            end_idx = min_path[1]
            total = min_path[2]
    return [start_idx, end_idx]

def mst_traverse(file):
    output = ""
    alist = fromFile(file)
    num_nodes = alist[0]
    alist = alist[1]
    first_node = find_ends(alist)[0]
    last_node = find_ends(alist)[1]
    print("Starting node:", find_prev(first_node))
    visited = [first_node]    # List of indexes of visited nodes
    check_visited = [0] * num_nodes   # Binary hash map of nodes using the ascii values
    check_visited[first_node] = 1
    min_dist = -1
    next_node = ""
    previous_node = find_prev(first_node)
    total_dist = 0
    traverse_dist = 0
    opened = [[]] * num_nodes
    t = 0
    current_node = previous_node
    for node in range(0, len(alist)):
        opened[node] = [find_prev(node)]
    # Find first node's shortest path
    while len(visited)!=num_nodes:
        min_dist = -1
        t = 0
        traverse_dist = 0
        next_node = ""
        for idx in visited:
            if idx!=current_node:
                print(idx, find_prev(idx))
                traverse_dist += find_min_path(opened, asciindex(current_node))[3][idx]
            for dist_idx in range(2, len(alist[idx])-1, 3):    # Goes by every 3 elements, because that's the clear cost
                traverse_dist += alist[idx][dist_idx]
                print(traverse_dist)
                if (traverse_dist<min_dist or min_dist<0) and check_visited[asciindex(alist[idx][dist_idx-1])]!=1:   # Makes sure it hasn't been visited before
                    min_dist = alist[idx][dist_idx]
                    t = alist[idx][dist_idx+1]
                    next_node = alist[idx][dist_idx-1]
                    previous_node = find_prev(idx)
        current_node = next_node
        opened[asciindex(previous_node)].append(next_node)
        opened[asciindex(previous_node)].append(t)
        opened[asciindex(previous_node)].append(t)
        opened[asciindex(next_node)].append(previous_node)
        opened[asciindex(next_node)].append(t)
        opened[asciindex(next_node)].append(t)
        check_visited[asciindex(next_node)] = 1
        visited.append(asciindex(next_node))
        output += previous_node + next_node + "\n"
        total_dist += min_dist
        print(opened)
    print("Total Distance:", total_dist)
    return output

def find_min_path(alist, start):
    #print(alist)
    # Cycle through all children to find the endpoint
    #furthest = -1
    #total = -1
    num_nodes = len(alist)
    visited = [start]    # List of indexes of visited nodes
    to_visited = [0] * num_nodes
    to_visited[start] = 0
    check_visited = [0] * num_nodes   # Binary hash map of nodes using the ascii values
    check_visited[start] = 1
    for idx in range(0, num_nodes):
        # Dijkstra's
        # Cycle through all branches to find that point
        for nodeidx in range(idx, len(visited)):
            node = visited[nodeidx]
            #print(alist[node])
            for connected in range(1, len(alist[node]), 3):   # Gets connected node letter
                if check_visited[asciindex(alist[node][connected])]!=1 or (to_visited[asciindex(alist[node][connected])]==0 or to_visited[asciindex(alist[node][connected])]>to_visited[node]+alist[node][connected+1]):
                    to_visited[asciindex(alist[node][connected])] = to_visited[node]+alist[node][connected+1]
                    #print("Distance from",find_prev(start), "to", find_prev(node), "to", alist[node][connected], "is:", to_visited[node], "+", alist[node][connected+1], "=", to_visited[asciindex(alist[node][connected])])
                    visited.append(asciindex(alist[node][connected]))
                    check_visited[asciindex(alist[node][connected])] = 1
                    '''if furthest==-1 or to_visited[asciindex(alist[node][connected])]>total:
                        furthest = asciindex(alist[node][connected])
                        total = to_visited[asciindex(alist[node][connected])]'''
    total = max(to_visited)
    furthest = to_visited.index(total)
    print(find_prev(start), find_prev(furthest), total, to_visited)
    return [start, furthest, total, to_visited]
    #return [start, furthest, total]

'''def find_path(alist, start_idx):
    all_paths = []  # Format [dist, []]
    path = []
    total_dist = 0
    num_nodes = len(alist)
    visited = [0]    # List of indexes of visited nodes
    check_visited = [0] * num_nodes   # Binary hash map of nodes using the ascii values
    check_visited[0] = 1
    max_cleared = num_nodes-1
    opened = []  # List of cleared roads, elements: [start, end, traversal_cost]
    current_node = start_idx
    while len(visited)!=num_nodes:
        min_dist = -1
        next_node = ""
        for idx in visited:
            #print("idx: ", idx)
            for dist_idx in range(2, len(alist[idx])-1, 3):    # Goes by every 3 elements, because that's the clear cost
                if (alist[idx][dist_idx]<min_dist or min_dist<0) and check_visited[asciindex(alist[idx][dist_idx-1])]!=1:   # Makes sure it hasn't been visited before
                    min_dist = alist[idx][dist_idx]
                    next_node = alist[idx][dist_idx-1]
                    previous_node = find_prev(idx)
                    #print(asciindex(alist[idx][dist_idx-1]))
        total_dist += min_dist
        check_visited[asciindex(next_node)] = 1
        visited.append(asciindex(next_node))
        output += previous_node + next_node + "\n"
        total_dist += min_dist
    return path'''