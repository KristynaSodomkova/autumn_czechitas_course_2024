"""
Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47.
Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund.
Kdy očekáváme, že jídlo dorazí zákazníkovi?
"""

from datetime import datetime, timedelta

order_time = datetime(2020, 11, 13, 19, 47)
takeover_time = timedelta(minutes=8, seconds=35)
preparation_time = timedelta(minutes=30)
delivery_time = timedelta(minutes=25, seconds=30)

expected_time = order_time + takeover_time + preparation_time + delivery_time
print(expected_time)
