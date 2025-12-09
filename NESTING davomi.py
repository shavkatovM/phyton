#1masala
# k = int(input("k = "))
# n = int(input("n = "))
# for i in range(n):
#     print(n)

#2masala
a = int(input("a = "))
b = int(input("b = "))

count = 0

for i in range(a, b + 1):
    print(i, end=" ")
    count += 1

print("\nChiqarilgan sonlar soni:", count)

#3masala
a = int(input("a = "))
b = int(input("b = "))
count= 0
for i in range(a,b > 0):
    print(i,end="")
    count -=1
print("\nChiqarilgan sonlar soni:", count)

#4masala
p = float(input("1kg narxi = "))

for i in range(1,10 + 1): 
    print(f"{1} kg = {p * i}")