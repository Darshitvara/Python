class account:
     bal = 0
     def __init__(self,amt):
          account.bal = amt

     def getdata(self):
          print("Enter the Name of Account Holder : ",end='')
          self.name = input()

     def credit_amt(self):         
          print("Enter the amount you want to credit : ",end='')
          self.amt = int(input())
          account.bal += self.amt

     def debit_amt(self):
          if account.bal > 3000:
               print('Enter the amount you want to Debit : ',end='')
               self.amt = int(input())
               account.bal -= self.amt
          else:
               print(" You can't debit amount.")
     
     def exec_opr(self,c):
               if c == 1:
                    self.credit_amt()
               if c == 2:
                    self.debit_amt()
               if c == 3:
                    account.display_bal()
       
     @classmethod
     def display_bal(cls):
          print("The Current Balance in your account is ",cls.bal)

flag = 0
while 1:
     print("Enter Your Bank Balance : ",end='')
     am = int(input())
     if am < 0 :
          print("Enter the currect amount. ")
     elif am < 3000:
          less = 3000 - am
          print('You don''t have sufficient balance in your account.')
          print("    Deposit ",less," To maintain minimum Balance.") 
          break
     else:
          break

client1 = account(am)

client1.getdata()

while flag == 0:
     print('1. Credit ')
     print('2. Debit')
     print('3. Display Amount')
     print('4. Exit')
     print('Enter your choice from above : ',end='')
     ch = int(input())
     if ch == 4 :
          break
     client1.exec_opr(ch)
