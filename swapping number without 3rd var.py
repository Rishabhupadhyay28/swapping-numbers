#swapping number without using 3rd variable

a=10 
b=20
print("the initial value of a is:",a)
print("the initial value of b is:",b)

a=a+b 
b=a-b 
a=a-b
print(" value of a after swapping : ",a)
print(" value of b after swapping :",b)