
start_range = int(input("Enter Starting range : "))
end_range = int(input("Enter Ending range : "))

for n in range(start_range,end_range):
     s = 0
     temp = n 
     while temp > 0:
          m = int(temp) % 10 
          s = s + (m * m * m)
          temp = int(temp)/10
  
     if s == n:
          print(n," is Perfect Number. ")

print("Done.")