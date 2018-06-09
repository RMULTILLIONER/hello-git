#Q1

print("Q.1- Take an input year from user and decide whether it is a leap year or not.")

year=int(input("enter any year you want: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("This is a leap year")
       else:
            print("Not a leap year")
   else:
        print("This is a leap year")
else:
     print("Not a leap year")


#Q2

print("\n\n Q.2- Take length and breadth input from user and check whether the dimension are of sqr. or rect.")

l = int(input("Enter length : "))
b = int(input("Enter breath : "))

if l == b:
        print("Dim. of square.")
else:
     print("Dim. of rectangle.")


#Q3

print("\n\n Q.3- Take the input age of 3 person and determine oldest and youngest among them.")

a=int(input("Enter 1st person age : "))
b=int(input("Enter 2nd person age : "))
c=int(input("Enter 3rd person age : "))
if a>b:
        if a>c:
                print("Person 1 is oldest.")
        else:
                print("Person 3 is oldest.")
if b>a:
        if b>c:
                print("Person 2 is oldest.")
        else:
                print("Person 3 is oldest.")

if a<b:
        if a<c:
                print("Person 1 is youngest.")
        else:
                print("Person 3 is youngest.")
if b<a:
        if b<c:
                print("Person 2 is youngest.")
        else:
             print("Person 3 is youngest.")


#Q4

print("\n\n Q.4 Points.")

points=int(input("enter points of competitor: "))
if points in range(1,51):
    print("Sorry! No prize this time.")
elif points in range(51,151):
    print("Congratulations! You won a Wooden Dog.")
elif points in range(151,181):
    print("Congratulations! You won a Book.")
elif points in range(181,201):
    print("Congratulations! You won Chocolates.")
else:
    print("Invalid Input ENTERED")

#Q5

print("\n\n Q.5-Shop -discount of 10%. Judge and print total cost for user. ")

quantity=int(input("Enter quantity of item: "))
if quantity*100>1000:
    print("total cost will be:",quantity*100-0.1*(quantity*100))
else:
    print("total cost will be:",quantity*100)


