# TODO: Figure out how the input is given
from Q2 import fromFile, asciindex, find_prev
import sys

def find_leaves(alist):
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
    # Find first node's shortest path
    while len(visited)!=num_nodes:
        min_dist = -1
        next_node = ""
        for idx in visited:
            for dist_idx in range(2, len(alist[idx])-1, 3):    # Goes by every 3 elements, because that's the clear cost
                if (alist[idx][dist_idx]<min_dist or min_dist<0) and check_visited[asciindex(alist[idx][dist_idx-1])]!=1:   # Makes sure it hasn't been visited before
                    min_dist = alist[idx][dist_idx]
                    next_node = alist[idx][dist_idx-1]
                    previous_node = find_prev(idx)
        check_visited[asciindex(next_node)] = 1
        visited.append(asciindex(next_node))
        output += previous_node + next_node + "\n"
        total_dist += min_dist
    print("Total Distance:", total_dist)
    return output

'''datafile = sys.argv[1]
print(mst_traverse(datafile))'''