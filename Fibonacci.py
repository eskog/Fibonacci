#!/usr/bin/python

fibonacci = [0,1]
legitInput = False
while not legitInput:
    try:
         i = int(raw_input("How many numbers do you want? "))
    except ValueError as e:
        print(e)
        print("Try again!")
    else:
        legitInput = True
x=1

while x != i:
    fibonacci.append(fibonacci[x-1] + fibonacci[x])
    x+=1
print(fibonacci[0:x])