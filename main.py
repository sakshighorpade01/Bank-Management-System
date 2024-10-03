from register import *
from bank import *

status = False


print("Welcome to Banking Project")
while True:
    try:
        register = int(input("1.SignUP\n"
                             "2.SignIN"))
        if register == 1 or register == 2:
            if register== 1:
                SignUp()
            if register== 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please enter valid input from options")
    
    except ValueError:
        print("Invalid Input.Try Again with Numbers") 

account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")

while status:
    print(f"Welcome {user.capitalize()} Choose Your banking service ")
    try:
        facility = int(input("1.Balance Enquiry\n"
                             "2.Cash Deposit\n"
                             "3.Cash Withdraw\n"
                             "4.Fund Tansfer\n"
                             ))
        if facility >= 1 or facility <= 4:
            if facility== 1:
                bobj = Bank(user,account_number[0][0])
                bobj.balanceenquiry( )

            elif facility== 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit :"))
                        bobj = Bank(user,account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter valid input i.e number")
                        continue

            elif facility== 3:
                try:
                    amount = int(input("Enter Amount to Withdraw"))
                    bobj = Bank(user,account_number[0][0])
                    bobj.withdraw(amount)
                    mydb.commit()
                    status = False
                except ValueError:
                        print("Enter valid input i.e number")
                        continue
                
            elif facility== 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number :"))
                        amount = int(input("Enter money to transfer :"))
                        bobj = Bank(user,account_number[0][0])
                        bobj.fundtransfer(receive,amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter Valid Account Number")
                        continue

                                                
               
        else:
            print("Please enter valid input from options")
            continue
    
    except ValueError:
        print("Invalid Input.Try Again with Numbers") 
        continue