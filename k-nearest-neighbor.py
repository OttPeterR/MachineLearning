# K Nearest Neighbor
import math


def count(a, b):
    if(a == b):
        return 0
    else:
        return 1


def squared(a, b):
    dif = math.fabs(a - b)
    return dif * dif


def manhattan(a, b):
    return math.fabs(a - b)


def dual_list_func(list1, list2, diff_func):
    # lists must be the same length
    if(len(list1) != len(list2)):
        return -1

    # sum the specified differences in the elements
    count = 0
    for i in range(len(list1)):
        count += diff_func(list1[i], list2[i])
    return count


def difference(list1, list2, measure='count'):
    if(measure == 'manhattan'):
        return dual_list_func(list1, list2, manhattan)
    elif (measure == 'squared'):
        return dual_list_func(list1, list2, squared)
    else:  # 'count'
        return dual_list_func(list1, list2, count)



def maplist(func, lis):
    return list(map(func, lis))


def k_nearest_neighbor(examples, new_example, k=1, measure='count'):
    # a list of [ (distance, class) ... ]
    distance = maplist(lambda e: [difference(e[0], new_example[0], measure)],
                       examples)

    # sort distance by least distance value
    def getKey(pair):
        return pair[0]
    sorted_distance = sorted(distance, key=getKey)

    # distance values are not needed anymore, just take the classes
    neighbors = maplist(lambda pair: pair[1], sorted_distance)

    # return the most common of the k nearest neighbors
    neighbors = neighbors[0:k]
    return max(set(neighbors), key=neighbors.count)
