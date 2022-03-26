import copy
from Q2 import fromFile, asciindex, find_prev
import sys

def mst_traverse(alist, startidx):
    output = ""
    num_nodes = alist[0]
    alist = alist[1]
    first_node = startidx
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
                #print("Distance from", current_node, "to", find_prev(idx), "through opened roads:", traverse_dist)
            for dist_idx in range(2, len(alist[idx])-1, 3):    # Goes by every 3 elements, because that's the clear cost
                td = alist[idx][dist_idx] + traverse_dist
                #print("start", alist[idx][dist_idx-1], "end", current_node)
                if find_prev(idx)==current_node:
                    td -= traverse_dist
                #print("Cost from", current_node, "to", find_prev(idx), "to", alist[idx][dist_idx-1], "is:", td)
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
        '''print(alist[asciindex(previous_node)])
        print(alist[asciindex(current_node)])'''
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
        #print(total_dist)
    print("Total Distance:", total_dist)
    return [total_dist, output]

def find_min_path(alist, start):
    #print("Shortest path from:", find_prev(start))
    #print(alist)
    # Cycle through all children to find the endpoint
    #furthest = -1
    #total = -1
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
            #print(alist[node])
            for connected in range(1, len(alist[node]), 3):   # Gets connected node letter
                if check_visited[asciindex(alist[node][connected])]!=1 and (to_visited[asciindex(alist[node][connected])]==0 or to_visited[asciindex(alist[node][connected])]>to_visited[node]+alist[node][connected+1] or inout[asciindex(alist[node][connected])]>inout[node]+alist[node][connected+1]+alist[node][connected+2]):
                    to_visited[asciindex(alist[node][connected])] = to_visited[node] + alist[node][connected+1]
                    inout[asciindex(alist[node][connected])] = inout[node] + alist[node][connected+1] + alist[node][connected+2]
                    #print("Distance from",find_prev(start), "to", find_prev(node), "to", alist[node][connected], "is:", to_visited[node], "+", alist[node][connected+1], "=", to_visited[asciindex(alist[node][connected])])
                    visited.append(asciindex(alist[node][connected]))
                    check_visited[asciindex(alist[node][connected])] = 1
                    '''if furthest==-1 or to_visited[asciindex(alist[node][connected])]>total:
                        furthest = asciindex(alist[node][connected])
                        total = to_visited[asciindex(alist[node][connected])]'''
    total = max(inout)
    furthest = inout.index(total)
    #print(find_prev(start), find_prev(furthest), total, to_visited)
    return [start, furthest, total, to_visited]
    #return [start, furthest, total]

def mst3(file):
    alist = fromFile(file)
    endpoints = find_ends(alist[1])
    #return mst_traverse(alist, find_start(alist[1], endpoints[0], endpoints[1]))[1]
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
    #print(start_idx, end_idx)
    return [start_idx, end_idx]

'''def find_start(alist, end1, end2):
    # Sums the effort to clear and traverse a path and returns the index of the node with the highest minimum
    min_in_out1 = -1
    min_in_out2 = -1
    start_idx = end1
    end_idx = end2
    for dist_idx in range(2, len(alist[end1])-1, 3):
        if (alist[end1][dist_idx]+alist[end1][dist_idx+1])<min_in_out1 or min_in_out1<0:
            min_in_out1 = alist[end1][dist_idx]+alist[end1][dist_idx+1]    # Calculates the minimum clear/traverse total to/from that node
    for dist_idx in range(2, len(alist[end2])-1, 3):
        if (alist[end2][dist_idx]+alist[end2][dist_idx+1])<min_in_out2 or min_in_out2<0:
            min_in_out2 = alist[end2][dist_idx]+alist[end2][dist_idx+1]    # Calculates the minimum clear/traverse total to/from that node
    if min_in_out2>min_in_out1:
        temp = start_idx
        start_idx = end_idx
        end_idx = temp
    return start_idx'''