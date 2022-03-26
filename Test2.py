from Q2 import *
from Q3 import *
import random
'''abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascidx = []
for letter in abc:
    ascidx.append(asciindex(letter))
    print(asciindex(letter))

for idx in ascidx:
    print(find_prev(idx))'''

#print(mst_traverse("Example.txt"))
'''ex = fromFile("Q3Test1.txt")
for node in range(0, len(ex[1])):
    print(mst_traverse(ex, node)[1])'''

'''ex3 = fromFile("Q3Test3.txt")
for n in range(0, len(ex3[1])):
    print(mst_traverse(ex3, n)[1])
    print("------------------------------------------------------------------")'''

'''ex2 = fromFile("Q3Test2.txt")
for n in range(0, len(ex2[1])):
    print(mst_traverse(ex2, n)[1])
    print("------------------------------------------------------------------")'''

'''exam = fromFile("Example.txt")
for n in range(0, len(exam[1])):
    print(mst_traverse(exam, n)[1])
    print("------------------------------------------------------------------")'''

ex4 = fromFile("Q3Test4.txt")
print(ex4)
for n in range(0, len(ex4[1])):
    print(mst_traverse(ex4, n)[1])
    print("------------------------------------------------------------------")

'''def generate_graph(num_nodes):
    graph = [[]] * num_nodes
    for node in range(0, num_nodes):
        graph[node] = [find_prev(node)]
    num_edges = random.random((num_nodes-1)//2, num_nodes-1)'''

'''ex5 = fromFile("Q3Test5.txt")
for n in range(0, len(ex5[1])):
    print(mst_traverse(ex5, n)[1])
    print("------------------------------------------------------------------")
'''
'''ex6 = fromFile("Q3Test6.txt")
for n in range(0, len(ex6[1])):
    print(mst_traverse(ex6, n)[1])
    print("------------------------------------------------------------------")

ex7 = fromFile("Q3Test7.txt")
for n in range(0, len(ex7[1])):
    print(mst_traverse(ex7, n)[1])
    print("------------------------------------------------------------------")'''