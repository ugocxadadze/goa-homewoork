number = int(input("Enter a number: "))


total_sum = 0


for i in range(1, number + 1):
    total_sum += i


print("The sum of all numbers up to", number, "is:", total_sum)