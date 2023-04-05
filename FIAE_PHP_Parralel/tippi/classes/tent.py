class Tent:
    total_count = 0
    max_count = 100

    def add_person(self, amount):
        if Tent.total_count >= self.max_count:
            print("Voll, geh weg!")
        elif amount > self.max_count - Tent.total_count:
            print(f"Ich lass nur noch {self.max_count - Tent.total_count} rein!")
            Tent.total_count = self.max_count
        else:
            print(f"Willkommen! Kommt alle her, wir haben noch {self.max_count - Tent.total_count} Plätze frei!")
            Tent.total_count += amount
