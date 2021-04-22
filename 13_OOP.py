class KitchenStuff:
    def __init__(self, color, volume):
        self.color = "light" + color
        self.volume = volume

    def serve(self):
        return f"Here you have a {self.color} {self.volume}."


class Cup(KitchenStuff):
    def __init__(self, color, volume, liquid, style):
        super().__init__(color, volume)

        self.liquid = liquid
        self.style = style

    def pour_down(self):
        return f"Pouring {self.volume} ml of {self.liquid}."


class Plate(KitchenStuff):
    def __init__(self, color, volume, dish):
        super().__init__(color, volume)

        self.dish = dish

    def serve(self):
        return f"Here you have a {self.color} plate of {self.dish}."


oriental_cup = Cup(color="red", volume=200, liquid="tea", style="oriental")
classic_cup = Cup(color="white", volume=500, liquid="juice", style="classic")

fish_plate = Plate(color="gray", volume=700, dish="fish")
pasta_plate = Plate(color="brown", volume=1000, dish="pasta")

my_cups = [oriental_cup, classic_cup]
my_plates = [fish_plate, pasta_plate]

for cup in my_cups:
    print(f"I like my {cup.color} {cup.style} cup because it has {cup.volume} ml of {cup.liquid}.")
    print(cup.serve())
    print(cup.pour_down())

for plate in my_plates:
    print(f"This is a {plate.color} plate of {plate.dish}.")
    print(plate.serve())
