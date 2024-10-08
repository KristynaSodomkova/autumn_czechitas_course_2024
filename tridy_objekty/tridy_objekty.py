# BALIK

# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state.
# Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

# Přidej metodu get_info(), která vrátí informace o balíku jako řetězec.
# Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}"

# Zkus si vytvořit alespoň dva objekty ze třídy Balik.
# U address uvažujeme typ řetězec (str), u weight desetinné číslo. U atributu state zadávej
# pro zjednodušení pouze dva stavy: doručen a nedoručen.
# balik1 = Package("Václavské Náměstí 12, Praha", 30.25, "nedoručen")
# balik2 = Package("Staromestske Náměstí 2, Praha", 0.50, "doručen")

# Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.
# print(balik1.get_info())
# print(balik2.get_info())


# Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku.
# Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg do 20 kg je 159 Kč a
# cena přepravy balíků těžších než 20 kg je 359 Kč. Metoda spočítá cenu a vrátí ji jako číslo.

    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        return 359

balik1 = Package("Václavské Náměstí 12, Praha", 30.25, "nedoručen")
balik2 = Package("Staromestske Náměstí 2, Praha", 0.50, "doručen")

print(balik1.delivery_price())
print(balik2.delivery_price())
# --------------------------------------------------------------------
# Kniha
# Zkus pro nakladatelství vytvořit software s využitím tříd a objektů.
# Vytvoř tedy třídu Book, která reprezentuje knihu.
# Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price


# Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

# Přidej metodu get_time_to_read().
# Metoda vrátí čas potřebný na přečtení knihy v hodinách.
# S využitím atributu pages vypočítej čas na přečtení knihy.
# Metoda bude mít nepovinný parametr, který udává počet minut potřebných pro přečtení jedné stránky knihy.
# Dobu potřebnou na přečtení knihy získáš jako násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy.
# Výchozí hodnota nepovinného parametru je 4.

    def get_time_to_read(self, minutes_per_page=4):
        return self.pages * minutes_per_page / 60

print(Book.get_info(Book("Harry Potter", 300, 250)))
print(Book.get_time_to_read(Book("Ronja", 200, 300)))
print(Book.get_time_to_read(Book("Eggs and me", 250, 420)))
print(Book.get_time_to_read(Book("Eggs and me", 250, 420), 5))
