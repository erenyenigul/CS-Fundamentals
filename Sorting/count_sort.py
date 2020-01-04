def count_sort(list,max) :

    count = [0]*(max+1)
    new = [0]*len(list)
    for i in list:
        count[i]+=1
    count[0]-=1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in list:
        new[count[i]]=i
        count[i]-=1
    list.clear()
    list.extend(new)

