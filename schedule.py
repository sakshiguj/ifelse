time=input("enter the time") 
if time=="6.00am to 7.00am":   
    print("morning exercise time")  
    if time=="7.00am to 8.30am":  
       print("breakfast")   
       if time=="8.30am to 9.30am":
            print("english activity")    
            if time=="9.30 to 1.30":
                print("coding time")    
                if time=="1.00pm to 2.30pm":
                    print("lunch break")  
                    if time=="2.30pm to 4.00pm":
                        print("culture activity") 
                        if time=="4.00pm to 9.00pm":
                            print("study time")
                            if time=="9.00pm to 10.00pm":
                                print("dinner time")
                            else:
                                print("not")
                        else:
                            print("not") 
                    else:
                        print("not")    
                else:
                    print("not")
            else:
                print("not")  
       else:
            print("not")   
    else:
        print("not")
else:
    print("not")                                                                             