import json

with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)
print(runners)

winner = runners[0]
winner_time = winner["casy"]["oficialni"]
print(winner_time)

"""
Pracuj dál se souborem zavod.json. Cílem cvičení je zjistit čas závodníka, který získal stříbrnou medaili - seznam závodníků je seřazený, tedy výherce je zapsán jako první v našem souboru. Budeš tedy muset projít data pomocí cyklu a vytvořit seznam všech závodníků, kteří závod dokončili, tj. jejich oficiální čas není 'DNF'.

Můžeš postupovat následujícím způsobem:

    Vytvoř si prázdný seznam finishers, kam budeš vkládat jména závodníků, kteří závod doběhli.
    Pomocí cyklu projdi seznam závodníků.
    Do cyklu vlož podmínku, která ověří, zda oficiální čas závodníka je odlišná od řetězce DNF.
    Dovnitř podmínky vlož kód, který vloží jméno a oficiální čas závodníka do seznamu finishers. 
    (obě hodnoty můžeš dát do nového seznamu, výsledný seznam finishers bude tedy obsahovat seznamy jako jeho položky). Pro přidání prvku do seznamu použij metodu append(), tedy finishers.append(seznam_s_jmenem_a_casem_zavodnika)
    Na konec programu (mimo cyklus) vlož příkaz na vypsání obsahu seznamu finishers.
    Zvol index výsledného seznamu finishers tak aby print vypisoval pouze stříbrného medailistu.

U každého bodu si klidně ověř že tvůj aktuální kus kódu dělá to co má - například dočasným pomocným printem.
"""

finishers = []
for runner in runners:
    if runner["casy"]["oficialni"] != "DNF":
        finishers.append([runner["jmeno"], runner["casy"]["oficialni"]])

print(finishers[1])


