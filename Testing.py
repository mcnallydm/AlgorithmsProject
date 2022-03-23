import random
from SortHouses import *
from Q1A_Sorted import *
from Q1A_Unsorted import *
from Q1B_Sorted import *
from Q1B_Unsorted import *
from Q2 import *
from Q3 import *

def generate_coords():
    coords = []
    num_nodes = random.randint(1, 200)
    x = 0
    y = 0
    oddx = random.randint(0, 1)
    oddy = random.randint(0, 1)
    for idx in range(0, num_nodes):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        if oddx==1:
            x *= -1
        if oddy==1:
            y *= -1
        oddx = random.randint(0, 1)
        oddy = random.randint(0, 1)
        coords.append([x,y])
    return coords

def print_coords(coords):
    for house in coords:
        print(house)

def max_dist(list_houses, station):
    maxd = 0
    for coord in list_houses:
            if dist(coord, station)>maxd:
                maxd = dist(coord, station)
    return maxd

def avg_dist(list_houses, station):
    avgd = 0
    for idx in range(0, len(list_houses)):
        avgd += dist(list_houses[idx], station)
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

ex4 = [
    [-1, 2],
    [2, 3],
    [4, 2],
    [1, 1],
    [1, -2],
    [0, -3],
    [4, -1],
    [2, -2]
]

ex5 = [
    [-2, 0],    # -2, -2
    [-2, 3],    # 1, -5 MINDIFF
    [-2, -3],   # -5, 1 MINSUM
    [-1, 1],    # 0, -2
    [-1, -1],   # -2, 0
    [-1, -2],   # -3, 1
    [1, 1],     # 2, 0  MAXSUM
    [2, -2]     # 0, 4  MAXDIFF
]

'''tests = [
    test_arr,
    ex1,
    ex2,
    ex3,
    ex4,
    ex5
]'''

def add_test(coords, testno):
    to_add = "ex" + str(testno) + " = [\n" + str(coords[0])
    # Remove last comma and replace with newline
    for house in range(1, len(coords)):
        to_add += ",\n" + str(coords[house])
    to_add += "\n]\n"
    print(to_add)
    return to_add


def get_tests(file):
    first = 1
    tests = []
    current_test = []
    data = open(file)
    x = 0
    y = 0
    current_line = data.readline()
    current_line = data.readline()
    temp = ""
    while(1):
        current_line = data.readline()
        x = 0
        y = 0
        temp = ""
        #current_line = data.readline()
        #current_line = data.readline()
        #print(current_line)
        if not current_line:
            tests.append(current_test)
            break
        else:
            current_line = current_line.strip()
            #print(len(current_line))
            if len(current_line)>1 and (current_line[1]=="[" or current_line[1]=="e"):
                current_line = current_line[1:len(current_line)-1:2]
            else:
                current_line = current_line[0:len(current_line)]
            #print(current_line)
            #print(len(current_line))
            '''if len(current_line)!=1 and current_line[1]!="e" and current_line[1]!="]":
                xidx = 3
                yidx = 9
                if current_line[xidx]=="-":
                    xidx += 2
                    yidx +=2
                if current_line[yidx]=="-":
                    yidx +=2
                x = int(current_line[xidx])
                y = int(current_line[yidx])
                current_test.append([x, y])'''
            
            if len(current_line)>0 and current_line[0]=="[":
                for ch in current_line:
                    if ch!="[" and ch!="]" and ch!=",":
                        temp += ch
                current_line = temp
                current_line = current_line.split(" ")
                #print(current_line)
                x = int(current_line[0])
                y = int(current_line[1])
                current_test.append([x, y])
                #print(current_test)
            elif len(current_line)>1 and current_line[0]=="e":
                tests.append(current_test)
                current_test = []
    return tests

def new_test(file, num_new):
    tests = get_tests(file)
    #print(tests)
    for i in range(0, num_new):
        tests.append(generate_coords())
    #print(tests)
    for idx in range(0, len(tests)):
        #print(tests[idx])
        add_test(tests[idx], idx)

