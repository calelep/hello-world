#Declare and add value of 0 to variables.

monthly_amount = 0

loan = 0

interest_rate = 0

number_of_payments = 0

loan_duration_years = 0

#Obtain values from user's inputs.

str_loan = input('Enter Loan Amount you intent to borrow: ')

str_interest_rate = input('Enter Interest Rate:  (i,e. for 5% enter .05)')

str_loan_duration_years = input('Enter desired number of years to pay off loan: ')

#Convert string values into floating numbers

loan = float(str_loan)

interest_rate = float(str_interest_rate)

loan_duration_years = float(str_loan_duration_years)

#Payments are once per Month, so number_of_payments is number of years for loan * 12

number_of_payments = loan_duration_years * 12

#Obtain monthly payments based on formula M = L[i(1+i)n] / [(1+i)n+1]
# M = monthly_amount
# L = loan
# i = interest_rate
# n = number_of_payments
monthly_amount = loan * interest_rate * (1 + interest_rate) * number_of_payments\
    /((1 + interest_rate) * number_of_payments - 1)

#Provide results to the user
print("Your monthly payment will be " + str(monthly_amount))
