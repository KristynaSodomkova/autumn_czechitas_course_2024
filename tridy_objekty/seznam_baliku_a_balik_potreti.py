"""
Přepravní společnost musí rozdělovat balíky do jednotlivých aut. Při plánování dopravy je potřeba hlídat,
zda pro jeden automobil není naplánována přeprava příliš velkého množství balíků. Vytvoř tedy tři objekty třídy Package.
Dále vytvoř seznam package_list, do kterého vlož vytvořené objekty. Příklad objektů a seznamu je níže.

package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
package_3 = Package("Vydrník svatého Drába 13", 0.5, "nedoručen")
package_list = [package_1, package_2, package_3]

    Vytvoř si proměnnou total_weight, do které si s využitím cyklu budeš ukládat celkovou hmotnost všech balíků. Na začátku bude mít hodnotu 0.
    Vytvoř cyklus, který projde seznam package_list.
    Pro každý balík přičti jeho hmotnost k proměnné total_weight.
    Na konci programu vypiš, jaká je celková hmotnost všech balíků.

Zatím jsme uvažovali, že třídu Package využívá ve svém programu přepravní společnost.
Stejnou třídu by ale mohl používat e-shop, který takto eviduje zboží odeslané zákazníkům.
Provozovatele e-shopu bude určitě zajímat, kolik celkem zaplatí přepravní společnosti za přepravu balíku.
Využij tedy balíky v seznamu package_list a spočítej celkové náklady na jejich přepravu.
Náklady na přepravu jednoho balíku zjistíš voláním metody delivery_price().

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

"""
Balík potřetí

Vrať se k návrhu software pro zásilkovou společnost. 
U třídy Package uprav atribut state tak, aby byl chráněný. Ověř, že vytváření objektů i výpisy informací o něm fungují.
"""
# self._state = state
# if self._state == "doručen":
# self._state = "doručen"