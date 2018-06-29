#Q.1 - Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.

import numpy as np
a = np.random.rand(10,1)
print(a)
print("MEAN OF ARRAY: ",np.mean(a))
print("\n\n")





#Q.2 - Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements. 

a = np.array(np.random.rand(20, 1))
print("Elements Generated : ", a)
print("Variance : ", a.var())
print("Standard Deviation : ", a.std())
print("\n\n")




#Q.3 - Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B. The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix. 

A=np.random.rand(10,20)
B=np.random.rand(20,25)
print(type(A))
print(type(B))

matrixmul=np.dot(A,B) #matrix multiplication of A and B.
print(matrixmul)

print(matrixmul.shape) #shape of new matrix

matrix=np.matrix(matrixmul) #sum of all elements of matrix.
print(matrix.sum())
print("\n\n")





#Q.4 - Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1) such that each element is the following function applied on each element of A. f(x)=1 / (1 + exp(-x)) Apply this function to each element of A and print the new array holding the value the function returns

A = np.random.rand(10,1)
def change(x):
    return 1 / (1 + np.exp(-x)) 
print(A)
print(A.shape)
updated = change(A) 
print("\nAFTER UPDATION : \n",updated)






