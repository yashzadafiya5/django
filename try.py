import itertools

num = [1, 3]
value = [2, 4]

# iterates over 3 lists and executes 
# 2 times as len(value)= 2 which is the
# minimum among all the three 
for a in zip(num, value):
    
    print (a)
    