# PDAX-Take-Home-Exam

# Objective
Your task is to implement a simplified version of the banking system application based on clean
architecture. You need to create the necessary classes and methods following the clean
architecture principles.

# Process
I approached the construction of the program sequentially as it was given in the requirements. 
Should there be any functions in the following numbers that would interact with previously built classes,
I implement the changes on a duplicate workspace to easily track errors of my modifications. 

First, I created a class Account to create instances of bank accounts with attributes of account id, customer id,
account_number, and account balance. Methods for manipulating the account balance such as deposit and withdraw were
added by taking in an amount and adding or subtracting it respectively to the current balance. Users can also view the
balance of an account with the added get_balance function. Customers also had a separate class with attributes of 
customer id, name, email, and phone number.

A class for use cases was made for three main functions. In creating an account, I used the method's input to supply 
the attribute details of customer and account. For testing purposes, I set the account number and account id to a
constant value but this can be replaced by a random number generator from "random" package. The generated account was
saved in a dictionary which can be looked up for making transactions and getting account statements. Running the code up
to this point gives you the following output:
![image](https://github.com/user-attachments/assets/5595f59b-c312-446f-92f9-7576616125fb)
![image](https://github.com/user-attachments/assets/274e056c-d8c3-4964-a003-22ac4bb28f37)

For making transactions, you have to specify the transaction type along with the amount and account ID to execute. Account ID
was used as look up value in the dictionary of accounts to pull up the particular account. Should users input a non-existent
account, it will be graciously met with a value error that the transaction will fail. Transaction types of depositing and
withdrawing are only accepted so I made a list of these two words to compare with the user's input. These transactions 
utilized the existing methods in the accounts class for deposit and withdraw. Running the code upto this point gives you 
the following output:
![image](https://github.com/user-attachments/assets/ab5421fb-f4f7-4760-a2da-4174a1d1f97e)
![image](https://github.com/user-attachments/assets/a38d98b4-b363-4a73-a3cc-c15957739fad)

Now that the account has some transactions, we need to log it to the account for generating account statements. I created a
class for transaction which has the attributes of transaction type, amount, resulting balance, and timestamp of said transaction.
I added the last attribute by using datetime package and incorporating it on the deposit and withdraw function. I added a transaction list
under accounts to log it. The method for generating account statements was fairly similar in making transactions without the use of 
deposit and withdraw. I took some time to format this account statement for accessible viewing of users. Running the code up
to this point gives you the following output:
![image](https://github.com/user-attachments/assets/662102d1-5215-4672-af5b-80af65f568eb)
![image](https://github.com/user-attachments/assets/ef818d6f-0cb0-431c-b1f2-5a10d3e64a79)

Finally, we need to make an infrastructure to serve as an account repository. Saving the account was initially incorporated in creating the 
account so I just isolated it on this class. Finding the account by Account ID follows a similar pattern of looking up the input on the
accounts dictionary. This was replicated for the method in finding accounts by customer id with the addded step of processing the input
customer ID. Since the dictionary had keys of Account ID, I compared the input to the dictionary's values instead. Once a match was made,
the corresponding key of the match is pulled up and is then used to get the account's details. I added test scenarios of a failed search
to ensure that the program handles requests from non-existent accounts. Running the code upto this point gives you the following output:
![image](https://github.com/user-attachments/assets/6a4fcd58-b319-4f79-a9ed-0dce25ed59c2)
![image](https://github.com/user-attachments/assets/591d5320-f2ec-4a03-8506-b97dc460aeb8)
