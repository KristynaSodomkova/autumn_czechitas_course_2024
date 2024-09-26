import json
"""
Stáhněte si soubor words.txt a zpracujte z něj výstupní soubor ve formátu JSON obsahující slovník. 
Klíče budou písmena a hodnoty seznamy slov, které začínají písmenem v klíči. Pokud na nějaké písmeno žádná slova nezačínají, tak ve výstupu toto písmeno nebude. 
Seřaďte tyto seznamy podle abecedy. Zajistěte, aby i klíče ve výstupním JSON souboru byly seřazeny a data byla odsazena čtyřmi mezerami pro lepší čitelnost člověkem.

Vzorový výstup: output.json.
"""

with open('words.txt', encoding='utf-8') as file:
    words = file.read().split()

words_list = []
for word in words:
    first_letter = word[0]
    if first_letter not in words_list:
        words_list.append(first_letter)
words_list = sorted(words_list)

words_dict = {}
for letter in words_list:
    words_dict[letter] = []

for word in words:
    first_letter = word[0]
    words_dict[first_letter].append(word)

for key, value in words_dict.items():
    words_dict[key] = sorted(value)

with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(words_dict, file, indent=4)



# words_dict = {}
# for word in words:
#     first_letter = word[0]
#     if first_letter not in words_dict:
#         words_dict[first_letter] = []
#     words_dict[first_letter].append(word)
#
# for key, value in words_dict.items():
#     words_dict[key] = sorted(value)
#
# with open('output.json', 'w', encoding='utf-8') as file:
#     json.dump(words_dict, file, indent=4)
