a = 12
b = 3

print(a + b)  #15
print(a -b)   #9
print(a * b)  #35
print(a / b)  #4.0
print(a // b) #4 integer division, rounded down towards minus infinity
print(a % b)  #0 modulo: the remainder after integer division


print()

for i in range(1, 4):
    print(i)

print()

# we cannot use below one as it will produce float output which would be problem for loop
#for i in range(1, a / b):
#    print(i)  
for i in range(1, a // b):
    print(i)

