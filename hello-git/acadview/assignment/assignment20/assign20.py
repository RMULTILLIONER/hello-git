#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same. 

import numpy
import pandas
import csv

name   =  ['RAVINDER', 'RAVI']
age    =  [21, 21]
number =  [9999988888, 8888899999]
email  =  ['ravinder21@gmail.com', 'ravi21@gmail.com']
panda_dataframe = pandas.DataFrame({"Name" : name, "Age" : age, "Number" : number, "Email" : email})

print(panda_dataframe.dtypes)
print()
print(panda_dataframe)


#Import the data and print the following :
# a.) First 5 rows of Dataframe
# b.) First 10 rows of the Dataframe
# c.) find basic statistics on the particular dataset.
# d.) Find the last 5 rows of the dataframe
# e.) Extract the 2nd column and find basic statistics on it.

import pandas as pd

df1=pd.read_csv('/Home/Documents/Python/PycharmProjects/assignment/venv/weather.csv')
print(df1)
print(df1.head(5))
print(df1.head(10))
print(df1.describe())
print((df1.tail()))
print(df1['Location'].describe())



