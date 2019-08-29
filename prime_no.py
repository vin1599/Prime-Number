
a = int(input("enter no: "))
for i in range(2, a):
    if a % i == 0:
        print(a, "is not prime")
        break
    else:
        print(a, "is prime")
        break
