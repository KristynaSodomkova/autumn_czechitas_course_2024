"""
Nyní se vrátíme k práci pro nakladatelství, pro které jsme již připravili třídy Item, Book a AudioBook.
V e-shopech se často objevuje možnost filtrování produktů.
Uvažujme například, že někteří fanoušci a fanynky audioknih vybírají knihy podle herce a herečky, kteří je čtou.
Preferované jméno bude uložené v proměnné favourite_narrator.
Napiš kód, který projde všechny položky v seznamu all_items a vypíše názvy (atribut title) objektů,
pro které se hodnota atributu narrator rovná hodnota v proměnné favourite_narrator.
Pozor na to, že v seznamu all_items jsou i běžné knihy, které vypravěče nemají.
Zajisti, aby program neskončil chybou, protože některý objekt nemá atribut narrator.
"""
class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_time_to_read(self):
        pass

class Book(Item):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self, minutes_per_page=4):
        return self.pages * minutes_per_page / 60

class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator

    def get_time_to_read(self):
        return self.duration_in_hours


favourite_narrator = "Zbyšek Horák"
item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
item_2 = Book("Kadet Hornblower", 399, 242)
item_3 = AudioBook("Odysseus", 389, 13.7, "Lukáš Hlavica")

all_items = [item_1, item_2, item_3]

for item in all_items:
    if hasattr(item, "narrator") and item.narrator == favourite_narrator:
        print(item.title)