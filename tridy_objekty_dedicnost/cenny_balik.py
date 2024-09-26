"""
Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

    Vytvoř třídu ValuablePackage, která dědí od třídy Package. ValuablePackage má navíc atribut value, ostatní atributy dědí od třídy Package.
    Atribut value nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Package.
    Přidej do výpisu informací o cenném balíku (metoda __str__) informaci o ceně balíku.
    Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí. Současně si vytvoř "obyčejný" balík o zkontroluj, že u něj se nic nezměnilo.

"""
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

package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
package_3 = Package("Vydrník svatého Drába 13", 0.5, "nedoručen")
package_list = [package_1, package_2, package_3]

total_weight = 0
for package in package_list:
    total_weight += package.weight

print(total_weight)

total_price = 0
for package in package_list:
    total_price += package.delivery_price()

print(total_price)

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state} a má hodnotu {self.value} Kč"

package_4 = ValuablePackage("Grimmauldovo náměstí 11", 15, "nedoručen", 500)
print(package_4)
print(package_4.value)
print(package_4.delivery_price())
print(package_4.deliver())
print(package_4.deliver())
# print(package_1.value)


