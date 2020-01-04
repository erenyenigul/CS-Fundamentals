def count_sort_radix(list,exp):

    count = [0]*(10)
    new = [0]*len(list)
    for i in list:
        count[int(i/(10**exp))%10]+=1
    count[0]-=1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in reversed(list):
        new[count[int(i/(10**exp))%10]]=i
        count[int(i/(10**exp))%10]-=1
    list.clear()
    list.extend(new)
    
def radix_sort(list,maximum=None):
    i = 0
    if maximum is None:
        maximum = max(list)
    while maximum/(10**i) >= 1 :
        count_sort_radix(list,i)
        i+=1
        