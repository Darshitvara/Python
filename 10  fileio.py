
f = open("darshit.txt","w")
fw = f.write("\n Hello ,\n here is the already stored content.\n")
f.close()

f = open("darshit.txt","a")
print(" Enter String to add : ",end= '')
str = input() 
fa = f.write(str)
f.close()

f = open("darshit.txt","r")
fr = f.read()
print(fr)
f.close()

