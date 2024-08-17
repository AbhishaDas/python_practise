"""Income tax is calculated as per the following table 
Annual Income
Tax percentage
Up to 2.5 Lakhs 
No Tax
Above 2.5 Lakhs to 5 Lakhs
5%
Above 5 Lakhs to 10 Lakhs
20%
Above 10 Lakhs to 50 Lakhs
30%

Write a program to find out the income tax amount of a person.
Program should accept annual income of a person
Output the amount of tax he has to pay

Eg 1:
Enter the annual income
495000
Income tax amount = 24750.00

Eg 2:
Enter the annual income
500000
Income tax amount = 25000.00"""

def calculate_incometax(annual_income):
    
    if annual_income<=250000:
        print("No Tax")
        return 0

    elif annual_income<=500000:
        result=annual_income * 0.05
        return result
    
    elif annual_income<=1000000:
        result=annual_income * 0.20
        return result
    
    elif annual_income<=5000000:
        result=annual_income * 0.30
        return result
    

annual_income=float(input("Enter the annual income: "))
income_tax=calculate_incometax(annual_income)
print("Income tax amount= ",income_tax)