def perfect_num(n):  #creating the function
    sum1 = 0          #storing thge variable
    for i in range(1, n):  #iterting through for loop
        if(n % i == 0):      #checking the reminder is zero for perfect num for all iteration
            sum1 = sum1 + i  #if it is increamenting by i
    if (sum1 == n):  #when n equals to one printing the output as a prime
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
n=int(input('enter the num'))             #user input
perfect_num=perfect_num(n)      #calling the function and assigning the object
