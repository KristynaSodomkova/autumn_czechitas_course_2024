"""
Implementujme systém pro správu seznamu úkolů. Stáhni si soubor tasks.txt.
Každý řádek obsahuje název úkolu a jeho prioritu (1=vysoká, 2=střední, 3=nízká), hodnoty jsou oddělené čárkou.

Tvůj program by měl nejprve načíst existující úkoly ze souboru `tasks.txt`` a uložit je do seznamu.
Pokud soubor neexistuje, program jen vypíše informaci o tom, že soubor neexistuje a že ho založí.
Samotné založení souboru v této části řešit nemusíš, o to se postaráme v další části.

Poté program umožní uživateli přidat nový úkol a jeho prioritu.
Pokud jako prioritu nezadá číslo nebo zadá jiné číslo než 1 až 3, vyvolej ValueError.
Pokud je vstup v pořádku, ulož seznam s přidaným úkolem do souboru tasks.txt.
Pokud soubor neexistuje, stačí ho pomocí funkce open s módem w otevřít.
"""
try:
    with open("tasks.txt", mode="r", encoding="utf-8") as input_file:
        tasks = input_file.readlines()
except FileNotFoundError:
    print("Soubor tasks.txt neexistuje. Založím nový soubor.")
    tasks = []

if not tasks: # to same jako if tasks == []:
    print("Soubor neobsahuje žádné úkoly.")

new_task = input("Zadej nový úkol: ")
new_priority = input(f"Zadej prioritu úkolu {new_task} (1=vysoká, 2=střední, 3=nízká): ")

if new_priority not in ["1", "2", "3"]:
    raise ValueError("Priorita musí být číslo 1, 2 nebo 3.")
else:
    new_task_item = f"{new_task},{new_priority}\n"
    with open("tasks.txt", mode="a", encoding="utf-8") as output_file:
        output_file.write(new_task_item)
    print(f"Úkol {new_task} byl přidán do seznamu.")
