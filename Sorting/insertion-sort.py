def insertion_sort(list) :
    for i in range(1,len(list)) :
        index = 0
        temp = list[i]
        for j in range(i):
          if  list[j] < list[i] :
              index = j+1
        for k in reversed(range(index,i)):
            list[k+1] = list[k]
        list[index] = temp
