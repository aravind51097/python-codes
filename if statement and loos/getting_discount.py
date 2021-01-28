count=float(input('enter quantity>>'))  # getting user quantity
cost=100                                #COST PER count
print('cost per count is >>>100rupess') #coveying cost per quantity
if count>=10:                           #initializing the discount condition 
    discount=(count*cost)/10             #discount as per count
    print('your cost is  >>\n',count*cost)  #cost before discount
    print('your discount is 10% of total cost >>\n',discount ,'\n total cost is after discount>>\n',(count*cost-discount))#printing discount and cost after discount
    print('thank you visit again')  #greeting the customer
    
else:
    print('your total cost is \n',cost*count) #cost without discount
    print('no discount for less then 10 count>> \n',count)   #coveying dicount eligilblity
    print('thank you visit again') #greeting customer