def get_mmd(house_list):
    minsum = ""     # Bottom left
    mindiff = ""    # Top left
    maxsum = ""     # Top right
    maxdiff = ""    # Bottom Right
    for house in house_list:    # O(n)
        sumxy = house[0]+house[1]
        diffxy = house[0]-house[1]
        if minsum=="" or sumxy<minsum:
            minsum = sumxy
        if maxsum=="" or sumxy>maxsum:
            maxsum = sumxy
        if mindiff=="" or diffxy<mindiff:
            mindiff = diffxy
        if maxdiff=="" or diffxy>maxdiff:
            maxdiff = diffxy
    minmaxdist = max((maxsum-minsum), (maxdiff-mindiff))/2
    return minmaxdist

def run_tests(file):
    tests = get_tests(file)
    station = []
    i = 0
    for case in tests:
        print("Test:", i)
        mmd = get_mmd(case)
        station = min_max(case)
        calc_max = max_dist(case, station)
        if mmd==calc_max:
            print("Station position:", station)
            print("Minimum maximum distance:", mmd)
            print("Max distance to station:", calc_max)
        else:
            print("TEST FAILED!\nTheoretical:", mmd, "\nActual:", calc_max)
        print("----------------------------------------------------------")
        i += 1

def run_rando(num_tests):
    tests = []
    station = []
    failed = 0
    for i in range(0, num_tests):
        tests.append(generate_coords())
    j = 0
    for case in tests:
        '''print("Test:", j)
        print(case)'''
        mmd = get_mmd(case)
        station = min_max(case)
        calc_max = max_dist(case, station)
        if mmd!=calc_max:
            print("TEST", j, "FAILED!\nTheoretical:", mmd, "\nActual:", calc_max)
            print(case)
            failed += 1
        j += 1
    if failed!=0:
        print("Number of failed Tests:", failed)
    else:
        print("All", num_tests, "tests passed.")

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
#string = "10\na b 6 0 c 3 0 e 9 0\nb a 6 0 c 4 0 d 2 0 g 9 0\nc a 3 0 b 4 0 d 2 0 e 9 0 f 9 0\nd b 2 0 c 2 0 f 8 0 g 9 0\ne a 9 0 c 9 0 f 8 0 j 18 0\nf c 9 0 d 8 0 e 8 0 g 7 0 i 9 0 j 10 0\ng b 9 0 d 9 0 f 7 0 h 4 0 i 5 0\nh g 4 0 i 1 0 j 4 0\ni f 9 0 g 5 0 h 1 0 j 3 0\nj e 18 0 f 10 0 h 4 0 i 3 0"

'''print(fromFile("Q2Test1.txt"))
print(fromString(str))
print(fromFile("Q2Test1.txt")==fromString(str))'''

#print(fromFile("Example.txt"))
'''print(min_span_tree("Example.txt"))
print("------------------------------------------")
print(min_span_tree("Q2Test1.txt"))

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(mst_traverse("Example.txt"))
print("------------------------------------------")
print(mst_traverse("Q2Test1.txt"))'''

'''print(min_max(ex1), max_dist(ex1, min_max(ex1)))
print(min_max(ex2), max_dist(ex2, min_max(ex2)))
print(min_max(ex3), max_dist(ex3, min_max(ex3)))
print(min_max(ex4), max_dist(ex4, min_max(ex4)))
print(min_max(ex5), max_dist(ex5, min_max(ex5)))
print("-----------------------------------------------------------------------------")

print_coords(generate_coords())'''

'''for idx in range(0, len(tests)):
    add_test(tests[idx], idx)'''

#print(get_tests("Q1Tests.txt"))
#new_test("Q1Tests.txt", 15)
#run_tests("Q1TestOutput.txt")
run_rando(random.randint(100, 500))