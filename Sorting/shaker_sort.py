

def shaker_sort(arr):
    a = range(1,len(arr))
    s = True
    while s:
      for i in a:
        s = False
        if arr[i-1]>arr[i] :
           temp = arr[i-1] 
           arr[i-1] = arr[i]
           arr[i] = temp
           s = True
      a = list(reversed(a))

arr = [1,2,37,8,0,9,9,99,8]
shaker_sort(arr)
print(arr)
