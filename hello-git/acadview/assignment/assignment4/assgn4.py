#tupple----WAP to create a tuple with diff. data types
 
tup_datatype= (5,10,0.1121,[1,22.2,'data type'], 'got this','ok' ,{5,4,3,6}, {1:'value','key':2})
#find lenght of tuple
print(len(tup_datatype))
print("\n")

#largest and smallest elements of tuple
tuple_datatype= (5,10,0.1121,-1,-2,-0.912)
print(max(tuple_datatype))
print(min(tuple_datatype))
print("\n")

#wap to find product of all element of a tuple
print(tuple_datatype[0]*tuple_datatype[1]*tuple_datatype[2]*tuple_datatype[3]*tuple_datatype[4]*tuple_datatype[5])
print("\n")
print("\n")



#set----
a = set([1,2,3,4,5,6,7,8])
b = set([3,4,5,6])
#diff
c = a - b
print('The difference of sets : ')
print(c)
print("\n")

#compare
print(a==b)
print("\n")

#intersection
c = a & b
print('Intersection of sets : ')
print(c)
print("\n")
print("\n")


#dictionary
#create a dictionary to store name and marks of 10 students by user input.
print('Enter name and marks for 10 students : ')
a = {}
for i in range(10):
	key = input('enter name  ')
	value = int(input('enter marks  '))
	a[key] = value
	print(a)
print("\n")

#sort dictionary created in previous question according to marks.
import operator
sort = sorted(a.items(), key=operator.itemgetter(1))
print(sort)
print("\n")
print("\n")

#Count occurences of each letter in word "MISSISSIPPI". Store count of every letter with a letter in a dictionary.
import collections
count = collections.Counter("MISSISSIPPI")
print(count)




