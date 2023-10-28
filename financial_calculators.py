#For this task I am asked to create a program that allows the user to access 2 different financial calculators (Investment and home loan repayment calculator.)
import math
print("Step 1:")
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

financial_calculator = str(input("Enter either 'Investment' or 'Bond' from the menu above to proceed."))

if financial_calculator == "INVESTMENT" or financial_calculator == "investment" or financial_calculator == "Investment":
 print("valid entry.")

elif financial_calculator == "BOND" or financial_calculator == "bond" or financial_calculator == "Bond":
 print("Valid entry.")

else:  print("Invalid entry.")

print("Step 2:")
#So now if user has selected investment, user will have to input  the amount of money that they are depositing, interest rate as a number, number of years they plan on investing and then user will input simple or compound.
if financial_calculator == "Investment" or financial_calculator == "investment" or financial_calculator == "INVESTMENT":
                    deposit = int(input("Enter amount of money that you are depositing: R "))
                    interest_rate =int(input("Enter interest rate (leave out '%'): "))
                    rate = interest_rate / 100
                    no_years = int(input("Enter amount of years you plan on investing: "))
                    interest = str(input("Enter 'simple' or 'compound': "))

                    if interest == 'simple':
                        simple_interest = deposit *(1 + rate * no_years)
                        print(simple_interest)

                    else:
                        compound_interest = deposit * math.pow((1 + rate), no_years)
                        print(compound_interest) 

#Now that the calculation for investment is done, I will now move onto bond.
#I shall ask user to input values needed to do the calculations if they have selected bond.
elif financial_calculator == "bond" or financial_calculator == "BOND" or financial_calculator == "Bond":
                present_value = int(input("Enter value of house: "))
                rate_interest = int(input("Enter interest(Enter number): "))
                r = (rate_interest / 100) / 12
                no_months = int(input("Enter number of months that you plan to repay bond: "))

                repayment = (r * present_value) / (1 - (1 + r) **(-no_months))
                print(repayment)

else:
        print("Wrong entry.")

    