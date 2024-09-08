for number in range(1, 11):
    print(number)

#2
my_list = []

for i in range(10):
    
    my_list.append(i)

print("სიაში არსებული 10 ელემენტი:")
print(my_list)

#3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = [num for num in numbers if num % 2 == 0]


print("წყვილი რიცხვები:")
print(filtered_numbers)