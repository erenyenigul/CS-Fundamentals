#Computer Project 1
def max(list) :
   max = 0
   for i in range(len(list)):
       if max < list[i]:
           max = list[i]
   return max

#Computer Project 2

def first_last(list) :
    first = -1
    last = -1
    max = 0
    for i in range(len(list)):
        if max < list[i]:
            first = i
            max = list[i]
        elif max == list[i]:
            last = i
    return (first,last)

#Computer Project 3

def linear_search(list, integer) :
    for i in range(len(list)):
        if integer == list[i]:
            return i
    return -1
#Computer Project 4

def binary_search(list, integer):
    i=0
    j=len(list)-1
    while list[i] != integer :
        k = int((i+j)/2)
        if  list[k] < integer :
            i=k+1
        else :
            j=k
    return i
#Computer Project 5

def bubble_sort(list) :
    for i in range(len(list)-1):
        for j in range(1,len(list)):
            if list[j] < list[j-1] :
                temp=list[j]
                list[j] = list[j-1]
                list[j-1] = temp

#Computer Project 6

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

#Computer Project 7

def change(coins,n) :
    #Assumed that the list 'coins' is sorted
    #An example input : [100,25,5,1],123 
    coin = 0
    for d in coins:
        while d <= n :
            n -= d
            coin+=1
    return coin

#Computer Project 8

def schedule(timetable) :
    #timetable is a list which has tuples with 2 items : first one is the start time
    #and the second is the end time for each talk.
    
    timetable.sort(key = lambda x: x[1])
    #Set of all talks which is selected:
    S = set()
    for i in timetable :
        compatible = True
        for j in S:
           if i[0]<j[1] : compatible = False
        if compatible : S.add(i)
    return S

#Computer Project 9

def linear_comparison(list,integer):
    i = 0
    while list[i] != integer:
      i += 1
    return i

def binary_comparison(list,integer):
    counter = 0
    i=0
    j=len(list)-1
    while list[i] != integer :
        k = int((i+j)/2)
        if  list[k] < integer :
            i=k+1
        else :
            j=k
        #Comparison made in the beginning of the iteration and
        #in if or else statements(1+1) 
        counter += 2
    return counter

#Computer Project 10

def bubble_sort_comparison(list) :
    counter = 0
    for i in range(len(list)-1):
        for j in range(1,len(list)):
            if list[j] < list[j-1] :
                temp=list[j]
                list[j] = list[j-1]
                list[j-1] = temp
            counter+=1
    return counter

def insertion_sort_comparison(list) :
    counter = 0
    for i in range(1,len(list)) :
        index = 0
        temp = list[i]
        for j in range(i):
          if  list[j] < list[i] :
              index = j+1
          counter+=1
        for k in reversed(range(index,i)):
            list[k+1] = list[k]
        list[index] = temp
    return counter







    

