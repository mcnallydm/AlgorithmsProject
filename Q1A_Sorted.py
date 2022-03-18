'''
- Minimize average distance to all houses
- Distance calculated using Manhattan method D = |x1-x2| + |y1-y2|
- Input as array of x-values and array of y-values

- Median of x-values = police-x
- Median of y-values = police-y


Sorting helps find median
'''
from math import trunc
from SortHouses import bubble

def sorted_min_avg(house_list):
    sortedx = bubble(house_list, 0)
    sortedy = bubble(house_list, 1)
    #if len(sortedx)%2==1:
    x = sortedx[trunc(len(sortedx)/2)][0]
    y = sortedy[trunc(len(sortedy)/2)][1]
    if len(house_list)%2==0:
        x += sortedx[(trunc(len(sortedx)/2)-1)][0]
        x = x/2
        y += sortedy[(trunc(len(sortedy)/2)-1)][1]
        y = y/2
    return [x, y]

'''
def range_avg(house_list):
    sortedx = bubble(house_list, 0)
    sortedy = bubble(house_list, 1)
    x = sortedx[0][0] + (sortedx[len(sortedx)-1][0]-sortedx[0][0])/2
    y = sortedy[0][1] + (sortedy[len(sortedy)-1][1]-sortedy[0][1])/2
    return [x, y]

def avg_avg(house_list):
    x = 0
    y = 0
    for idx in range(0, len(house_list)):
        x += house_list[idx][0]
        y += house_list[idx][1]
    x = x/len(house_list)
    y = y/len(house_list)
    return [x, y]
'''