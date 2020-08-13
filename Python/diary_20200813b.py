Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit[1] + fruit[3]+fruit[5]
>>> print(letter)
aaa
>>> len(fruit)
6
>>> number = []
>>> len(numbers)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    len(numbers)
NameError: name 'numbers' is not defined
>>> numbers =[]
>>> len(numbers)
0
>>> numbers.append(1)
>>> len(numbers)
1
>>> numbers.append(55)
>>> len(numbers)
2
>>> numbers
[1, 55]
>>> vardi = ['a', 'ab', 'abc']
>>> vardi
['a', 'ab', 'abc']
>>> vardu_garumi =[]
>>> vardu_garumi.append(len(vardi[0]))
>>> vardu_garumi.append(len(vardi[1]))
>>> vardu_garumi.append(len(vardi[2]))
>>> vardu_garumi
[1, 2, 3]
>>> type(vardi)
<class 'list'>
>>> type(vardu_garumi)
<class 'list'>
>>> inex = 0
>>> while index <len(fruit):
	letter = fruit[index]
	print(letter)
	index = index +1

	
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    while index <len(fruit):
NameError: name 'index' is not defined
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    while index < len(fruit):
NameError: name 'index' is not defined
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> index = 6
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> index = 0
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> index = 5
>>> while index > len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> while index => len(fruit):
		letter = fruit[index]
	print(letter)
	index = index - 1
	
SyntaxError: invalid syntax
>>> while index => len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1
	
SyntaxError: invalid syntax
>>> while index >= len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> index = 6 - 1
>>> while index >= len(fruit):
	letter = fruit[index]
	print(letter)
	index = index - 1

	
>>> index = 5
>>> while index >= 0:
	letter = fruit[index]
	print(letter)
	index = index - 1

	
a
n
a
n
a
b
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
>>> print(s[6:11])
Pytho
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit[3:4]
'a'
>>> type(fruit)
<class 'str'>
>>> fruit[:]
'banana'
>>> 
