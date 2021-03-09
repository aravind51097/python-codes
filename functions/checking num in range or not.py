def rangein(num): #defining function name

      #getting the user ip
   
    while num>100:            #setting the range value
       
        print('not in range try again>>>',num)
        num=int(input('enter the num again..'))  #looping the input untill the condition is satishfied
        
    else:
        print('num in range>>',num)   #if in range printing the value

num=int(input('enter you num>>'))
range1=rangein(num)          #calling the function
