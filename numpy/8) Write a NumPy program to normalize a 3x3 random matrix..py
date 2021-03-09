import numpy as np
arr=np.random.random((3,3))
print('before normaliztion \n ',arr)
arr2=((arr-arr.min())/(arr.max()-arr.min()))

print('after normalization \n',arr2)
