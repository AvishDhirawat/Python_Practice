Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> print('Hello World\n\t"hello world"\n\t\thello world?\nHello World!')
Hello World
	"hello world"
		hello world?
Hello World!
>>> print("Hello World",end=" ") print("Hello World",end=" ") print("Hello World",end=" ") print("Hello World",end=" ")
SyntaxError: invalid syntax
>>> print("Hello World",end=" "); print("Hello World",end=" "); print("Hello World",end=" "); print("Hello World",end=" ")
Hello World Hello World Hello World Hello World 
>>> a=100,b=200
SyntaxError: cannot assign to literal
>>> e=100,f=200
SyntaxError: cannot assign to literal
>>> e,f=100,200
>>> if(e and f):
	print(e and f)

200
>>> print(e<<)
SyntaxError: invalid syntax
>>> print(e and f)
200
>>> print(e or f)
100
>>> print(x&y)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(x&y)
NameError: name 'x' is not defined
>>> print(e&f)
64
>>> print(a&b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(a&b)
NameError: name 'a' is not defined
>>> a,b="Star","Lord"
>>> print(a&b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(a&b)
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> print(a and b)
Lord
>>> print(a or b)
Star
>>> print(e | f)
236
>>> a=10
>>> b="Chirag"
>>> print(type(a,b))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(type(a,b))
TypeError: type() takes 1 or 3 arguments
>>> print(type(a))
<class 'int'>
>>> print(type(b))
<class 'str'>
>>> c = 3.8
>>> print(type(if(a==0)))
SyntaxError: invalid syntax
>>> print(type(c))
<class 'float'>
>>> type(a&b)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    type(a&b)
TypeError: unsupported operand type(s) for &: 'int' and 'str'
>>> type(e&f)
<class 'int'>
>>> g = TRUE
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    g = TRUE
NameError: name 'TRUE' is not defined
>>> bool a=1001
SyntaxError: invalid syntax
>>> a =
SyntaxError: invalid syntax
>>> a = ""
>>> type(a)
<class 'str'>
>>> a
''
>>> b
'Chirag'
>>> c
3.8
>>> j
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    j
NameError: name 'j' is not defined
>>> a = "NULL"
>>> type(a)
<class 'str'>
>>> a = "None"
>>> type(a)
<class 'str'>
>>> a = None
>>> b = bool
>>> c = complex
>>> type(a)
<class 'NoneType'>
>>> type(b)
<class 'type'>
>>> type(c)
<class 'type'>
>>> "Write a program to add two numbers : \n 1st is Integer and 2nd is float"
'Write a program to add two numbers : \n 1st is Integer and 2nd is float'
>>> b = bool 1001
SyntaxError: invalid syntax
>>> bool 1001
SyntaxError: invalid syntax
>>> bool a = 1001
SyntaxError: invalid syntax
>>> int(input(a,b))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int(input(a,b))
TypeError: input expected at most 1 argument, got 2
>>> int(input("Enter a Number : "))
Enter a Number : 5
5
>>> a = 5+4j
>>> type(a)
<class 'complex'>
>>> a = True
>>> type(a)
<class 'bool'>
>>> a,b = int(input("Enter an Integer : ")), float(input("Enter a Floating Number : "))
Enter an Integer : 3
Enter a Floating Number : 5.6
>>> print(a+b)
8.6
>>> a,b = int(input("Enter an Integer : ")), int(input("Enter another Integer : "))
Enter an Integer : 25
Enter another Integer : 5
>>> print(type(a/b))
<class 'float'>
>>> pi = 3.140567
>>> r=int(input("Enter radius of Circle : "))
Enter radius of Circle : 5
>>> area = pi*r**2
>>> print(area)
78.514175
>>> print(area,end=2)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(area,end=2)
TypeError: end must be None or a string, not int
>>> print({area:.2f})
SyntaxError: invalid syntax
>>> area.format(.2f)
SyntaxError: invalid syntax
>>> {.2f}.format(area)
SyntaxError: invalid syntax
>>> a,b,c,d = 20,30,40,50
>>> dis=(((c-a)**2)+((d-b)**2)**0.5)
>>> print(dis)
420.0
>>> {.2f}.format(area)
SyntaxError: invalid syntax
>>> {:.2f}.format(area)
SyntaxError: invalid syntax
>>> {area:.2f}.format(area)
SyntaxError: invalid syntax
>>> area.split(:.2f)
SyntaxError: invalid syntax
>>> print("{0:.2f}".format(area))
78.51
>>> print("%.2f"%area)
78.51
>>> interset_rate=10
>>> intrest_rate=10
>>> amount=2500
>>> time=35
>>> SI=intrest_rate*time*amount/100
>>> print(SI)
8750.0
>>> p=2500
>>> r=10
>>> t=35
>>> n=3
>>> CI=p(1+(r/n))**(n*t)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    CI=p(1+(r/n))**(n*t)
TypeError: 'int' object is not callable
>>> CI=p*(1+(r/n))**(n*t)
>>> print(CI)
1.8376392372036044e+70
>>> p=2000
>>> r=5
>>> t=25
>>> n=2
>>> CI=p*((1+(r/n))**(n*t))
>>> print(CI)
3.1947156789289934e+30
>>> num=int(input("Enter a Number : "))
Enter a Number : 25
>>> num=int(input("Enter a Number : "));
Enter a Number : 27
>>> if(num%2==0):
	print("Number is Even")
    elif(num==0):
	    
SyntaxError: unindent does not match any outer indentation level
>>> if(num%2==0):
	print("Number is Even")
else:
	print("Number is Odd")

Number is Odd
>>> def ev_od:
	
SyntaxError: invalid syntax
>>> def ev_od(n):
	if(n%2==0):
	print("Number is Even")
	
SyntaxError: expected an indented block
>>> def ev_od(n):
	if(n%2==0):
		print("Number is Even")
	else:
		print("Number is Odd")

	
>>> ev_od(12)
Number is Even
>>> ev_od(23)
Number is Odd
>>> def p_n_z(n):
	if(n>0):
		print("Number is Positive")
	elif(n==0):
		print("Number is Zero")
	else:
		print("Number is Negative")

>>> p_n_z(5)
Number is Positive
>>> p_n_z(0)
Number is Zero
>>> p_n_z(-3)
Number is Negative
>>> def small_no(a,b):
	l=a if a>b else b

>>> def small_no(a,b):
	l=a if a>b else b
	print(l)

	
>>> small_no(25,15)
25
>>> small_no(20,32)
32
>>> def small_no(a,b):
	l=a if a<b else b
	print(l)

	
>>> small_no(25,10)]
SyntaxError: unmatched ']'
>>> small_no(25,10)
10
>>> small_no(26,32)
26
>>> def great_no(a,b):
	l=a if a>b else b
	print(l)

	
>>> great_no(25,10)
25
>>> great_no(34,776)
776
>>> def large_no(a,b,c):
	if(a>b and a>c):
		print("A is Largest")
	elif(b>a and b>c):
		print("B is Largest")
	else:
		print("C is Largest")

		
>>> large_no(25,76,33)
B is Largest
>>> def large_no(a,b,c):
	if(a>b and a>c):
		print(a," is Largest")
	elif(b>a and b>c):
		print(b," is Largest")
	else:
		print(c," is Largest")

>>> large_no(33,67,3)
67  is Largest
>>> def large_no(a,b,c):
	if(a>b and a>c):
		print(a,"is Largest")
	elif(b>a and b>c):
		print(b,"is Largest")
	else:
		print(c,"is Largest")

>>> large_no(35,6,23)
35 is Largest
>>> 
