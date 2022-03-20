from SortHouses import *
from Q1A_Sorted import *
from Q1A_Unsorted import *
from Q1B_Sorted import *
from Q1B_Unsorted import *
from Q2 import *
from Q3 import *

def dist(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])

def avg_dist(list_houses, station):
    avgd = 0
    for idx in range(0, len(list_houses)):
        avgd += dist(list_houses[idx], station)
    avgd = avgd/len(list_houses)
    return avgd

def max_dist(list_houses, station):
    maxd = 0
    for coord in list_houses:
            if dist(coord, station)>maxd:
                maxd = dist(coord, station)
    return maxd

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

'''def pushtest():
    heapx = []
    for idx in range(0, len(ex1)):   # add to heap
        heapx = heapush(heapx, ex1[idx][0])
        #print(heapx)'''


'''#print(avg_avg(ex1), avg_dist(ex1, avg_avg(ex1)), max_dist(ex1, avg_avg(ex1)))
print(min_avg(ex1), avg_dist(ex1, min_avg(ex1)), max_dist(ex1, min_avg(ex1)))
print(sorted_min_avg(ex1), avg_dist(ex1, sorted_min_avg(ex1)), max_dist(ex1, sorted_min_avg(ex1)))
#print(range_avg(ex1), avg_dist(ex1, range_avg(ex1)), max_dist(ex1, range_avg(ex1)))
print("------------------------------------------")

#print(avg_avg(ex2), avg_dist(ex2, avg_avg(ex2)), max_dist(ex2, avg_avg(ex2)))
print(min_avg(ex2), avg_dist(ex2, min_avg(ex2)), max_dist(ex2, min_avg(ex2)))
print(sorted_min_avg(ex2), avg_dist(ex2, sorted_min_avg(ex2)), max_dist(ex2, sorted_min_avg(ex2)))
#print(range_avg(ex2), avg_dist(ex2, range_avg(ex2)), max_dist(ex2, range_avg(ex2)))
print("------------------------------------------")

#print(avg_avg(ex3), avg_dist(ex3, avg_avg(ex3)), max_dist(ex3, avg_avg(ex3)))
print(min_avg(ex3), avg_dist(ex3, min_avg(ex3)), max_dist(ex3, min_avg(ex3)))
print(sorted_min_avg(ex3), avg_dist(ex3, sorted_min_avg(ex3)), max_dist(ex3, sorted_min_avg(ex3)))
#print(range_avg(ex3), avg_dist(ex3, range_avg(ex3)), max_dist(ex3, range_avg(ex3)))
print("------------------------------------------")

#print(avg_avg(test_arr), avg_dist(test_arr, avg_avg(test_arr)), max_dist(test_arr, avg_avg(test_arr)))
print(min_avg(test_arr), avg_dist(test_arr, min_avg(test_arr)), max_dist(test_arr, min_avg(test_arr)))
print(sorted_min_avg(test_arr), avg_dist(test_arr, sorted_min_avg(test_arr)), max_dist(test_arr, sorted_min_avg(test_arr)))
#print(range_avg(test_arr), avg_dist(test_arr, range_avg(test_arr)), max_dist(test_arr, range_avg(test_arr)))'''


#pushtest()
str = "10\na b 6 0 c 3 0 e 9 0\nb a 6 0 c 4 0 d 2 0 g 9 0\nc a 3 0 b 4 0 d 2 0 e 9 0 f 9 0\nd b 2 0 c 2 0 f 8 0 g 9 0\ne a 9 0 c 9 0 f 8 0 j 18 0\nf c 9 0 d 8 0 e 8 0 g 7 0 i 9 0 j 10 0\ng b 9 0 d 9 0 f 7 0 h 4 0 i 5 0\nh g 4 0 i 1 0 j 4 0\ni f 9 0 g 5 0 h 1 0 j 3 0\nj e 18 0 f 10 0 h 4 0 i 3 0"

'''print(fromFile("Q2Test1.txt"))
print(fromString(str))
print(fromFile("Q2Test1.txt")==fromString(str))'''

#print(fromFile("Example.txt"))
print(min_span_tree("Example.txt"))
print("------------------------------------------")
print(min_span_tree("Q2Test1.txt"))