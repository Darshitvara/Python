
from asyncio.windows_events import NULL


class person:
     c_obj = 0
     def __init__(self):
          self.f_name = 'Anonymous'
          self.m_name = ''
          self.l_name = ''
          self.age  = 18
          self.adrs = 'Earth'
          self.e_id = 'Not Created.'
          person.c_obj += 1

     def get_data(self):
          print("Enter Your First Name  : ",end='')
          self.f_name = input()
          print("Enter Your Middle Name : ",end='')
          self.m_name = input()
          print("Enter Your Last Name   : ",end='')
          self.l_name = input()
          print("Enter Your Age         : ",end='')
          self.age = int(input())
          print("Enter Your Address     : ",end='')
          self.adrs = input()
          print("Enter Your Email Id    : ",end='')
          self.e_id = input()
          print('\n')
     def put_data(self):         
               print(' Name     : ',self.f_name,self.m_name,self.l_name)              
               print(' Age      : ',self.age)
               print(' Email Id : ',self.e_id)
               print(' Address  : ',self.adrs,'\n')

     def total_ob(self):
          return person.c_obj

ob = person()
ob1 = person()
ob2 = person()
print("Hello Human,\n")
ob.get_data()
# ob1.get_data() 
ob.put_data()
ob1.put_data()
tob = ob.total_ob()
print('Total Number of created object : ',tob)
