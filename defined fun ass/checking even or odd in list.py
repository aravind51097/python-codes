def evenlist(num):
    
    for i in num:
        if i%2==0:
            print('even')
            i+=1
        else:
            print('odd')
num=[1,2,3,3,3,3,4,5]

evenlist(num)
