#Q.1- Write a Python program to read last n lines of a file

def lastnlines(f, n):
    with open(f) as file:
        print("last lines from file : ",f)
        for line in (file.readlines()[-n:]):
            print(line, end="")

name = "Home/Documents/python/acadview/workspace/hello-git/assignment14/assign14.txt"
n = int(input('Type the number of n last lines to read : '))
try:
    lastnlines(name,n)
except():
	print('File Error')





#Q.2- Write a Python program to count the frequency of words in a file.

from collections import Counter
def word_count(file):
        with open(file) as f:
                return Counter(f.read().split())

print("Words with their frequency are : \n",word_count("assign14.txt"))





#Q.3- Write a Python program to copy the contents of a file to another file 

import os
os.system('copy assign14.txt assignmen14.txt')






# Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open('assign14.txt') as fh1, open('assignmen14.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
         print(line1+line2)
        



#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

import random

b=[]
with open("assign14.txt", "w") as f:
    for i in range(10):
        a =random.random()
        b.append(a)
        f.write(str(a) + "\n")

a = b.sort()

with open("assignmen14.txt", "w") as f:
    for i in range(len(b)):
        f.write(str(b[i]) + "\n")












