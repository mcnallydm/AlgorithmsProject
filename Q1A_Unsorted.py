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

def push(heap, item):
    return heap

def pop(heap):
    return heap

def min_avg(house_list):
    x = 0
    y = 0
    heapx = [0] * len(house_list)
    heapy = [0] * len(house_list)
    for idx in range(0, len(house_list)):   # add to heap
        x += house_list[idx][0]
        y += house_list[idx][1]
    for loops in range(0, trunc(len(house_list)/2)):  # remove up to median
        heapx = pop(heapx)
        heapy = pop(heapy)
    x = heapx[0]
    y = heapy[0]
    return [x, y]
