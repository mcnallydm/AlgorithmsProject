import copy

def bubble(list_coords, col):
    sorted_list = copy.deepcopy(list_coords)
    go = True
    while (go):
        swapped = False
        for idx in range(0, len(sorted_list)-1):
            if sorted_list[idx][col]>sorted_list[idx+1][col]:
                temp = sorted_list[idx]
                sorted_list[idx] = sorted_list[idx+1]
                sorted_list[idx+1] = temp
                swapped = True
            elif sorted_list[idx][col]==sorted_list[idx+1][col]:    # Sorts by y secondarily
                secondary = (col+1)%2
                if sorted_list[idx][secondary]>sorted_list[idx+1][secondary]:
                    temp = sorted_list[idx]
                    sorted_list[idx] = sorted_list[idx+1]
                    sorted_list[idx+1] = temp
                    swapped = True
        if swapped==False:
            go = False
    return sorted_list


def sort_houses(list_houses):
    # list_houses is an array of arrays of coordinates
    both_lists = [] # An array containing both sorted lists
    sort_x = bubble(list_houses, 0)
    both_lists.append(sort_x)
    sort_y = bubble(list_houses, 1)
    both_lists.append(sort_y)
    return both_lists