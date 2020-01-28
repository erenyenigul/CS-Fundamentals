import sys

print(sys.version)
graph = {
         'S': set([('A',1), ('G',12)]),
         'A': set([('B',3), ('C',1)]),
         'B': set([('D',3)]),
         'D': set([('G',3)]),
         'C': set([('D',1), ('G',1)])
         }
#priority queue
queue = []
queue.append([['S'],0])

def sortKey(val):
    return val[1]

while not len(queue)==0 :
    current = queue.pop(0)

    if(current[0][-1]!='G'):
        for next in graph[current[0][-1]]:
            list = current[0][:]
            list.append(next[0])
            cost = current[1] + next[1]
            queue.append([list, cost])
            queue.sort(key=sortKey)
    else:
        print "Lowest cost path is"
        print(current[0])
        break


