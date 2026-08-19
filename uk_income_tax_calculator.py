def calculate_tax(annual_salary):

    personal_allowance = 12570
    basic_rate_limit = 50270
    higher_rate_limit = 125140

    if annual_salary <= personal_allowance:
        tax = 0

    elif annual_salary <= basic_rate_limit:
        basic_rate_tax = (annual_salary - personal_allowance) * 0.20
        tax = basic_rate_tax

    elif annual_salary <= higher_rate_limit:
        basic_rate_tax = (basic_rate_limit - personal_allowance) * 0.20
        higher_rate_tax = (annual_salary - basic_rate_limit) * 0.40
        tax = basic_rate_tax + higher_rate_tax
 
    else:
        basic_rate_tax = (basic_rate_limit - personal_allowance) * 0.20
        higher_rate_tax = (higher_rate_limit - basic_rate_limit) * 0.40
        additional_rate_tax = (annual_salary - higher_rate_limit) * 0.45

        tax = ( basic_rate_tax + higher_rate_tax + additional_rate_tax)
    return tax


print("Welcome to the UK Income Tax Calculator!")

annual_salary = int(input("\nWhat is your annual salary? £"))

tax = calculate_tax(annual_salary)

take_home_salary = annual_salary - tax

print(f"\nGross salary: £{annual_salary:,.2f}")
print(f"Income tax: £{tax:,.2f}")
print(f"Take-home salary: £{take_home_salary:,.2f}")
