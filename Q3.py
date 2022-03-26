import copy
from Q2 import fromFile, asciindex, find_prev

def mst_traverse(alist, startidx):
    output = ""
    num_nodes = alist[0]
    alist = alist[1]
    first_node = startidx
    #print("Starting node:", find_prev(first_node))
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
    td = 0
    current_node = previous_node
    for node in range(0, num_nodes):
        opened[node] = [find_prev(node)]
    # Find first node's shortest path
    while len(visited)!=num_nodes:
        min_dist = -1
        t = 0
        next_node = ""
        for idx in visited:
            traverse_dist = 0
            if idx!=asciindex(current_node):
                traverse_dist += find_min_path(opened, asciindex(current_node))[3][idx]
            for dist_idx in range(2, len(alist[idx])-1, 3):    # Goes by every 3 elements, because that's the clear cost
                td = alist[idx][dist_idx] + traverse_dist
                if find_prev(idx)==current_node:
                    td -= traverse_dist
                if (td<min_dist or min_dist<0) and check_visited[asciindex(alist[idx][dist_idx-1])]!=1:   # Makes sure it hasn't been visited before
                    min_dist = td
                    t = alist[idx][dist_idx+1]
                    next_node = alist[idx][dist_idx-1]
                    previous_node = find_prev(idx)
        current_node = next_node
        for i in range(1, len(alist[asciindex(previous_node)]), 3):
            if alist[asciindex(previous_node)][i]==current_node:
                alist[asciindex(previous_node)][i+1] = t
        for i in range(1, len(alist[asciindex(current_node)]), 3):
            if alist[asciindex(current_node)][i]==previous_node:
                alist[asciindex(current_node)][i+1] = t
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
    #print("Total Distance:", total_dist)
    return [total_dist, output]

def find_min_path(alist, start):
    num_nodes = len(alist)
    visited = [start]    # List of indexes of visited nodes
    to_visited = [0] * num_nodes
    inout = [0] * num_nodes
    to_visited[start] = 0
    check_visited = [0] * num_nodes   # Binary hash map of nodes using the ascii values
    check_visited[start] = 1
    for idx in range(0, num_nodes):
        # Dijkstra's
        # Cycle through all branches to find that point
        for nodeidx in range(idx, len(visited)):
            node = visited[nodeidx]
            for connected in range(1, len(alist[node]), 3):   # Gets connected node letter
                if check_visited[asciindex(alist[node][connected])]!=1 and (to_visited[asciindex(alist[node][connected])]==0 or to_visited[asciindex(alist[node][connected])]>to_visited[node]+alist[node][connected+1] or inout[asciindex(alist[node][connected])]>inout[node]+alist[node][connected+1]+alist[node][connected+2]):
                    to_visited[asciindex(alist[node][connected])] = to_visited[node] + alist[node][connected+1]
                    inout[asciindex(alist[node][connected])] = inout[node] + alist[node][connected+1] + alist[node][connected+2]
                    visited.append(asciindex(alist[node][connected]))
                    check_visited[asciindex(alist[node][connected])] = 1
    total = max(inout)
    furthest = inout.index(total)
    return [start, furthest, total, to_visited]

def mst3(file):
    alist = fromFile(file)
    endpoints = find_ends(alist[1])
    start1 = mst_traverse(copy.deepcopy(alist), endpoints[0])
    start2 = mst_traverse(copy.deepcopy(alist), endpoints[1])
    if start1[0]>start2[0]:
        return start2[1]
    else:
        return start1[1]

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