from SortHouses import *
from Q1A_Sorted import *
from Q1A_Unsorted import *
from Q1B_Sorted import *
from Q1B_Unsorted import *
from Q2 import *
from Q3 import *

def avg_dist(list_houses, station):
    avgd = 0
    for idx in range(0, len(list_houses)):
        avgd += abs(list_houses[idx][0]-station[0]) + abs(list_houses[idx][1]-station[1])
    avgd = avgd/len(list_houses)
    return avgd

test_arr = [
    [2, 3],
    [1, 7],
    [9, 1],
    [5, 5],
    [5, 4],
    [5, 5],
    [2, 2]
]

ex1 = [
    [2, 4],
    [5, 2],
    [4, 1],
    [5, 6],
    [1, 6],
    [8, 7],
    [7, 3]
]

ex2 = [
    [10, 8],
    [3, 3],
    [5, 5],
    [1, 5],
    [1, 7],
    [6, 6],
    [1, 1],
    [4, 1],
    [8, 4],
    [6, 2],
    [9, 4],
    [1, 3]
]

ex3 = [
    [5, 2],
    [8, 4],
    [3, 4],
    [4, 4],
    [7, 2],
    [1, 3],
    [5, 8],
    [4, 2],
    [6, 1],
    [2, 6]
]

print(min_avg(ex1), avg_dist(ex1, min_avg(ex1)))
print(sorted_min_avg(ex1), avg_dist(ex1, sorted_min_avg(ex1)))
#print(range_avg(ex1), avg_dist(ex1, range_avg(ex1)))
print("------------------------------------------")

print(min_avg(ex2), avg_dist(ex2, min_avg(ex2)))
print(sorted_min_avg(ex2), avg_dist(ex2, sorted_min_avg(ex2)))
#print(range_avg(ex2), avg_dist(ex2, range_avg(ex2)))
print("------------------------------------------")

print(min_avg(ex3), avg_dist(ex3, min_avg(ex3)))
print(sorted_min_avg(ex3), avg_dist(ex3, sorted_min_avg(ex3)))
#print(range_avg(ex3), avg_dist(ex3, range_avg(ex3)))
print("------------------------------------------")

print(min_avg(test_arr), avg_dist(test_arr, min_avg(test_arr)))
print(sorted_min_avg(test_arr), avg_dist(test_arr, sorted_min_avg(test_arr)))