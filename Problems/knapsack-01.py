
weight = [4,3,4,2,3,10,9,10]
value  = [2,3,4,10,34,1,10000,9999]


N = 7
CAPACITY = 10

arr = [[None]*(CAPACITY+1)]*(N+1)

def K(n,c):
  if arr[n][c] != None :
      return arr[n][c]
  elif n==-1 or c==0:
      return 0
  elif weight[n]>c:
      return K(n-1,c)
  else :
      temp1 = K(n-1,c)
      temp2 = value[n] + K(n-1,c-weight[n])
      result= max(temp1,temp2)
      arr[n][c] = result
      print(result)
      return result

print(K(N,CAPACITY))
