#Q1

print("Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.\n")
'''
importing the time and thread modules
'''
import threading
import time

t = threading.Thread()
t.start()
print(threading.currentThread().getName())
time.sleep(5)                                          # Setting the sleep time of threads
print("MESSAGE DISPLAYED AFTER 5 SECONDS.........")    # Print message after they wake up




#Q2

print("\n\nQ2. Make a thread that prints numbers from 1-10, waits for 1 sec between")

'''
importing the time and thread modules
'''

import threading
import time

class mythread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("\nThread Starting.........")
        i=1
        while i<=10:
            print(i)
            time.sleep(1)
            i+=1
        print("\nThread Ended...........")

t = mythread()
t.run()




#Q3

print("\n\nQ3. Make a list that has 5 elements.Create a threading process that prints the \n5 elements of the list with a delay of multiple of 2 sec between each display.\nDelay goes like 2sec-4sec-6sec-8sec-10sec ")
'''
importing the time and thread modules
'''

import threading
import time

class mythread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Thread starting....")


threads = ['1', '2', '3', '4', '5']
i = 1
for t in threads:
    t = mythread()
    t.run()
    time.sleep(2)
    print(2*i)
    i=i+1
print("Thread Ending........")




#Q4

print("\n\nQ4. Call factorial function using thread")
'''
importing the thread modules
'''

import threading

class newThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print(fact)


n = int(input("Enter number : "))
#the factorial will be calculated through the thread
t = newThread()                        
t.start()




