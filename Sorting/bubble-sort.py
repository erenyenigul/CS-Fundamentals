def bubble_sort(list) :
    for i in range(len(list)-1):
        for j in range(1,len(list)):
            if list[j] < list[j-1] :
                temp=list[j]
                list[j] = list[j-1]
                list[j-1] = temp
