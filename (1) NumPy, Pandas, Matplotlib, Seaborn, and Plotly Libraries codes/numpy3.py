import numpy as np

randarr = np.random.randint(1,50,20)
print(randarr)

arr = np.arange(25)
print(arr)

# indexing 1d vector
print(arr[0])
print(randarr[1])

# slicing 1d vector
print(arr[1:4])
print(randarr[1:4])

print(arr[:4])
print(randarr[5:])

# value broadcasting
arr[1:4] = 100

slicerand = randarr[:8]
slicerand[:] = 99          # problem slicerand and randarr changes

slicerand = randarr[:10].copy()
slicerand[:] = 100 
