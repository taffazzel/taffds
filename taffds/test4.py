import array


def do_thing(l):
    '''l.append(3)'''
    l.append(67)

'''l=[0]
print(l)
do_thing(l)
print(l)
'''
'''
array=[1,2,3,4]
import numpy as np

a = np.array([5,3,4,'y'])
b=[5,6,7]
print(a)
print(type(a))

'''

import numpy as np
from array import *
arr = np.array([1, 2, 3, "ABV", 'Y'])
print(arr.ndim)
print(type(arr))
a=array('d',[1.2,1.3,2.3])
print(a)
print(type(a))


x = np.array([1,2,'C'])
x1 = array('d',[1,2])
'''Find a peak element which is not smaller than its neighbours'''

'''
x=[10,15,7,8,1,25,30]
from array import *
y = sorted(x,key=lambda x:x,reverse=True)
dd = array('i',[1,2,3])
print(dd)
x1 = dd[::-1]
print(type(list(dd[::-1])))


a = [1,2,3,4]
b = ['c','d','r','w']
list2=[(3, 'r'), (3, 'w'), (4, 'c')]
list3=[]
for i in a:
    for j in b:
        if (i,j) not in list2:
            print("not in list2",(i,j))
            list3.append((i,j))


[[(i,j) for j in b if (i,j) not in list2] for i in a]



[i for i in a if i>2]

[i*2 for i in a]

for i in a:
    print(i*2)

[i for i in a]

[[i for i in a]]'''


list1 = [1, 2, 3, 4, 1, 3, 5, 2, 3, 5, 6, 1, 2, 3, 5, 5, 2,10,8,7]
list2=[1,3,4,5]
l3=[]
l4=[]
'''[[print(i,j) for j in range(5)] for i in range(5)]'''
for i in list1:
    if i not in list2:
        l3.append(i)


l4 = [i for i in list1 if i not in list2]
print([[(i,j)for j in list2 if j>2] for i in list1 if i >7])
print("YES")
print(list(set(l4)))

for i in list1:
    for j in list2:
        if i>7 and j>2:
            print(i,j)


92197419534
992582