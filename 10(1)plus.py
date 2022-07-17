
f = open("just.txt","r+")    #To perform any operation on file , first it must be open and close after operaion.

fr = f.read()     

f.write("\n Bye bye.")

print(fr)                   #Indiractly print the content of file (  BY Help of fr variable , to reduce complexity and maintain clear code look)

f.close()                   #Mendatory part


g = open("just.txt","a")    #Though the variable g , operation will be performed untill file closed.
                           
g.write("\n\n\n\ni'm back.")

g.close()                  #Mendatory part



d = open("just.txt","r")   #To read the content which is apended.

print(d.read())

d.close()                  #Mendatory part
