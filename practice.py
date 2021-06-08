Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1
>>> b=2
>>> print(a==b)
False
>>> letters=["a","b","c","d","e","f","g","h","i"]
>>> a,c,e,g,i
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a,c,e,g,i
NameError: name 'c' is not defined
>>> letters[::2]
['a', 'c', 'e', 'g', 'i']
>>> 
>>> 
>>> a=range(10)
>>> list(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=range(10)
>>> a
range(0, 10)
>>> list(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=range(1,11)
>>> list(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> b=list(a)
>>> b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in b:
	print(i*10)

	
10
20
30
40
50
60
70
80
90
100
>>> c=[i*10 for i in b]
>>> c
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> 
>>> 
>>> [10]
[10]
>>> 
>>> 
>>> b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> c=[]
>>> for i in b:
	d=i*10
	c.append(d)
	print(c)

	
[10]
[10, 20]
[10, 20, 30]
[10, 20, 30, 40]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 40, 50, 60, 70, 80]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> c
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> for i in b:
	d=i*10
	c.append(d)

	
>>> 
>>> 
>>> 


>>> 


>>> 

>>> 


>>> 

>>> 
>>> 
>>> b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> c=[]
>>> for i in b:
	d=i*10
	c.append(d)
	print(c)

	
[10]
[10, 20]
[10, 20, 30]
[10, 20, 30, 40]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 40, 50, 60, 70, 80]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> c
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> 
>>> 
>>> 
>>> list1=[1,1,"1",2,3,4,1,1,2,3]
>>> 1,"1",2,3,4
(1, '1', 2, 3, 4)
>>> set(list1)
{1, 2, 3, 4, '1'}
>>> d=set(list1)
>>> d
{1, 2, 3, 4, '1'}
>>> list(d)
[1, 2, 3, 4, '1']
>>> list1
[1, 1, '1', 2, 3, 4, 1, 1, 2, 3]
>>> from collections import OrderedDict
>>> x=OrderedDict.fromkeys(list1)
>>> x
OrderedDict([(1, None), ('1', None), (2, None), (3, None), (4, None)])
>>> 
>>> list(x)
[1, '1', 2, 3, 4]
>>> x=list(OrderedDict.fromkeys(list1))
>>> x
[1, '1', 2, 3, 4]
>>> 
>>> list(dict.fromkeys(list1))
[1, '1', 2, 3, 4]
>>> (dict.fromkeys(list1))
{1: None, '1': None, 2: None, 3: None, 4: None}
>>> list1
[1, 1, '1', 2, 3, 4, 1, 1, 2, 3]
>>> list2=[]
>>> for i in list1:
	if i not in list2:
		list2.append(i)
		print(list2)

		
[1]
[1, '1']
[1, '1', 2]
[1, '1', 2, 3]
[1, '1', 2, 3, 4]
>>> list2
[1, '1', 2, 3, 4]
>>> print("hello")

