"""
Napište program, který se po spuštění zeptá na název souboru,
který má vytvořit (nebo přepsat, pokud už ten soubor existuje), a pak se zeptá na řádek textu, který má do souboru zapsat.
"""

file_name = input("Zadejte název souboru: ")
text = input("Zadejte text: ")

with open(file_name, mode="w", encoding="utf-8") as output_file:
    print(text, file=output_file)
