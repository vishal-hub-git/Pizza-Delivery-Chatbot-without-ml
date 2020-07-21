import re
import pandas as pd
pizza_data= pd.read_excel("Book1.xlsx")

print("\n"+"HI,This is YUM_PIZZA shop. We have best pizza's in coimbatore. So,order and be happy. Welcome!!!!")
print("Press anything to start your order.")
input("User : ")
print("May I know your name please sir")
name=input("User : ")

print("Type YES to confirm that you are here to order pizza or type NO ")

user_response= input("User : ")

sd=re.match(r'yes',user_response.lower())



if sd != None:
    print("Thanks for your response Mr/Mrs."+name+ ". So Veg or Non-veg!!!!!! ")
    user_response= input("User : ")
    er=re.match(r'non',user_response.lower()) 
    if er != None:
        def non_veg():
            print("We are having 5 varities of non-veg pizza, list's are below.")
            print("Choose any one Mr/Mrs."+name)
            print(pizza_data[["non_veg_pizza","Price"]])
            er=pizza_data[["non_veg_pizza","Price"]]
            print("Eg : type 0 to order CHICKEN_SAUSAGE")
            user=int(input("User : "))
            print("Thanks for choosing ")
            print( er.loc[[user]])
            fv=int(er.loc[user][1])
            print("Price of your order is Rs. "+str(fv))
            print("Enter your mode of  payment : Cash on delivery or card")
            print("Exciting offers are waiting for those who pay in card")
            delivery=(input("User : "))
            sd=re.match(r'card',delivery)
            if sd ==None:
                 print("Enter the coupoun code, if you want offer or type no")
                 code=input("Coupoun Code : ")
                 ms=re.match(r'no',code)
                 if ms==None:
                     if code=='25percentoff':
                       print("Your code is correct. 25 percent offer is provided for you.")
                       fv=fv-fv*0.25
                       print("You should pay Rs. "+str(fv))
                     else:
                        print("Your code is wrong. Try with code next time")
                 else:
                     print("Ok,then continue with address")
                 print("Enter your address please sir")
                
                 address=input("User : ")
                 print("Your order will be delivered on the address"+"\n "+address+"\n"+"Thanks for your order. Visit again Mr./Mrs."+name)
                
            else:
                
                 print("Enter the coupoun code, if you want offer or type no")
                 code=input("Coupoun Code : ")
                 md=re.match(r'no',code)
                 if md==None:
                     if code=='50percentoff':
                       print("Your code is correct. 50 percent offer is provided for you.")
                       fv=fv-fv*0.25
                       print("You should pay Rs. "+str(fv))
                     else:
                        print("Your code is wrong. Try with code next time")
                 else:
                     print("Ok then continue with payment")
                 num=input("Enter your card number: ")
                 p=int(input("Enter the OTP sent to you : "))
                 if p==1959:      
                  print("\n"+"Your money has been received ")
                  print("\n"+"Enter your address please sir")
                  address=input("User : ")
                  print(" ")
                  print("your order will be delivered on the address"+" \n"+address+"\n"+"Thanks for your order. Visit again Mr./Mrs."+name)
                 else:
                  print("Your OTP is wrong . Order again from first") 
        we=non_veg()    
             
    else:     
        
        def veg():
            
            print("We are having 5 varities of non-veg pizza, list's are below.")
            print("Choose any one Mr/Mrs."+name)
            print(pizza_data[["veg_pizza","Price"]])
            er=pizza_data[["veg_pizza","Price"]]
            print("Eg : type 0 to order MARGHERITA")
            
            user=int(input("User : "))
            print("Thanks for choosing ")
            print( er.loc[[user]])
            fv=int(er.loc[user][1])
            print("Price of your order is Rs. "+str(fv))
            print("Enter your mode of  payment : Cash on delivery or card")
            delivery=(input("User : "))
            sd=re.match(r'card',delivery)
            if sd ==None:
                 print("Enter the coupoun code, if you want offer or type no")
                 code=input("Coupoun Code : ")
                 mv=re.match(r'no',code)
                 if mv==None:
                     if code=='25percentoff':
                       print("Your code is correct. 25 percent offer is provided for you.")
                       fv=fv-fv*0.25
                       print("You should pay Rs. "+str(fv))
                     else:
                        print("Your code is wrong. Try with code next time")
                 else:
                     print("Ok,then continue with address")
                 print("Enter your address please sir")
                 address=input("User : ")
                 print("Your order will be delivered on the address" +"\n "+address+"\n"+"Thanks for your order. Visit again Mr./Mrs."+name)
                
            else:
                
                 print("Enter the coupoun code, if you want offer or type no")
                 code=input("Coupoun Code : ")
                 md=re.match(r'no',code)
                 if md==None:
                     if code=='50percentoff':
                       print("Your code is correct. 50 percent offer is provided for you.")
                       fv=fv-fv*0.5
                       print("You should pay Rs. "+str(fv))
                     else:
                        print("Your code is wrong. Try with code next time")
                 else:
                     print("Ok then continue with payment")
                 num=input("Enter your card number : ")
                
                 p=int(input("Enter the OTP sent to you : "))
                 if p==1959:
                  print("\n"+"Your money has been received ")
                  print("\n"+"Enter your address please sir")
                  address=input("User : ")
                  print(" ")
                  print("your order will be delivered on the address"+" \n"+address+"\n"+"Thanks for your order. Visit again Mr./Mrs."+name)
                 else:
                  print("Your OTP is wrong . Order again from first") 
                
              
          
        w=veg()
else:
      print("Thank you for visiting the page")
        