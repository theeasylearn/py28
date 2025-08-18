# write a program to findout & display profit or loss amount from product purcharse and sale price 
# if sales price > purcharse price profit 
# if sales price < purcharse price loss 
'''
    steps 
    1) take 2 input purcharse price and sales price & store in variable 
    2) findout difference between sales price and purcharse price and store in variable
    3) if differnce is > 0 then display message profit with difference variable 
    4) if difference is < 0 then display message loss with difference variable 
'''
purchase_price = int(input("Enter product purcharse price"))
sales_price = int(input("Enter product sales price"))
difference = sales_price - purchase_price
if difference>0:
    print("profit is ",difference)
    print("you have done good job")
    print("you can become business man")

if difference<0:
    print("loss is",difference)
    print("you need to develop business skill")
    print("or you can do job")

print("Good bye...")
