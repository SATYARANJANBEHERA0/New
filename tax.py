def calculate_tax(income):
    if income <= 250000:
        tax = 0
    elif 250000 < income <= 500000:
        tax = (income - 250000) * 0.05
    elif 500000 < income <= 1000000:
        tax = (income - 500000) * 0.2 + 12500
    else:
        tax = (income - 1000000) * 0.3 + 112500
    
    return tax
# example usage
income = int(input("Enter your income:"))
tax = calculate_tax(income)
print(" income tax =", tax)


