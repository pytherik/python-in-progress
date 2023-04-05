class Garage:

    max_cars = 2
    total_cars = 0

    def __init__(self, name, color):
        if Garage.total_cars < 2:
            self.name = name
            self.color = color
            Garage.total_cars += 1
            print(f"Das {color}e {name} steht jetzt in der  Garage!")
        else:
            print(f"Die Garage ist voll! Der {color}e {name} muss woanders parken!")