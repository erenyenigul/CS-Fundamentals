ALL = []
def find(a,i):

    c = check(a)
    if c == 1 :
       ALL.append(a.copy())
       print(a)
    elif (c ==0):
       if (i<(len(a)-1)) :
           find(a.copy(),i+1)
       a[i] += 1
       find(a.copy(),i)
    else :
        return

def check(b):
    result = b[0]*1+b[1]*2+b[2]*5+b[3]*10+b[4]*20+b[5]*50+b[6]*100+b[7]*200
    if  result < 200 : return 0
    elif result == 200: return 1
    else :return 2

c = [0]*8
find(c.copy(),0)
print(len(ALL))