number =['the',1,5,6,7,9,4,6]
sum =0
count =0
for i in number:
    print(i)
    try:
        sum = sum+ i
        count +=1
    except:
        print("no")

print(f"sum of list element ={sum}, count of element={count}")
print(f"average of element={(sum/count)}")