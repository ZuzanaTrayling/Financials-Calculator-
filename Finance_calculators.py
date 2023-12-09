import math

#                           **** CAPSTONE PROJECT ****

# Create 2 different finantial calculator: Investment/Bond(Home loan repayment)
# Using if, elif, else statement and boolean True method throug the code
# use print() statements create empty lines

print()
# print menu 
print('''invesstment - to calculate the amount of interest you'll earn on your investment \n  
      bond - to calculate the amount you'll have to pay on a home loan \n
      enter eaither 'investment' or 'bond from the menu above to proceed:''')
print()
investment_or_bond = input(str("Please choose between 'investment'or'bond' finantial calculator:  " )).lower()
#user choose between 'investment' or 'bond'' calculater , use .lower() for case-insensitivity.

if investment_or_bond == "investment": # use boolean method, if true, assign variables (p,r,t) to question - change to int as output is number
  if True :
    p = int(input("Please input the amount you are depositing: ")) #'p', deposit amount 
    r = int(input("Please enter the interest rate(%): "))# 'r', interest rate
    t = int(input("Please input the number of years you intend to deposit: "))# 't', number of years to deposit

   # user choose between 'simple' or 'compound'interest , use .lower() for case-insensitivity.
   # use boolean method, if true,and interest variable == simple  using the interest formula and f method we print the statement. 
    interest = input(str("Please choose between 'compound' or 'simple' interest: ")).lower() 
    if interest == "simple":
      if True:
        interest = p * ( 1 + (r/100)*t) # total amount of interest formula for simple interest
        print (f"The total amount when simple interest is applied is {interest}. ")
    elif interest == "compound": #if true,and interest variable == compound  using the interest formula and f method we print the statement. 
      if True:
        interest = p * math.pow(1+(r/100),t)# total amount of interest formula for compound interest
        print (f"The total amount when compound interest is applied is {interest}")
    else:
      print ("This is an error message, please enter correct data.")# if incoretc data entered - print error message

# use boolean method, if true,  variables(p,i,n) assigned to questions - change to int as output is number
elif investment_or_bond == "bond":
  if True:
        p = int(input("Please input the present value of the house: ")) # 'p', value of the house
        i = int(input("Please enter the monthly interest rate(%): ")) # 'monthly interest'
        i_1 = (i/100)/12 # interest i devide by 100 and then by 12. 
        n = int(input("Please input the number of years you intend to deposit: ")) # 'number of year to deposit'
        investment_or_bond = (i_1 * p)/(1- (1 + i_1)**(-n)) # bond repyment formula
        print (f"The amount you repay on your home loan each month is {investment_or_bond}")# print the amount you repay 
else:
  print ("This is an error message, please enter correct data.")# if incoretc data entered - print error message
