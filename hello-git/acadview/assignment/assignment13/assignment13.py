#Q1
'''
Q.1- Name and handle the exception occured in the following program:

a=3
 if a<4:
    a=a/(a-3)
     print(a)



#1.  IndentationError -  if a<4: ---extra space given
#2.  IndentationError -  print(a) ---extra space given
#3.  ZeroDivisionError-  a=a/(a-3) ---divisible by zero not accepted
'''
#handling above exceptions by foll.
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
 print("DIVISIBILITY BY ZERO IS UNDEFINED\n\n")



#Q2
'''
Q.2- Name and handle the exception occurred in the following program:
l=[1,2,3]
print(l[3]) 



#1.  IndexError -  print(l[3]) ---list index out of range 
'''
#handling above exception by foll.
l=[1,2,3]

try:
    print(l[3])
    
except IndexError:
	print("list index out of range\n\n")
   


#Q3
'''
Q.3- What will be the output of the following code:
# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not


#1.  SyntaxError -  print "An exception" ---Missing parentheses in call to 'print'. Did you mean print("An exception")?
#2.  NameError   -  raise NameError("Hi there")  # Raise Error --- exception raise by user/coder
'''
##handling above exceptions by foll.

'''
output
(venv) rmultillioner@Rmultillioner:~/VirtualEnvironments$ python assign13.py
  File "assign13.py", line 4
    print "An exception"
                       ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("An exception")?






(venv) rmultillioner@Rmultillioner:~/VirtualEnvironments$ python assign13.py
An exception
Traceback (most recent call last):
  File "assign13.py", line 2, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there

'''
#It will raise a user defined 'NameError:  Hi there' because the raise command will call that error.It will also print the except statement 'An exception' because it was set to be invoked in the case of NameError.



#Q4
'''
Q.4- What will be the output of the following code:
 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#1. SyntaxError - print "a/b result in 0" ---Missing parentheses in call to 'print'
#2. SyntaxError - print c ---Missing parentheses in call to 'print'

'''
##handling above exceptions by foll.
'''
output
(venv) rmultillioner@Rmultillioner:~/VirtualEnvironments$ python assign13.py
  File "assign13.py", line 6
    print "a/b result in 0"
                          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("a/b result in 0")?
(venv) rmultillioner@Rmultillioner:~/VirtualEnvironments$ python assign13.py
  File "assign13.py", line 8
    print c
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(c)?







(venv) rmultillioner@Rmultillioner:~/VirtualEnvironments$ python assign13.py
-5.0
a/b result in 0
'''
#It is so because everytime the try block runs successfully,the else statement would print, otherwise an exception would be raised and it'd print the exception error.





#Q5.
'''
Q.5- Write a program to show and handle following exceptions:
1. Import Error
2. Value Error
3. Index Error
'''
# IMPORT ERROR
try:
    from tweeky import attri
except ImportError:
    print("There is no library found with this name")

# VALUE ERROR

    try:
        x = int(input("Enter a number : "))
        print(x)
        
    except ValueError:
        print("It is not a number")

#INDEX ERROR

i = int(input("enter index to print element"))
try:
	l = [1, 2, 3]
	print(l[i])
except IndexError:
      print("please enter a valid index!")




#Q6.
'''
Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18).
'''
class AgeTooSmallError:
    pass
def func():
    while True:
        try:
            value = int(input("Enter your age : "))
        except AgeTooSmallError:
            raise AgeTooSmallError
        if value < 18:
            print("WAIT,UNTILL YOU ARE 18 AND THEN TRY AGAIN")
            continue
        else:
            print("Accepted.")
            break
    return value

func()






















