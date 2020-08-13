Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
labi
>>> a=5.5
>>> 
>>> 
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
slikti
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("ari labi")
else:
	print("slikti")

	
ari labi
>>> a = h
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a = h
NameError: name 'h' is not defined
>>> a="dd"
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("ari labi")
else:
	print("slikti")

	
slikti
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("ari labi")
elif type(a)==int:
	print("ir jau labi")
else:
	print("slikti")

	
slikti
>>> a = 10
>>> 
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("ari labi")
elif type(a)==int:
	print("ir jau labi")
else:
	print("slikti")

	
labi
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("ari labi")
elif type(a)==int:
	print("ir jau labi - bet so tekstu neviens nekad neredzes")
else:
	print("slikti")

	
labi
>>> print("aa\n bbbb\n cccc\n")
aa
 bbbb
 cccc

>>> print(" aa\n bbbb\n cccc\n")
 aa
 bbbb
 cccc

>>> 
