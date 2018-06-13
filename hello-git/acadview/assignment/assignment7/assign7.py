#Q1
print("\n\n Q.1- Create a function to calculate the area of a circle by taking user radius ")

x = float(input("Enter radius of circle : "))
#Defining the function
def area(x):                            
    a = 3.14*x*x
    print("Area of circle is : ")
    print(a)
area(x)




#Q2
print("\n\n Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000 " )

#Defining the function
def perfect(n):
 sum=0
 for i in range(1,n):
     if n%i==0:
        sum=sum+i

 if sum==n:
  return True
 else:
  return False
for i in range(1,1001):
    if perfect(i):
      print(i)




#Q3
print("\n\n Q.3- Print multiplication table of 12 using recursion")

#Defining the function
def table(n,i):
    print(n*i)
    i=i+1
    if i<=10:
        table(n,i)
table(12,1)



#Q4
print("\n\n Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion")

#Defining the function
def power(a,b):
    if b == 1:
        return a
    else:
        return a * power(a,b-1)
x = int(input("Enter a number : "))
y = int(input("Enter it's power : "))
print (power(x,y))



#Q5
print("\n\n Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary ")

#Defining the function
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter the number:"))
f=fact(num)
dict={num:f}
print(dict)



