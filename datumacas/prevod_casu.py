"""V proměnné apolloStart máme uložený datum a čas startu Apolla 11.
Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané, tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka.
Čas vypisovat nemusíš."""

from datetime import datetime

apolloStart = datetime(1969, 7, 16, 9, 32)
print(apolloStart.strftime("%m/%d/%Y"))
# Output: 07/16/1969