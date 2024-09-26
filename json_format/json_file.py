import json

with open('absolventi.json', encoding='utf-8') as file:
    absolvents = json.load(file)
print(absolvents)

hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open('hodiny.json', mode='w', encoding='utf-8') as file:
    json.dump(hours, file)

data = {"řeřicha": "Česká Třebová"}
with open("rericha.json", mode="w", encoding="utf-8") as output_file:
    json.dump(data, output_file) # soubor obsahuje {"\u0159e\u0159icha": "\u010cesk\u00e1 T\u0159ebov\u00e1"}

with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)
print(runners)

winner = runners[0]
winner_time = winner["casy"]["oficialni"]
print(winner_time)

