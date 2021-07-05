
num1=input("enter the alphabet")
if num1>"a" and num1<"z":
    num2=input("enter the number")
    if num2>"0" and num2<"9":
        num3=input("enter the special character")
        if num3=="%":
            print("its storng password")
        else:
            print("its not strong password")    
    else:
        print("its not special character ")  
else:
    print("its not number")                 