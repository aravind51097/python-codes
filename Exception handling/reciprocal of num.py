def reciprocal(x):
    
    try:
        if x%2!=0:
            raise ValueError
        
        if x%2==0:
            recip=(1/x)
            print('the reciprocalof num is  ',recip)
    except ValueError as e:
      
            print('please enter even nums')
x=int(input('enter the number for reciprocation'))
reciprocal=reciprocal(x)
