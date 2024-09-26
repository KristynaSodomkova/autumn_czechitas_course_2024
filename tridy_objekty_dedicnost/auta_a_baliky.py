"""
U našich balíků budeme nově evidovat, který řidič(ka) balík doručuje. Díky tomu pak bude možné odeslat SMS zprávu s číslem řidiče (řidičky), aby mohli zákazníci v případě potřeby řidiče (řidičku) kontaktovat.

Vytvoř třídu Driver, která bude mít atributy name a phone_number. Dále uprav třídu Package.
Třída bude mít nově atribut driver, ve kterém bude uložen(a) řidič(ka) doručující balík.
Uprav i třídu ValuablePackage, aby v metodě __init__() předala hodnotu parametru driver metodě __init__ rodičovské třídy.
Přidej třídě Package metodu send_message(), která odešle zprávu s textem: "Dnes budeme doručovat váš balík.
V případě potřeby kontaktujte řidiče na čísle: " Na konec zprávy doplň telefonní číslo.
"""

class Package:
    def __init__(self, address, weight, state, driver):
        self.address = address
        self.weight = weight
        self.state = state
        self.driver = driver

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

    def send_message(self):
        return f"Dnes budeme doručovat váš balík. V případě potřeby kontaktujte řidiče na čísle: {self.driver.phone_number}"

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value, driver):
        super().__init__(address, weight, state, driver)
        self.value = value

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state} a má hodnotu {self.value} Kč"

class Driver:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"Řidič(ka) {self.name} je k zastižení na čísle {self.phone_number}."

driver_1 = Driver("Jan Novák", "+420 777 888 999")
driver_2 = Driver("Marie Nováková", "+420 777 888 000")

message = Package("Praha 1", 5, "nedoručen", driver_1)
print(message.send_message())