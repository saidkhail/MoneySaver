# This project will figure out how much I need to save to reach my goal


print("------Welcome to the Money Saving Calculator-----")
print("\t\t\t")

years = int(input("Please let us know how many years are you willing to save : "))
print("\t")
saving = int(input("How much money do you have in your savings:  "))
print("\t")
income = int(input("How much do you make per month:  "))
print("\t")
print("Please display below how much you spend per month :  ")
print("\t")
expenditure = int(input("Expenditure : "))
print("\t")
discretional_spending = int(input("Discretional Spending : "))
print("\t")
calculation = int((expenditure + discretional_spending))
print(calculation)

print("-------------------------------------------------------------------")

formula = (income - calculation )
float_number = float(formula) # Converting it to a float
formatted_number = "{:.2f}".format(float_number) # formatting the number to 2 decimal places
print(formatted_number)

savings  = formula * 12
final_amount = 0

for i in range(0,years):
    if final_amount == 0:
        final_amount = saving


final_amount = (final_amount + savings)
formatted_number = "{:.2f}".format(final_amount)
print(final_amount)
print("There will be no interest as its forbidden")
print("-------------------------------------------------------------------")
print("This is how much you have saved:") + float(final_amount)
