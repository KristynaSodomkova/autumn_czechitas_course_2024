"""
Na adrese https://svatky.adresa.info/json najdete API, které vám odpoví, kdo má dneska svátek.

    Využijte toto API k tomu, abyste napsali program, který po spuštění vypíše na obrazovku kdo má dneska svátek.
    Pokud použijete adresu https://svatky.adresa.info/json?date=DDMM, kde místo DDMM doplníte datum,
    dostanete jméno, které má svátek v zadaný den. Formát DDMM znamená že 6. ledna bude zapsáno jako 0601, 12. září jako 1209 apod.
    Napište program, který dostane na příkazové řádce číslo dne a číslo měsíce a vypíše na výstup kdo má v daný den svátek.
    Použijte váš program abyste zjistili, kdo má svátek 29. února.
    Bonus: předchozí bod uprav tak, že nebudeš dávat funkci requests.get() adresu včetně parametru date=1209,
    ale pouze základní "endpoint" https://svatky.adresa.info/json a parametry (vše za ?) dodáš volitelným parametrem.
    Budeš potřebovat pracovat s dokumentací k requests.
"""

import requests

date_of_nameday = input("Enter date in format DDMM: ")
response = requests.get(f'https://svatky.adresa.info/json?date={date_of_nameday}')

data = response.json()

print(data[0]['name'])
