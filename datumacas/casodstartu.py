"""
Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03. Ulož si hodnotu startu do proměnné.

    Který den v týdnu Solar Orbiter odstartoval?
    Spočítej, kolik času od jeho startu uplynulo.

"""
from datetime import datetime

solar_orbiter_start = datetime(1969, 7, 16, 9, 32)
print(solar_orbiter_start.strftime("%A"))
print(solar_orbiter_start.weekday())
print(solar_orbiter_start.isoweekday() )
print(datetime.now() - solar_orbiter_start)
