def maximum(a, b):
    if a > b:
        return a
    else:
        return b

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

result = maximum(num1, num2)

print("the greater number is=",result)