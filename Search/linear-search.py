def linear_search(list, integer) :
    for i in range(len(list)):
        if integer == list[i]:
            return i
    return -1
