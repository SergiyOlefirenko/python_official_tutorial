'''
It is also possible to use a list as a queue, 
where the first element added is the first element retrieved (“first-in, first-out”);
To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.
'''

from collections import deque


queue = deque(['Eric', 'Jhon', 'Michael'])
queue.append('Terry')
queue.append('Graham')
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
