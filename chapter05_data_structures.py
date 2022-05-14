# LISTS

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4) # Find next banana starting a position 4

fruits.reverse()

fruits.append('grape')

fruits.sort()

#  USING LISTS AS STACKS

stack = [3, 4, 5]

stack.append(6)

stack.append(7)

stack.pop()

stack.pop()

# USING LISTS AS QUEUES

from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry") # Terry arrives

queue.append("Graham") # Graham arrives

queue.popleft() # The first to arrive now leaves

queue.popleft() # The second to arrive now leaves

queue # Remaining queue in order of arrival

# LIST COMPREHENSIONS

squares = []

for x in range(10):
    squares.append(x**2)

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

from math import pi

[str(round(pi, i)) for i in range(1, 6)]

# NESTED LIST COMPREHENSIONS

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]

list(zip(*matrix))

# THE del STATEMENT

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]

# TUPLES AND SEQUENCES

t = 12345, 54321, 'hello!'

v = ([1, 2, 3], [3, 2, 1])

empty = ()

singleton = 'hello', # <-- note trailing comma

len(empty)

len(singleton)

x, y, z = t

# SETS

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

'orange' in basket # fast membership testing

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')

b = set('alacazam')

a # unique letters in a

a - b # letters in a but not in b

a | b # letters in a or b or both

a & b # letters in both a and b

a ^ b # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}

# DICTIONARIES

tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127

del tel['sape']

{x: x**2 for x in (2, 4, 6)}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

# EXECUTING MODULES AS SCRIPTS

# STANDARD MODULES

# THE dir() FUNCTION

import builtins

dir(builtins)

# PACKAGES

