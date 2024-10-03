#User Registration SIgnIn SignUp
from database import *
from customer import *
from bank import Bank
import random

def SignUp():
    username = input("Create username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("Username already exists")
        SignUp()
    else:
        print("Username is available Please Proceed")
        password = input("Enter your password :")
        name = input("Enter your name :")
        age = input("Enter your age :")
        city = input("Enter your city :")
        while True:
            account_number = random.randint(10000000,99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if(temp):
                continue
            else:
                print("Your account number :",account_number)
                break

    cobj = Customer(username,password,name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username,account_number)
    bobj.create_transaction_table()


def SignIn():
    username = input("Enter username :")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter password :")
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            #print(temp[0][0])
            if temp[0][0] == password:
                print("SignIn successfully")
                return username
            else:
                print("Wrong password try again")
                continue

    else:
        print("Enter correct username :")
        SignIn()

    
