class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
            
    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
        
    def print_holder_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print(f"Balance: ${self.balance}\n")   

accno=int(input("Enter Account Number:"))
accname=input("Enter account holder name:")
balance=int(input("Enter Balance in the account:"))
s = BankAccount(accno,balance,accname)
while(True):
    print(".........Menu..........")
    k = int(input("1.Account holder details\n2.Balance enquiry\n3.Deposit\n4.Withdraw\n5.exit\nEnter your option:"))
    if(k==1):
        print("Account Holder Details:")
        s.print_holder_details()
    elif (k == 2):
        s.check_balance()
    elif (k == 3):
        n=int(input("Enter amount for deposit:"))
        s.deposit(n)
    elif (k == 4):
        n1= int(input("Enter amount for withdrawl:"))
        s.withdraw(n1)
    else:
        exit()
