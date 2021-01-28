a=float(input('enter 1st num \n'))
b=float(input('enter 2nd num \n'))
c=float(input('enter 3rd num \n'))
if a>b and a>c:
    print(a,' A greater')
elif b>a and b>c:
    print(b,'B greater')
elif c>a and c>b:
    print(c,'C greater')

else:
    print('All are equal')
