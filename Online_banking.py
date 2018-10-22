import sys

class bank():
  def __init__(self):
    self.balance=0
    return

  def deposit(self, value):
    self.balance+=float(value)
    self.print()

  def withdraw(self, value):
    self.balance-=float(value)
    self.print()

  def transfer(self, value):
    self.balance-=float(value)
    self.print()
    return
  
  def print(self):
    print("Your balance is "+str(self.balance))
    if self.balance>=500:
      print("You're RICH!!! Go buy a car NOW!!!")
    elif self.balance>100:
      print("You're not broke, but you can do better, GO MAKE SOME MORE MONEY :) ")
    elif self.balance>=0:
      print("You're broke bro, GO GET A JOB!! :(")
    else:
      print("YOU'RE OWING THE BANK!!! GO DEPOSIT MONEY NOW!!!")
    return

  def exit(self, name):
    print("Goodbye "+name)
    input()
    raise SystemExit

list_names=[]

name=input("Hello, what is your account name?")
user=bank()
print("Hi "+str(name))
user.print()
while True:
  answer=input("What would you like to do? (e.g deposit 23, withdraw 12, view balance, exit) ")
  answer_list=answer.split(" ")
  if answer_list[0]== "deposit":
    user.deposit(answer_list[1])
  elif answer_list[0]=="withdraw":
    user.withdraw(answer_list[1])
  elif answer_list[0]=="view":
    user.print()
  elif answer_list[0]=="exit":
    user.exit(name)
