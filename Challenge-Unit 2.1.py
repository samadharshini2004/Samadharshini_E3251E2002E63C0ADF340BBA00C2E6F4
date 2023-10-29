#bank account
class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  #deposit
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited: ₹{}. New Balance: ₹{}.".format(amount,
                                                       self.__account_balance))
    else:
      print("Invalid Deposit Amount.")

  #withdraw
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdrew: ₹{}. New Balance: ₹{}.".format(amount,
                                                      self.__account_balance))
    else:
      print("Invalid withdrawal amount or Insufficient balance.")

  #display
  def display_balance(self):
    print("Account Balance of {} (Account Number: {} is ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


#creating an instance of the BankAccount class
account = BankAccount(account_number="123456789",
                      account_holder_name="Sareeshma Rehan",
                      initial_balance=90000.0)

#displaying
account.display_balance()
#testing the deposit functionality
account.deposit(5000.0)
#testing the withdrawal functionality
account.withdraw(9000.0)
account.withdraw(300000)
