from datetime import datetime

class Account:
    def __init__(self, account_id,customer_id,account_number,balance = 0.0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance
        self.transactions = [] #lists transactions done on an account
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            timestamp =datetime.now().strftime("%m/%d/%Y %H:%M:%S")   #creates transaction timestamps
            self.transactions.append(Transaction('deposit',amount,self.balance, timestamp))  #attach the deposit details to transaction list
            print(f"You have deposited: {amount}. Your account balance is: {self.balance}\n")
            return (self.balance, amount)
        else:
            raise ValueError ("Please provide a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -=amount
                timestamp =datetime.now().strftime("%m/%d/%Y %H:%M:%S")     #creates transaction timestamps
                self.transactions.append(Transaction('withdraw',amount,self.balance, timestamp))    #attach the deposit details to transaction list
                print(f"You have withdrawn: {amount}. Your account balance is: {self.balance}")
                return(self.balance, amount)
            else:
                raise ValueError ("Insufficient balance. Failed to withdraw")
        else:
            raise ValueError ("Please provide a positive amount.")

    def get_balance(self):
        print(f"Your account balance is: {self.balance}")
        return(self.balance)

class Customer:
    def __init__(self, customer_id, name, email, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

#Added class Transaction to make bank transaction details
class Transaction:  
    def __init__(self, transaction_type, amount, resulting_balance,timestamp):
        self.transaction_type = transaction_type
        self.amount = amount
        self.resulting_balance = resulting_balance
        self.timestamp = timestamp
              
class UseCase:
    def __init__(self):
        self.accounts = {}      #create a dictionary of accounts to look up account id input
        
    def create_account(self, customer_id, name, email, phone_number):
        account_number = '654321'   
        account_id = '1234'
        new_customer = Customer(customer_id, name, email, phone_number)
        new_account = Account(account_id,customer_id, account_number)
        self.accounts[account_id] = new_account     #attach the new account to dictionary
        print("Successfully created a new account!\n")
        print(f"Account #: {new_account.account_number},Account ID: {new_account.account_id}, Name: {new_customer.name}, Balance: {new_account.balance}\n")
        return new_account
    
    def make_transaction(self,account_id,amount,transaction_type):
        if account_id not in self.accounts:
            print(self.accounts)
            print(f"Account ID {account_id} not found\n")
            return
        
        account = self.accounts[account_id]     #get account values based on account id input
        
        if transaction_type not in ['deposit','withdraw']:
            raise ValueError ("Choose transaction type 'deposit' or 'withdraw'\n")  
        else:
            if transaction_type == 'deposit':
                account.deposit(amount)
            else:
                account.withdraw(amount)
            print("Transaction successful.\n")
            return
     
    def generate_account_statement(self, account_id):
        if account_id not in self.accounts:
            print(self.accounts)
            print(f"Account ID {account_id} not found\n")
            return
        
        account = self.accounts[account_id]
        
        if not account.transactions:
            print (f"No transactions found for {account_id}\n")     
            return
        
        statement = "Displaying transactions...\n"
        statement += f"Account Statement for Account ID:{account.account_id}\n"
        statement += "=" * 65 + "\n"
        statement += "     Type    |   Amount   |   Balance    |   Date & Time   \n"
        statement += "=" * 65 + "\n"      
        
        for transaction in account.transactions:
            statement += f"{transaction.transaction_type.capitalize():<12} | {transaction.amount:<10} | {transaction.resulting_balance:<12} | {transaction.timestamp}\n"    
        
        statement += "=" * 65 + "\n"
        return statement

class AccountRepository:
    def __init__(self):
        self.accounts = {}
    
    def save_account(self, account):
        self.accounts [account.account_id] = account
        print(f"Account ID: {account.account_id} saved successfully.\n")
    
    def find_account_by_id(self, account_id):
        if account_id not in self.accounts:
                print(f"Account ID {account_id} not found.\n")
                return
        
        account = self.accounts[account_id]
        
        search_result = f"Account {account_id} Found by ID. Displaying Results...\n"
        search_result += f"Account Number: {account.account_number} | Customer Number: {account.customer_id} | Balance: {account.balance}\n"
        print(search_result)
        return

    def find_accounts_by_customer_id(self, customer_id):
        customer_id_key = customer_id       
        for account in self.accounts.values():
            if account.customer_id == customer_id:
                customer_id_key = account.account_id       #Find customer id in account dictionary values
            elif customer_id not in self.accounts:
                print(f"Account ID {customer_id} not found.\n")
                return
                
        customer_account = self.accounts[customer_id_key]
           
        search_result = f"Account {customer_id_key} found by Customer ID {customer_id}. Displaying Results...\n"
        search_result += f"Account Number: {customer_account.account_number} | Customer Number: {customer_account.customer_id} | Balance: {customer_account.balance}\n"
        print(search_result)


##########################   TEST SCRIPTS  ########################

test_scenario1 = UseCase()
test_scenario2 = AccountRepository()
create_acc1 = test_scenario1.create_account('1001','Ed','ed@gmail.com','098712345678')

save_acc1 = test_scenario2.save_account(create_acc1)

acc1_deposit = test_scenario1.make_transaction('1234',5000,'deposit')
acc1_withdraw = test_scenario1.make_transaction('1234',2000,'withdraw')
acc1_withdraw2 = test_scenario1.make_transaction('1234',1000,'withdraw')

account_statement = test_scenario1.generate_account_statement('1234')
print(account_statement)

find_acc1_by_id = test_scenario2.find_account_by_id('1234')
find_acc1_by_id_fail = test_scenario2.find_account_by_id('1233')

find_acc1_by_customer_id = test_scenario2.find_accounts_by_customer_id('1001')
find_acc1_by_customer_id_fail = test_scenario2.find_accounts_by_customer_id('1003')

