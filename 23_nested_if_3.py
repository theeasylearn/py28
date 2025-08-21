'''
    write a program to calculate & display gross annual income, tax and net income from monthly given income as per below income tax rule 
    annual income                           Tax Rate
    Above Rs. 24,00,001	                    30%
    From Rs. 20,00,001 to Rs. 24,00,000	    25%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,001 to Rs. 16,00,000	    15%
    below 12,00,000                          0%
    steps
    1) accept monthly income 
    1.2) if montly income is <0 then display message invalid input 
    otherwise
    2) calculate gross income 
        gross_income = monthly income * 12 
    3) decide tax rate 
        if gross_income > 2400001 then store 30 into tax_rate 
        if gross_income > 2000001 then store 25 into tax_rate 
        if gross_income > 1600001 then store 20 into tax_rate 
        if gross_income > 1200001 then store 15 into tax_rate 
        otherwise tax rate will be 0%
    4) calculate tax 
        tax = (gross_income * tax) / 100;    
    5) calculate net income 
        net_income = gross_income - tax 
    6) display gross_income, tax, net_income
'''
monthly_income = int(input("Enter monthly income"))
if monthly_income<0:
    print("invalid monthly income")
else:
    gross_income = monthly_income * 12 
    if gross_income>2400001:
        tax = 30 
    elif gross_income>2000001:
        tax = 25 
    elif gross_income>1600001:
        tax = 20 
    elif gross_income>1200001:
        tax = 15
    else:
        tax = 0 

    tax = (gross_income * tax) / 100
    net_income = gross_income - tax 
    print(f"gross income = {gross_income} tax = {tax} net income = {net_income} ")