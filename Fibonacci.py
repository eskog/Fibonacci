#!/usr/bin/python

fibonacci = [0,1]
i = int(raw_input("How many numbers do you want? "))
x=1

while x != i:
    fibonacci.append(fibonacci[x-1] + fibonacci[x])
    x+=1
print(fibonacci[0:x])