number = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))


for i in range(1, number + 1):
    if i % 2 == 0:
        print(f"{i} - ლუწი")
    else:
        print(f"{i} - კენტი")
        