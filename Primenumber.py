def prime():
    while choice == 1:
        number = int(input("Enter your no: "))
        if number > 1:
            for num in range(2, number + 1):
                if number % num == 0:
                    print(number, "is not prime")
                    break
                else:
                    print(number, "is prime.")
                    break
        else:
            print("Enter positive number from 2 and more")
        break
    while choice == 2:
        lower_range = int(input("Enter lower range : "))
        higher_range = int(input("Enter your no: "))
        for number in range(lower_range, higher_range+1):
            for num in range(2, number):
                if number % num == 0:
                    # remove "#" to print non-prime number
                    # print(number, "is not prime")
                    break
                else:

                    print(number, "is prime.")
                    list1.append(number)
                    break
        print(list1)
        sum1 = sum(list1)
        print("sum of prime no in range", lower_range, "to", higher_range, "is", sum1)
        avarage = sum1 / len(list1)
        print(avarage)
        break


print("PRIME NUMBER")
print(f"\nTo check single Prime number enter 1"
      f"\nTo check PRIME number's in range enter 2\n")
choice = int(input("Enter your choice: "))
list1 = []

prime()
