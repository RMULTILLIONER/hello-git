#Q1
print("Q1 Create a list with user defined inputs.")
x = []
print("Enter no. of elements in list")
p = int(input())
print("Enter %d list values" % (p))
for i in range(0, p):
    x.append(input())
print(x)
print("\n")


#Q2
print("Q2 Add the following list to above created list:[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]")
x.append('google')
x.append('apple')
x.append('facebook')
x.append('microsoft')
x.append('tesla')
print(x)
print("\n")


#Q3
print("Q3 Count the number of time an object occurs in a list. ")
print("google occur : " + str(x.count('google')))
print("apple occur : " + str(x.count('apple')))
print("facebook occur : " + str(x.count('facebook')))
print("microsoft occur : " + str(x.count('microsoft')))
print("tesla occur : " + str(x.count('tesla')))
print("1 occur : " + str(x.count('1')))
print("\n")


#Q4
print("Q4 Create a list with numbers and sort it in ascending order.")
a = []
print("Enter no of elements :")
y = int(input())
print("Enter %d elements" %(y))
for i in range(0, y):
    a.append(int(input()))
print(a)
a.sort()
print("Sorted list : ")
print(a)
print("\n")


#Q5
print("Q5 Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]")
arr_a = [1,10,19,21]
arr_b = [6,8,11,30]
arr_c = []
print("Array A : " + str(arr_a))
print("Array B : " + str(arr_b))
print("Merging of array A and array B into array C")
arr_c = arr_a + arr_b
print(arr_c)
print("Sorting of Array C")
arr_c.sort()
print(arr_c)
print("\n")


#Q6
print("Q6 Implement a stack and queue using lists.")
print("\nImplementing Stack :")
stack = ["I", "AM", "A"]
stack.append("GREAT")
stack.append("MAN")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print("\nImplementing Queue :")
from collections import deque
queue = deque(["I", "AM", "GREAT", "MAN"])
print(queue)
queue.append("BE")
print(queue)
queue.append("ALIVE")
print(queue)
print(queue.popleft())                 
print(queue.popleft())                 
print(queue)
print("\n")


#Q7
print("Q7 Count even and odd numbers in that list.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,12,12,12,1,1,2,2] 
print(numbers)
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
