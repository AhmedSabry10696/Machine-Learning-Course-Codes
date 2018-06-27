import numpy as np

# generate random num bet 2 nums 
x = np.linspace(0,10,100) 

# uniform distrbution generate random num from 0:1  "vector"
y = np.random.rand(5)

# normal "gaussian" distrbution generate num from -v:+v  "vector"
z = np.random.randn(5)

# uniform distrbution generate random num from 0:1  "matrix"
y1 = np.random.rand(5,3)

# normal "gaussian" distrbution generate num from -v:+v  "matrix"
z1 = np.random.randn(5,3)

# identity matrix
i = np.eye(5)

randarr = np.random.randint(1,50,20)
print(randarr)

arr = np.arange(25)
print(arr)

arr2d = np.reshape(arr,(5,5))   # 5*5 =25
print(arr2d)  

maximum = np.max(randarr)
print(maximum) 

locmax = np.argmax(randarr)
print(locmax)

minimum = np.min(randarr)
print(minimum)

locmin = np.argmin(randarr)
print(locmin)

print(np.shape(arr))
print(np.shape(arr2d))

print(arr.dtype)
print(randarr.dtype)
