from util import Queue, Stack

graph = {
         'S': set(['A', 'G']),
         'A': set(['B', 'C']),
         'B': set(['D']),
         'D': set(['G']),
         'C': set(['D', 'G'])
         }

def graph_search(graph,start,end,a) :
    a.push(start)
    visited = list()
    while not a.isEmpty() :
        current = a.pop()
        visited.append(current)
        if current == end:
            break
        for e in graph[current]:
            a.push(e)
    return visited


stack = Stack()
queue = Queue()

graph_search(graph,'S','G',queue)
graph_search(graph,'S','G',stack)