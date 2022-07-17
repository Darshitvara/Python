from functools import reduce
lst = [2,5,3,13,6,15,22,7]

fil_list_evens = list(filter(lambda a : a%2==0,lst))
fil_list_odds = list(filter(lambda a : a%2==1,lst))

print(fil_list_evens)
print(fil_list_odds)

map_list = list(map(lambda b : b * b, lst))

print(map_list)

reduce_list = reduce(lambda a,b : a+b,map_list)

print(reduce_list)