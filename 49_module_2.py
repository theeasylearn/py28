import currency
n = float(input("Enter the rupee"))
doller = currency.toDollar(n)
euro = currency.toEuro(n)
pound = currency.toPound(n)

print(f'rupees are {n},doller ={doller},euro ={euro},pound={pound}')