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

def min_avg(house_list):
    x = 0
    y = 0
    for idx in range(0, len(house_list)):
        x += house_list[idx][0]
        y += house_list[idx][1]
    x = x/len(house_list)
    y = y/len(house_list)
    return [x, y]
