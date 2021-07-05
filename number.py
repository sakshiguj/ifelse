a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b>c:
    print(a,b,"is greater")
elif b>c>a:    
    print(b,c, "is greater")
elif c>a>b:
    print(b,c, "is greater")
elif b>a>c:
    print(b,a,"is greater") 
elif a>c>b:
    print(a,c,"is greater") 
elif c>b>a:
    print(c,b,"is greater")              
else:
    print("invalid")        
