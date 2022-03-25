from Q2 import asciindex, find_prev, min_span_tree
from Q3 import mst_traverse
abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascidx = []
for letter in abc:
    ascidx.append(asciindex(letter))
    print(asciindex(letter))

for idx in ascidx:
    print(find_prev(idx))