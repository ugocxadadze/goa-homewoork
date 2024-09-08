favorite_cars = ["bmw", "audi", "toyota", "ford", "mercedes", "lamborghini", "porsche", "dodge"]
disliked_cars = ["audi", "ford", "dodge", "toyota"]
new_cars = ["ferrari", "bugatti", "mclaren", "jaguar"]
for i in range(len(favorite_cars)):
    if favorite_cars[i] in disliked_cars:
        favorite_cars[i] = new_cars.pop(0)
print(f"ჩემი საყვარელი მანქანებია: {', '.join(favorite_cars)}")