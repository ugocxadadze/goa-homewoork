family_members = []


print("გთხოვთ შეიყვანოთ ოჯახის წევრების სახელები. როცა დასულდებით, დაწერეთ 'დასრულდა'.")

while True:
    name = input("შეიყვანეთ ოჯახის წევრის სახელი: ")
    if name.lower() == 'დასრულდა':
        break
    family_members.append(name)


print("\ოჯახის წევრები:")
for member in family_members:
    print(member)