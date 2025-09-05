#example of lambda function 
toDollar = lambda rupees : rupees/86
getInterest = lambda amount,rate,year : (amount*rate*year) / 100
getMax = lambda num1,num2 : num1>num2 
print(toDollar(1000))
print(getInterest(1000,10,2))
print(getMax(10,20)) #false
print(getMax(100,50)) #true
