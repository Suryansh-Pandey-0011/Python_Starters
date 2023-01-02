Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
all([1,2,3,4,5,6,7,8,9]])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
all([1,2,3,4,5,6,7,8,9])
True
all([0,1,2,3,4,5,6,7,8,9])
False
any([1,0])
True
any([0,0,0,0,])
False
enumerate([1,2,3,"d","g","f","d"])
<enumerate object at 0x00000231F60423C0>
list(enumerate([1,2,3,"d","g","f","d"]))
[(0, 1), (1, 2), (2, 3), (3, 'd'), (4, 'g'), (5, 'f'), (6, 'd')]
all([])
True
any([])
False
>>> l=[345,56,678,234,67]
>>> print(sorted(l))
[56, 67, 234, 345, 678]
>>> l=['s','d','f','r']
>>> print(sorted(l))
['d', 'f', 'r', 's']
>>> print(sorted(l, reverse=True))
['s', 'r', 'f', 'd']
>>> 
==================== RESTART: C:/PythonPrograms/list-sort.py ===================
10,55,69,456,78
length: 5
list enumerate: [(0, '10'), (1, '55'), (2, '69'), (3, '456'), (4, '78')]
max: 78
min: 10
>>> 
==================== RESTART: C:/PythonPrograms/list-sort.py ===================
data: 15,1561,5,84115,54
length: 5
list enumerate: [(0, '15'), (1, '1561'), (2, '5'), (3, '84115'), (4, '54')]
max: 84115
list: ['15', '1561', '5', '54', '84115']
>>> 
==================== RESTART: C:/PythonPrograms/list-sort.py ===================
data: 1551,21561,13,1332,26
length: 5
list enumerate: [(0, '1551'), (1, '21561'), (2, '13'), (3, '1332'), (4, '26')]
max: 26
min: 13
list: ['13', '1332', '1551', '21561', '26']
>>> 
==================== RESTART: C:/PythonPrograms/list-sort.py ===================
data: 12215,151,1212,18415,45
length: 5
list enumerate: [(0, 12215), (1, 151), (2, 1212), (3, 18415), (4, 45)]
max: 18415
min: 45
list: [45, 151, 1212, 12215, 18415]
