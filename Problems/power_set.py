def power_set(set_) :
   power = set()
   arr = list(set_)
   for i in range(2**len(arr)):
       temp = []
       for j in range(len(arr)):
           if (i & (1 << j)) > 0 :
              temp.append(arr[j])
       power.add(tuple(temp))
   return power

print(power_set(set([1,2,3])))
