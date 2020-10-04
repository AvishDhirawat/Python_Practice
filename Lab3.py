Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> def Cal_Dist(x1,x2,y1,y2):
	d=((x2-x1)**2)+((y2-y1)**2)**(1/2)
	print("Distance : {:.2f}".format(d))

	
>>> x1,x2,y1,y2=map(int,input("Enter the X1 X2 Y1 and Y2 Respectively : ").split())
Enter the X1 X2 Y1 and Y2 Respectively : 23 54 67 88
>>> Cal_Dist(x1,x2,y1,y2)
Distance : 982.00
>>> import sys
a=sys.argv
print(a)
SyntaxError: multiple statements found while compiling a single statement
>>> import sys
>>> a=sys.argv
>>> print(a)
['']
>>> 
================================ RESTART: Shell ================================
>>> 
