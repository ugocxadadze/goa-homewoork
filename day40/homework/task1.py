names_list = []


for i in range(3):
    name = input(f"შეიყვანეთ სახელი #{i+1}: ")
    names_list.append(name)


print("\შეგროვილი სახელები:")
for name in names_list:
    print(name)