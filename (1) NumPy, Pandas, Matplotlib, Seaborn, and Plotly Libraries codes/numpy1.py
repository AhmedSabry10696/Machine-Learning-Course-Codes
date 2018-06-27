import numpy as np

# create vector
num = [4,5,6,7,8]
print(type(num))
numvec = np.array(num)
print(type(numvec))
  
# create matrix
numlist = [[2,3],[4,5]]
print(type(numlist))
nummat = np.array(numlist)
print(type(nummat))

print(len(num))
print(len(num))

print(len(numlist))
print(len(nummat))

print(nummat.size)

x = np.arange(0,10,1)           # creare vector
n1,n2 = np.mgrid[0:5,0:5]       # create matrix
# n1 -> matrix   n2 -> transpose of n1
# transpose: row -> col
n1,n2 = np.mgrid[0:10,0:5];
# n1 -> every row changes from 0 to 9
# n2 -> every col changes from 0 to 4

z = np.zeros(6)
o = np.ones(6)

zm = np.zeros((6,3))
om = np.ones((6,3))