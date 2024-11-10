# IRPEF 2022 Income tax rate
# from 0 up to 15.000 euros 23%
# from 15.001 up to 28.000 euros 25%
# from 28.001 up to 50.000 euros 35%
# above 50.000 euros 43%

# IRPEF 2024 Income tax rate
# from 0 up to 28.000 euros 23%
# from 28.001 up to 50.000 euros 35%
# above 50.000 euros 43%

# Ignore the no-tax area.
# Tabulate the due tax amount for each of the two years.
# Compute the tax difference for the same income in the two years.

income_amount = int(input("Enter income: "))

def irpef_2022(income):
    if(0 <= income <= 15000):
        tax_2022 = income / 100 * 23
    elif(15001 <= income <= 28000):
        tax_2022 = income / 100 * 25
    elif(28001 <= income <= 50000):
        tax_2022 = income / 100 * 35
    elif(50001 <= income):
        tax_2022 = income / 100 * 43
    print(f"The due tax amount for 2022 is €{tax_2022}")
    return tax_2022

def irpef_2024(income):
    if(0 <= income <= 28000):
        tax_2024 = income / 100 * 23
    elif(28001 <= income <= 50000):
        tax_2024 = income / 100 * 35
    elif(50001 <= income):
        tax_2024 = income / 100 * 43
    print(f"The due tax amount for 2024 is €{tax_2024}")
    return tax_2024

def tax_difference(tax_2022, tax_2024):
    dif = tax_2024 - tax_2022
    print(f"The tax difference from 2022 to 2024 is €{dif}")

tax_2022 = irpef_2022(income_amount)
tax_2024 = irpef_2024(income_amount)
tax_difference(tax_2022, tax_2024)
    
