Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Cal_Dist(x1,x2,y1,y2):
	d=((x2-x1)**2)+((y2-y1)**2)**(1/2)
	print("Distance : {:.2f}".format(d))

>>> x1=int(input("Enter the X1 and X2 : "));
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x1=int(input("Enter the X1 and X2 : "))
ValueError: invalid literal for int() with base 10: 'x1=int(input("Enter the X1 and X2 : "));'
>>> x1,x2=int(input("Enter the X1 and X2 : "))
Enter the X1 and X2 : 23 54
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x1,x2=int(input("Enter the X1 and X2 : "))
ValueError: invalid literal for int() with base 10: '23 54'
>>> x1,x2=int(map(input.split("Enter the X1 and X2 : ")))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x1,x2=int(map(input.split("Enter the X1 and X2 : ")))
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> x1,x2=map(int(input.split("Enter the X1 and X2 : ")))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x1,x2=map(int(input.split("Enter the X1 and X2 : ")))
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> x1=int(input("Enter the X1 : "))
Enter the X1 : 23
>>> cal_Dist(23,54,67,98)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cal_Dist(23,54,67,98)
NameError: name 'cal_Dist' is not defined
>>> Cal_Dist(23,54,67,98)
Distance : 992.00
>>> def Cal_Dist(x1,x2,y1,y2):
	d=((x2-x1)**2)+((y2-y1)**2)^(1/2)
	print("Distance : {:.2f}".format(d))

	
>>> Cal_Dist(23,54,67,98)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Cal_Dist(23,54,67,98)
  File "<pyshell#13>", line 2, in Cal_Dist
    d=((x2-x1)**2)+((y2-y1)**2)^(1/2)
TypeError: unsupported operand type(s) for ^: 'int' and 'float'
>>> def Cal_Dist(x1,x2,y1,y2):
	d=((x2-x1)**2)+((y2-y1)**2)**(1/2)
	print("Distance : {:.2f}".format(d))
	
