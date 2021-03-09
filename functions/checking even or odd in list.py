def evenlist(num):
    
    for i in num:
        if i%2==0:
            print('even',i)
            i+=1

num=[1,2,3,3,3,3,4,5]

evenlist(num)
