num=int(input('emnter number>>>>'))
for i in range(2,num):
    if num%i==0:
        print('not prime')
        break
else:
        print('prime')
