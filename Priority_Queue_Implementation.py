import heapq

class PriorityQueue:

    def __init__(self):
        self._queue=[]
        self._index=0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index+=1
    def pop(self):
        heapq.heappop(self._queue)[-1]

'''heappush and heappop functions work on a list queue so that first item in the list has the smallest priority
here we have negated the priority value since we want the list to work or sort from highest to the lowest priority
'''
class Item:
    def __init__(self):
        self.name=name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
q=PriorityQueue()
q.push(Item('manga'),1)
q.push(Item('kumar'),4)
q.push(Item('saroja'),5)
q.push(Item('narasimha rao'),1)
q.pop()
q.pop()
q.pop()
q.pop()
