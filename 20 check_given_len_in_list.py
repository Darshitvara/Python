from re import L

def Enter_name():
     for i in range(5):
          print(" Student {} Name : ".format(i+1),end='')
          name = input()
          l_name.append(name)

def check_len(lst):
     for i in range(5):    
          if len(lst[i]) > 5 :
               print(lst[i])

l_name = []
Enter_name()
# print(l_name)
check_len(l_name)


