num1=int(input("input the first number :"))
b="+"
cal=("+","-","/","*","**","%")
op=input("input your operator :")
num2=int(input("input the second number :"))
b=op
if op=="+":
    c=num1+num2
    print(c)
elif op=="-":
    c=num1-num2
    print(c)
elif op=="*":
    c=num1*num2
    print(c)
elif op=="/":
    if num2==0:
        print("input another number")
    else:
    c=num1/num2
    print(c)
elif op=="**":
    c=num1**num2
    print(c)
elif op=="%":
    c=num1%num2
    print(f"{num1}/{num2}={num1/num2} remainder {num1%num2}")


