my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.extend([7, 8])
my_list.insert(2, 2.5)
print("სიების შექმნა და განახლება:")
print(my_list)  # [1, 2, 2.5, 3, 4, 5, 6, 7, 8]
my_list.remove(2.5)
del my_list[0]
popped_element = my_list.pop()
print("ელემენტების წაშლა და გამოცვლა:")
print(my_list)  # [2, 3, 4, 5, 6, 7]
print("წაშლილი ელემენტი:"), popped_element()

sub_list1 = my_list[1:4]
sub_list2 = my_list[:3]
sub_list3 = my_list[3:]

print("slicing-ის მაგალითები:")
print("1:4 სექრეტი:", sub_list1)
print("[:3] სექრეტი:", sub_list2) 
print("[3:] სექრეტი:", sub_list3)
full_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = full_list[::2]

print("მრავალგზის სიის გაწვდვა:")
print("მთლიან სიის გაწვდვა:", sliced_list)
numbers = [10, 20, 30, 40, 50]


for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2  # ყველა ელემენტის გაწვდვა 2-ით

print("სიის ელემენტების გაწვდვა 2-ით:")
print(numbers)  # [20, 40, 60, 80, 100]
names = ["Alice", "Bob", "Charlie"]
ages = [24, 27, 22]


combined = list(zip(names, ages))

print("პარალელური სიების გაწვდვა:")
for name, age in combined:
    print(f"{name} არის {age} წლის")
#პროგრამული სავარჯიშოები


items = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
first_two = items[:2]
last_two = items[-2:]
middle = items[2:-2]

print("პროგრამული")
print("პირველი ორი:", first_two)  # ['apple', 'banana']
print("ბოლო ორი:", last_two)  # ['fig', 'grape']
print("საშუალო:", middle)  # ['cherry', 'date']

numbers = list(range(1, 11))

print("10 რიცხვის სიის slicing-ის მაგალითები:")
print("ყველა რიცხვი:", numbers[:])
print("პირველი ხუთი:", numbers[:5])
print("ბოლო ხუთი:", numbers[5:])
print("ზოგიერთი სექრეტი (2-დან 8-მდე):", numbers[2:8])
print("ყოველი მეორე რიცხვი:", numbers[::2])

