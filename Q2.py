# TODO: Figure out how the input is given
'''
- Input from text file?
- Formatted exactly as given
- Output should be piped into an output file

- Number of edges in complete graph is (n(n-1))/2
- If it's more than 1/2 of that number, use a matrix
- Otherwise use a list
'''
'''
You are given a mountain area with a number of N villages present. A number of roads crisscross the area connecting the various villages
(directly or indirectly, meaning that the connection might pass through a third village). A snowstorm however has blocked all the roads
and the villages are now disconnected from each other. Your goal is to reconnect all the villages with the smallest cost possible,
when you are given the cost of opening a road that correct two villages.

Your input will be a graph (you may use either adjacency matrix or adjacency list representation at your discretion), where each road
between villages will be assigned a cost (to open the selected road). Note that the connection between two villages might pass through
other villages. Your algorithm should determine which roads to clear.

Give an efficient algorithm (10%): note you can map this problem to a well-known problem we have studied in class, and then state its
complexity (5%). Then code it (20%); which includes giving at least 2 appropriate test cases in your report.
'''
def fromString(str):
    str = str.split("\n")
    read = []
    num_nodes = int(str[0])
    read.append(num_nodes)
    adj_list = []
    for line in range(1, len(str)):
        current_line = str[line]
        current_line = current_line.split(" ")
        for element in range(1, len(current_line)):
                if element%3!=1:
                    current_line[element] = int(current_line[element])
        adj_list.append(current_line)
    read.append(adj_list)
    return read

def fromFile(file):
    num_nodes = 0
    adj_list = []
    read = []
    data = open(file)
    current_line = data.readline()
    current_line = current_line.strip()
    num_nodes = int(current_line)
    read.append(num_nodes)  # Adds the number of nodes
    while(1):
        current_line = data.readline()
        if not current_line:
            break
        else:
            current_line = current_line.strip()
            current_line = current_line.split(" ")
            for element in range(1, len(current_line)):
                if element%3!=1:
                    current_line[element] = int(current_line[element])
            adj_list.append(current_line)
    read.append(adj_list)
    return(read)

def asciindex(str):
    idx = 0
    if ord(str)<=90:
        idx = ord(str)-39
    else:
        idx = ord(str)-97
    return idx

def find_prev(asc):
    if asc>25:
        asc += 39
    else:
        asc += 97
    return chr(asc)

'''def next_path(alist, visited, check_visited):
    min_dist = alist[2]
    next_node = alist[1]
    for idx in visited:
        for dist_idx in range(2, len(alist[idx])-1, 3):    # Goes by every 3 elements, because that's the clear cost
            if alist[dist_idx]<min_dist and check_visited[asciindex(alist[idx][dist_idx-1])]!=1:   # Makes sure it hasn't been visited before
                min_dist = alist[idx][dist_idx]
                next_node = alist[idx][dist_idx-1]
                find_prev(idx)
    check_visited[asciindex(next_node)] = 1
    visited.append(asciindex(next_node))'''

def min_span_tree(file):
    output = ""
    alist = fromFile(file)
    num_nodes = alist[0]
    alist = alist[1]
    visited = [0]    # List of indexes of visited nodes
    check_visited = [0] * num_nodes   # Binary hash map of nodes using the ascii values
    check_visited[0] = 1
    min_dist = -1
    next_node = ""
    previous_node = 'a'
    total_dist = 0
    # Find first node's shortest path
    '''for dist_idx in range(2, len(alist[first_node])-1, 3):    # Goes by every 3 elements, because that's the clear cost
        if alist[dist_idx]<min_dist and check_visited[asciindex(alist[dist_idx-1])]!=1:   # Makes sure it hasn't been visited before
            min_dist = alist[dist_idx]
            next_node = alist[dist_idx-1]
    check_visited[asciindex(next_node)] = 1
    visited.append(asciindex(next_node))'''
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
        '''print("Check visited value: ", check_visited[asciindex(alist[idx][dist_idx-1])])
        print(visited)
        print(check_visited)'''
<<<<<<< HEAD
        print(total_dist)
=======
    print("Total Distance:", total_dist)
>>>>>>> f316d8557f41072cb0037ce041eb3b2ff74b5633
    return output
