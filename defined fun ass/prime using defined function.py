def prime(num):                         # defining a function called prime
   
    for i in range(2,num):              # iterting through the list for checking
        if num%i==0:                    # condition for not a prime
            print('not a prime>>',num)  # printing the output
            break                       # exiting from loop after the loop satishfied
    else:              
        print('prime>>',num)




num=int(input('enter the number>>>>'))  # getting user input

prime=prime(num)                         # calling the function and assigning it to the object called prime
