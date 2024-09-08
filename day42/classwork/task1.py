names = []

for i in range(3):
    name = input(f"გთხოვთ, შეიყვანოთ {i+1}. სახელი: ")
    names.append(name)


print("\nსიაში არსებული სახელები:")
for name in names:
    print(name)