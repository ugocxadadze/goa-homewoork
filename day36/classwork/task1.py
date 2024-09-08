foods = [
    "პიცა",
    "ჰამბურგერი",
    "პასტა",
    "სალათი",
    "ფრანჩიზი",
    "ბურგერი",
    "შაურმა",
    "საშუალო",
    "ბურგერი",
    "დონატი"
]

middle_index = len(foods) // 2
if len(foods) % 2 == 0:
    middle_elements = foods[middle_index - 1:middle_index + 2]
else:
    middle_elements = foods[middle_index - 1:middle_index + 2]

print("შუაში მყოფი 3 ელემენტი:")
print(middle_elements)

print("\nყველა ელემენტი:")
for food in foods:
    print(food)

print("\nპირველი 4 ელემენტი:")
print(foods[:4])

print("\nბოლო 4 ელემენტი:")
print(foods[-4:])