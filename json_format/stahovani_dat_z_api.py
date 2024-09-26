import requests

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()
# print(data)

# [{'first_name': 'Frederic', 'last_name': 'Trusler', 'email': 'ftrusler0@whitehouse.gov', 'gender': 'Male'}, ...

"""
Jak už jsme si ověřili v lekci, datové API na adrese https://api.kodim.cz/python-data/people obsahuje seznam lidí. 
Napište program, který tento seznam z API stáhne a převede z formátu JSON na Python slovníky. 
Proveďte následující úkoly.

    Zjistěte kolik lidí celkem seznam obsahuje.
    Zjistěte jaké všechny informace máme o jednotlivých osobách.
    Zjistěte, kolik je v souboru mužů a žen.

"""

print(len(data))
information = []
first_person = data[0]
for key in first_person:
    information.append(key)
print(information)

males = 0
females = 0
for person in data:
    if person["gender"] == 'Male':
        males += 1
    if person["gender"] == 'Female':
        females += 1
print(males)
print(females)

# print(len([person for person in data if person['gender'] == 'Male']))
