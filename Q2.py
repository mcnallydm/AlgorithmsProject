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

def min_span_tree(alist):
    output = ""
    num_nodes = alist[0]
    # Maybe compare each list to (n-1)?
    # Maybe calculate (n(n-1))/2 and sum the lengths (length += (len(node_list)-1)/3) to see if it exceeds (n(n-1))/4?
    return output