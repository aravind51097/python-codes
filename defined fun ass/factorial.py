def fac(a):
    count=1
    i=1
    while i<=a:
        count=count*i
        i+=1
    print(count)
        
a=int(input('enter the number'))

fac=fac(a)
