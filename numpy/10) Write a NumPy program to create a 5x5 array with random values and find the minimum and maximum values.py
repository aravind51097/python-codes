import numpy as np
arr=np.random.randint(1,50,size=(5,5))
print('array is \n',arr)
print('max is \n',arr.max())
print('minimum is \n',arr.min())
print('sum of the elememts is \t',arr.sum())
a1=arr.sum()-arr.min()*arr.max()
print(a1)
