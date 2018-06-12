#Q1
print(" Q.1- Take 10 integers from user and print it on screen.  ")
output = list()
print("\nEnter values to List : ")
for i in range(10):
    int_val = int(input(("Enter %d value : ") %(i+1)))  
    output.append(int_val)
print("Integer List : " ,output)



#Q2
print("\n\n Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true")
print("Done in another file ")

#Q3
print("\n\n Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list. ")
List1 = list()
List2 = list()
print("Enter values to find Square List: ")
for a in range(10):
    int_val1 = int(input(("Enter %d value : ") %(a+1)))
    List1.append(int_val1)       
print("Integer List : " ,List1)
for item in List1:
    sqr_val = item*item
    List2.append(sqr_val)          
print("Square List: " ,List2)

#Q4
print("\n\n Q.4- From a list containing ints, strings and floats, make three lists to store them separately ")
List_1 = [ 231,232,23,"z", "r", 3,1.43, 34.34, 8.32]
int_List = [ i  for i in List_1 if isinstance(i, int) ]
str_List = [ i  for i in List_1 if isinstance(i, str) ]
float_List = [ i  for i in List_1 if isinstance(i, float) ]
print("Mix List : " , List_1)
print("Int List : " ,int_List)
print("Str List : " ,str_List)
print("Float List : " ,float_List)

#Q5
print("\n\n Q.5- Using range(1,101), make a list containing even and odd numbers.  ")
List_a = list()
List_b = list()
for li in range(1,101):
    if(li % 2 == 0):
        List_a.append(li)
    else:
        List_b.append(li)
print("\nEven List : ", List_a)
print("\nOdd List : ", List_b)

#Q6
print("\n\n Q.6- Print the pattern:")
pattern = '*'
for i in range(1,5):
 print(pattern*i)


#Q7
print("\n\n Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop")
Dict = dict()
print("Enter element , Key:Valuepair : ")
for i in range(5):
    key = input(("Enter key %d ") % (i+1))
    value = input(("Enter Value of %d key ") % (i+1))
    Dict[key] = value
for it in Dict:
 print(it,':',Dict[it])

#Q8
print("\n\n Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop")
number = int(input("Enter length of List : "))
list_1 = list()
print("Enter element to List : ")
for x in range(number):
    in_val = input()
    list_1.append(in_val)
print(" List : ", list_1)
del_item = input(("Enter the input to delete : "))
if( del_item in list_1):
    list_1.remove(del_item)
    print(" List after deletion : ", list_1)
else:
    print("Not in List")



