a=input("enter the name")
b=input("enter the mobile number")
c=input("enter your date of birth")
d=input("enter your gender")
e=input("enter your password")
if a=="sakshi gujarkar":
    print("your name is correct")
    if b=="1234567890":
       print("correct mobile number")
       if c=="26/07/2002":
            print("DOB is valid")
            if d=="female":
               ("ok")
               if e=="128989":
                    print("successfully create account")
               else:
                   print("something went wrong")
            else:       
                print("gender is wrong") 
        else:
           print("please check your DOB") 
    else:
       print("mobile number is wrong") 
else:  
    print("your name is not match")                    
