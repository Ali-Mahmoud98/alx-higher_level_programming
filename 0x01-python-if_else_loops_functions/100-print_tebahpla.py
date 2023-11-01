#!/usr/bin/python3

x = 0
for i in range(ord('z'), ord('a') - 1, -1):
    x += 1
    if x%2 == 0:
        i -= 32 
    print("{:c}".format(i), end='')
