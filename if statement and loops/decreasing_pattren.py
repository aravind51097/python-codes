for i in range(5):
    if i%2==0:
        for j in range(i+1):
            print('*',end='')
        print()
for k in range(5):
    if k%2==0:
        for k1 in range(5-k):
            print('*',end='')
        print()
