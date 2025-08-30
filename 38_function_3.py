# find bmi
def getbmi(weight,height):
    if weight==0 and height==0:
        print("invalid input")
    else:
        bmi = weight / (height ** 2)
        print(bmi)
        if bmi >=60:
            print("obese")
        elif bmi >=40 and bmi<60:
            print("overweight")

w = float(input("Enter your weight"))
h = float(input("Enter your height"))


getbmi(w,h)