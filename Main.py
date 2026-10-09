import mysql.connector as c
import time
import sys
db=c.connect(host='localhost',user='root',password='password')
obj=db.cursor()
obj.execute("CREATE DATABASE IF NOT EXISTS bank_management")
obj.execute("USE bank_management")
obj.execute("CREATE TABLE IF NOT EXISTS accounts(acc_name varchar(50),acc_no int primary key,password varchar(50),balance int)")
db.commit()

def create():
    print("\n--- CREATE NEW ACCOUNT ---") 
    accname=input('Enter Account holder name:').capitalize()
    acc=int(input('Enter Account Number:'))
    pas=int(input('Enter your Account Password:'))
    bal=int(0)
    com="insert into accounts values('{}',{},{},{})".format(accname,acc,pas,bal)
    try:
        obj.execute(com)
        db.commit()
        print("account '{}'created succesfully".format(acc))
    except Exception:
        print('Could Not Create Your Account')

def balance():
    print("\n--- Login To View YOur Balance ---")
    login_acc = int(input("Enter Account Number: "))
    login_pas = input("Enter Password: ")
    com = "SELECT acc_name, balance FROM accounts WHERE acc_no = {} AND password = '{}'".format(login_acc, login_pas)
    try:
        obj.execute(com)
        record = obj.fetchone() 
        if record != None:
            print("\nWelcome, {}!".format(record[0]))
            print("Your current balance is: ₹{}".format(record[1]))
        else:
            print("\nInvalid Account Number or Password.")
    except Exception:
        print("Could not fetch Your Balance")

def deposit():
    print("\n--- DEPOSIT ---")
    login_acc = int(input("Enter Account Number: "))
    login_pas = input("Enter Password: ")
    amt = int(input("Enter amount to deposit: "))
    query = "SELECT balance FROM accounts WHERE acc_no = {} AND password = '{}'".format(login_acc, login_pas)
    try:
        obj.execute(query)
        record = obj.fetchone()
        if record != None:
            update_cmd = "UPDATE accounts SET balance = balance + {} WHERE acc_no = {}".format(amt, login_acc)
            obj.execute(update_cmd)
            db.commit()
            print("\nSuccessfully deposited! New balance: ₹{}".format(record[0] + amt))
        else:
            print("\nInvalid Account Number or Password.")
    except Exception:
        print("Could not deposit Your Money")

def withdraw():
    print("\n--- WITHDRAW ---")
    login_acc = int(input("Enter Account Number: "))
    login_pas = input("Enter Password: ")
    amt = int(input("Enter amount to withdraw: "))
    query = "SELECT balance FROM accounts WHERE acc_no = {} AND password = '{}'".format(login_acc, login_pas)
    try:
        obj.execute(query)
        record = obj.fetchone()
        if record != None:
            if record[0] >= amt:
                update_q = "UPDATE accounts SET balance = balance - {} WHERE acc_no = {}".format(amt, login_acc)
                obj.execute(update_q)
                db.commit()
                print("\nSuccessfully withdrew! New balance: ₹{}".format(record[0] - amt))
            else:
                print("\nInsufficient funds. Your balance is: ₹{}".format(record[0]))
        else:
            print("\nInvalid Account Number or Password.")
    except Exception:
        print("Could not withdraw Your Money")


while True:          
    print("\n=== BANK MANAGEMENT SYSTEM ===")
    print("1. Create account")
    print("2. View balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    choice=int(input('Enter Your Choice:'))
    if choice==1:
        create()

    elif choice==2:
        balance()
        time.sleep(2)

    elif choice==3:
        deposit()

    elif choice==4:
        withdraw()

    elif choice==5:
        print('Thank You For Banking With Us! ')
        break

    elif choice==67:
            obj.execute("select * from accounts")
            for i in obj:
                print(i)
    else:
        print('Invalid Choice! Please Try Again.')
    
sys.exit()





