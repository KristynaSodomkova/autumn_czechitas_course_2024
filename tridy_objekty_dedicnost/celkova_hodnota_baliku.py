"""
Pokračuj ve své práci pro zásilkovou společnost.
Společnost chce doplnit do aplikace funkci pro výpočet celkového hodnoty nákladu nějakého auta,
aby pak (např. v případě nehody nebo krádeže) mohla snadno spočítat celkovou hodnotu cenných balíků v autě a předat informaci pojišťovně.
Příklad je podobný bonusu na výpočet celkové hmotnosti z předchozí části, liší se ale v tom, že hodnotu mají pouze cenné balíky, zatímco hmotnost mají všechny balíky.

Níže je příklad balíků, které můžeš použít pro tvorbu svého programu.

    Vytvoř si proměnnou total_value, do které si s využitím cyklu budeš ukládat celkovou hodnotu všech balíků. Na začátku bude mít hodnotu 0.
    Vytvoř cyklus, který projde seznam package_list.
    Vyber funkci, která je podle tebe nejvhodnější pro zajištění bezpečného čtení atributu value. Můžeš použít funkci isinstance(), hasattr() i getattr(). Přičti hodnotu balíku k proměnné total_value, aniž by program skončil chybou u objektu package_2.
    Na konci programu vypiš, jaká je celková hodnota balíků v autě.
"""
from dataclasses import dataclass


@dataclass
class Package:
    address: str
    weight: float
    state: str


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

package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
package_3 = Package("Vydrník svatého Drába 13", 0.5, "nedoručen")
package_list = [package_1, package_2, package_3]

total_weight = 0
for package in package_list:
    total_weight += package.weight

total_price = 0
for package in package_list:
    total_price += package.delivery_price()

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state} a má hodnotu {self.value} Kč"

package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

print(package_1)

total_value = 0
for package in package_list:
    if hasattr(package, "value"):
        total_value += package.value

print(total_value)
