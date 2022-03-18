'''
- Minimize average distance to all houses
- Distance calculated using Manhattan method D = |x1-x2| + |y1-y2|
- Input as array of x-values and array of y-values

- Median of x-values = police-x
- Median of y-values = police-y
- Sorting doesn't matter

Sorting helps determine how many are to the left and right of the avg point
Find the median
*/
'''

from math import trunc

def heapush(heap, child):
    heap.append(child)  # Adds new number to heap
    idx = len(heap)-1   # Gets last index of heap
    parent_idx = (idx)//2 # Finds parent index
    #print(parent_idx)
    parent = heap[parent_idx]
    while (child<parent):
        temp = child
        heap[idx] = parent
        heap[parent_idx] = temp # Swaps child & parent
        idx = parent_idx    # Sets child idx to the idx it just moved to
        parent_idx = (idx)//2 # Finds new parent index
        parent = heap[parent_idx]   # Sets parent to the value of the new parent index
    #print(heap)
    return heap

def heapop(heap):
    idx = 0
    heap[0] = heap[len(heap)-1]
    parent = heap[0]
    heap.pop()
    left = heap[1]
    child_idx = 1
    smallest = left
    if (child_idx+1)<=len(heap)-1:
        right = heap[2]
        if right<left:
            smallest = right
            child_idx += 1
    while parent>smallest:
        temp = parent
        heap[idx] = smallest
        heap[child_idx] = temp  # Swaps parent and child
        idx = child_idx
        if ((idx*2)+1)<=len(heap)-1:
            child_idx = (idx*2)+1
            left = heap[child_idx]
            smallest = left
            if (child_idx+1)<=len(heap)-1:
                right = heap[child_idx+1]
                if right<left:
                    smallest = right
                    child_idx += 1
        else:
            break
    #print(heap)
    return heap

def min_avg(house_list):
    x = 0
    y = 0
    heapx = []
    heapy = []
    for idx in range(0, len(house_list)):   # add to heap
        heapx = heapush(heapx, house_list[idx][0])
        heapy = heapush(heapy, house_list[idx][1])
    for loops in range(0, trunc(len(house_list)/2)-1):  # remove up to median
        heapx = heapop(heapx)
        heapy = heapop(heapy)
    if len(house_list)%2==0:
        x = heapx[0]
        y = heapy[0]
    heapx = heapop(heapx)
    heapy = heapop(heapy)
    x += heapx[0]
    y += heapy[0]
    if len(house_list)%2==0:
        x /= 2
        y /= 2
    return [x, y]
