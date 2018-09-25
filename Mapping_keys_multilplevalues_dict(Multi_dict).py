

'''For mapping a single key to multiple values we can map a single key to either a set or a list data type
list will always maintain the order of the insertion items
where as in sets it has got to remove the duplicates 
our option to remove based on our requirement'''

from collections import defaultdict
d=defaultdict(list) # it is a dictionary where we can map a list to a single key value
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

d=defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(1)
print(d)


d={} '''creating an empty dictionary'''
for key ,value in pairs:
    if key not in d:
        d[key]=[]
        d[key].append(value)


d=defaultdict(list)
for key ,value in pairs:
    d[key].append(value)
