# Taking users input
annual_salary = float(input("Enter your starting annual salary: ")) 
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#Fixed Data
portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12 
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12 
monthly_deposit = monthly_salary * portion_saved 

# Initial savings(current_savings)
# The function is used to stop algorithm 
current_savings = 0.0


months = 0  #This would be helpful to hold the number of months at the end of  the algorithm

while  current_savings < down_payment:

# problem states investment income and savings deposits occur at the end
    # of the month, so increment month before increasing current_savings
    months += 1 #Same as months = months + 1
    current_savings *= 1 + monthly_rate_of_return #Same as current_savings = current_savings * (1 + monthly_rate of return)
    current_savings += monthly_deposit #Same as current_savings = current_savings + monthly_deposit
    # problem states that semi-annual raises take effect the next month, so 
    # increase monthly_salary after increasing current_savings
    if months % 6 == 0:
        annual_salary *= 1 + semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_deposit = monthly_salary * portion_saved
    
print('Number of months:', months)