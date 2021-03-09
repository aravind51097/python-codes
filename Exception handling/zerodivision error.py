def zero(x):
    try:
        if x!=0: 
            y=x/0
        else:
            print('the answer is ',x)
    except ZeroDivisionError:
        print('The number should not be natural')



x=int(input('enter the number   '))
zero=zero(x)
