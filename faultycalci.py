print("enter 1st number")
num1= int(input())
print("enter 2nd number")
num2= int(input())
print("so what u weant" ,"+,*,/,-,%")
num3= input()

if num1 == 45 and num2==3 and num3== "*":
    print("555")
elif num1 ==56 and num2==9 and num3=="+":
    print("77")
elif num1== 56 and num2==6 and num3=="/":
    print("4")
elif num3 == "*":
    multiply =num1*num2
    print(multiply)
elif num3=="+":
    plus= num1+num2
    print(plus)
elif num3 == "-":
    subtrt = num2 - num1
    print(subtrt)
elif num3== "/":
    percent=num2%num1
    print(percent)
else:
    print("out of range")    
    
