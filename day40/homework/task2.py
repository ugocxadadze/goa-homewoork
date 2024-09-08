even_numbers = []
odd_numbers = []


number = int(input("შეიყვანეთ რიცხვი: "))


if number % 2 == 0:
    even_numbers.append(number)
    print(f"{number} არის ლუწი რიცხვი და დაამატა ლუწი რიცხვების სიაში.")
else:
    odd_numbers.append(number)
    print(f"{number} არის კენტი რიცხვი და დაამატა კენტების სიაში.")


print("\nლუწი რიცხვების სია:")
print(even_numbers)

print("\nკენტების სია:")
print(odd_numbers)