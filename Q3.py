# TODO: Figure out how the input is given
from Q2 import *

def find_start(alist):
    # Sums the effort to clear and traverse a path and returns the index of the node with the highest minimum
    highest_min_out = 0
    min_in_out = -1
    start_idx = -1
    for idx in range(0, len(alist)):
        for dist_idx in range(2, len(alist[idx])-1, 3):
            if (alist[idx][dist_idx]+alist[idx][dist_idx+1])<min_in_out or min_in_out<0:
                min_in_out = alist[idx][dist_idx]+alist[idx][dist_idx+1]    # Calculates the minimum clear/traverse total
        if min_in_out>highest_min_out:
            highest_min_out = min_in_out    # Finds the max min clear/traverse
            start_idx = idx
        min_in_out = -1
    return start_idx

def mst_traverse(file):
    output = ""
    alist = fromFile(file)
    num_nodes = alist[0]
    alist = alist[1]
    first_node = find_start(alist)
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