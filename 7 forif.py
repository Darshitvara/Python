
list = [ "darshit", 4 , "jay",30 , "Harsh",90  ,"maitri",10 ,"umangi",5,"tanvi",1]

for item in list:
     
   if str(item).isnumeric() and int(item) < 6:
      print(item)

for item in list:
     if str(item).isnumeric() == 0 :
          print(item)

