"""
Vedení společnosti si uvědomilo, že do hodnoty balíků v autě by se neměly započítávat balíky, které už byly doručeny,
protože již byly předány příjemci a nebudou tedy ukradeny nebo zničeny.

    Uprav kód, který vytváří balíky, aby byl jeden balík vytvořený ve stavu doručen.
    Uprav cyklus, aby započítal hodnotu pouze těch balíků, které jsou ve stavu nedoručen.
    Je třeba pro čtení použít některou z funkcí isinstance(), hasattr() nebo getattr().

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
    if hasattr(package, "value") and package.state == "nedoručen":
        total_value += package.value

print(total_value)
package_1.deliver()

total_value = 0
for package in package_list:
    if hasattr(package, "value") and package.state == "nedoručen":
        total_value += package.value
print(total_value)