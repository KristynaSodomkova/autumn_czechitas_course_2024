# BALIK PODRUHE

# Vrať se k návrhu software pro zásilkovou společnost.
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}"


    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        return 359

    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        self.state = "doručen"
        return "Doručení uloženo"

balik1 = Package("Praha 1", 5, "doručen")
balik2 = Package("Praha 2", 50, "nedoručen")
print(balik1.deliver())
print(balik2.deliver())
print(balik2.deliver())


# U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print().
print(Package("Nejaka adresa", 4, "doručen"))

# Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení.
# Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen.
# Pokud ano, metoda vrátí zprávu "Balík již byl doručen". Tím bude řidič (řidička) informován(a) o tom,
# že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku.
# Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".
# Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?


# ---------------------------------------
# KNIHA PODRUHE

"""
Vrať se k práci se třídou Book. Pokud jsi ji nestihl(a) v minulé části vytvořit, 
vrať se nejprve k zadání příkladu na předchozí stránce a třídu si vytvoř.

U knihy budeme chtít evidovat, kolik kusů bylo prodáno. 
Přidej atribut sold, jehož hodnotu bude možné nastavit v metodě __init__(). 
Dále přidej atribut costs, které představují náklady na jednu knihu (např. tisk, doprava do knihkupectví, podíl autora (autorky) atd.).
Přidej metodu profit(), která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).
Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku. 
Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák". 
Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". 
Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".
"""

class Book:
    def __init__(self, title, pages, price, sold, costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs



    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."


    def get_time_to_read(self, minutes_per_page=4):
        return self.pages * minutes_per_page / 60

    def profit(self):
        return self.sold * (self.price - self.costs)

    def rating(self):
        if self.profit() < 50000:
            return "propadák"
        elif self.profit() < 500000:
            return "průměr"
        return "bestseller"

book1 = Book("Harry Potter", 400, 350, 100)
book2 = Book("Harry Potter 2", 500, 450, 200)

# ---------------------------------------
# ZKUSEBNI DOBA

"""
U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

    Rozšiř metodu __init__ třídy Employee o parametr probation_period. Tuto hodnotu ulož jako atribut třídy Employee.
    Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.

"""
class Employee:
    def __init__(self, name, position, holiday_entitlement, probation_period):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.probation_period = probation_period

    def __str__(self):
        if self.probation_period:
            return f"Zaměstnanec {self.name} pracuje na pozici {self.position}. Je ve zkušební době."
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

frantisek = Employee("František Novák", "konstruktér", 25)
print(frantisek)