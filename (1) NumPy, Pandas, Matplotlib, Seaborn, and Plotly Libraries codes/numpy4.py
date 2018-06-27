import numpy as np

randmat = np.random.rand(5,5)    # 2d matrix

# indexing 2d matrix
print(randmat[0])
print(randmat[0][0])
print(randmat[0,0])

# slicing 2d matrix
print(randmat[:2,:])  # [from row : to row, from col:to col]

res = randmat>0.2  # mask
print(res)

condittionsel = randmat[res]
print(condittionsel)

# res = randmat[randmat>0.2]