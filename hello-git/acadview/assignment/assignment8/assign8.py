#Q1
print("\n\n Q.1- What is Time Tuple?")
import time
a = time.ctime()     
print("time.ctime() returns STRING.")
print("Ex : " + a +"\n")

b = time.strptime(a)
print("time.strptime(string) returns TIME TUPLE")
print("Ex : " + str(b))



#Q2
print("\n\n Q.2- Write a program to get formatted time.")
import time
time.asctime()
print(time.asctime())


#Q3
print("\n\n Q.3- Extract month from the time.")
import datetime
myDate = datetime.date.today()
dateStr = str(myDate.month)
print("The month is : ")
print(dateStr)


#Q4
print("\n\n Q.4- Extract day from the time.")
import datetime
myDate = datetime.date.today()
dateStr = str(myDate.day)
print("The date is : ")
print(dateStr)


#Q5
print("\n\n Q.5- Extract date (ex : 11 in 11/01/2021) from the time. ")
import datetime
myDate = datetime.date.today()
dateStr = str(myDate.day) + "/" + str(myDate.month) + "/" + str(myDate.year)
print("The date is : ")
print(dateStr)


#Q6
print("\n\n Q.6- Write a program to print time using localtime method")
import time
print("time.localtime() method : ")
print(time.localtime())

#Q7
print("\n\n  Q.7- Find the factorial of a number input by user using math package function")
import math
number= int(input("enter the number"))
print(math.factorial(number))


#Q8
print("\n\n Q.8- Find the GCD of a number input by user using math package functions")
import math
a = int(input("Enter number : "))
b = int(input("Enter other number : "))
math.gcd(a, b)
print(math.gcd(a, b))


#Q9
print("\n\n Q.9- Use OS package and do the following tasks: \n1. Get current working directory. \n2. Get the user environment.")
import os
print("Current Working Directory is :   " + os.getcwd())
print(os.environ.get('PATH'))



