"""
Vytvoř program, který vypíše výsledek dělení těchto čísel. Program se postupně zeptá na dvě čísla (mohou být celá i desetinná).
Vyděl tato čísla mezi sebou a vypiš výsledek dělení. Ošetři, aby program nezhavaroval při pokusu o dělení nulou.
V tomto případě nemusíš ošetřovat zadání nečíselného vstupu, ošetření více výjimek v jednom bloku si ukážeme v další části.
"""

def divide_numbers():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        result = first_number / second_number
        print(f"The result of division is {result}")
    except ZeroDivisionError:
        print("You can't divide by zero.")
    # except ValueError:
    #     print("You have to enter a number.")

divide_numbers()