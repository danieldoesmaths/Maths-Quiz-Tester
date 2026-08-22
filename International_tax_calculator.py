class TaxCalculator:

    def __init__(self, country, annual_salary):
        self.country = country
        self.annual_salary = annual_salary
        self.tax = 0

    def calculate_tax(self):

        if self.country == "UK":
            personal_allowance = 12570
            basic_rate_limit = 50270
            higher_rate_limit = 125140
            if self.annual_salary <= personal_allowance:
                self.tax = 0
                
            elif self.annual_salary <= basic_rate_limit:
                self.tax = (self.annual_salary - personal_allowance) * 0.20
                
            elif self.annual_salary <= higher_rate_limit:
                basic_rate_tax = (basic_rate_limit - personal_allowance) * 0.20
                higher_rate_tax = (self.annual_salary - basic_rate_limit) * 0.40
                self.tax = (basic_rate_tax + higher_rate_tax)

            else:
                basic_rate_tax = (basic_rate_limit - personal_allowance) * 0.20
                higher_rate_tax = (higher_rate_limit - basic_rate_limit) * 0.40
                additional_rate_tax = (self.annual_salary - higher_rate_limit) * 0.45
                self.tax = (basic_rate_tax + higher_rate_tax + additional_rate_tax)

        else:
            print("Country not supported.")

    def calculate_take_home(self):
        return self.annual_salary - self.tax

    def calculate_effective_rate(self):
        if self.annual_salary == 0:
            return 0
        return (self.tax / self.annual_salary) * 100

print("Welcome to the international tax calculator ")

country = input("\nWhich country? ")

salary = float(input("What is your annual salary? £"))

calculator = TaxCalculator(country,salary)
calculator.calculate_tax()
take_home = calculator.calculate_take_home()
effective_rate = calculator.calculate_effective_rate()

print("\n========== RESULTS ==========")
print(f"Country:            {calculator.country}")
print(f"Gross salary:       £{calculator.annual_salary:,.2f}")
print(f"Income tax:         £{calculator.tax:,.2f}")
print(f"Take-home salary:   £{take_home:,.2f}")
print(f"Effective tax rate: {effective_rate:.2f}%")
print("=============================")