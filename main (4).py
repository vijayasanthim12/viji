'''implement a class called bankaccount that represents a bank account.the class should have private.
attributes for account number,account holder name,and account balance.includ methods to 
deposite money,withdraw money,and display the account balance.ensure that the account balance
cannot be accessed directly from outside the class.write a program to create an instance of the
BankAccount class and test the deposite and withdrawl functionality.'''


class BankAccount:

  def__init__(self,account_number,account_holder_name,initial-balance=0.0):
  self.__account_number = account_number
  self.__account_holder_name = account_holder_name
  self.__account_balance = initial_balance

def deposit(self,amount):
  if amount > 0:
    self.__account_balance+=amount
    #self.__account_balance=self.__account_balance+amount
print("Deposited ₹{} .new balance: ₹{}".format(amount))