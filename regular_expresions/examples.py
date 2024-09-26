import re
"""
. = jeden libovolny znak                        \d = cislice
[] = jeden znak z uvedenych                     \D = cokoliv krome cislic
[1-5] = jeden znak z intervalu                  \s = bily znak (mezera, tabulator, novy radek)
[a-z] = jeden znak z intervalu                  \S = cokoliv krome bilych znaku
[A-Z] = jeden znak z intervalu                  \w = alfanumericky znak (cislice, pismeno)
[A-Z0-9] = jeden znak z intervalu               \W = cokoliv krome alfanumerickych znaku
{n} = presne n vyskytu                          ^ = zacatek retezce
{n,} = nejmene n vyskytu                        $ = konec retezce
{,n} = nejvyse n vyskytu
{n,m} = od n do m vyskytu
\. = tecka
? = 0 nebo 1 vyskyt
* = 0 nebo vice vyskytu
+ = 1 nebo vice vyskytu
"""
address_pattern = r'\d+ \w+ St, \w+, [A-Z]{2}, \d{5}'
address = "123 Main St, Springfield, IL, 62704"


def check_expression(expression, string):
    if re.match(expression, string):
        print("Format matches.")
    else:
        print("Format does not match.")

check_expression(address_pattern, address)

bank_account_pattern = r'\d{6,10}/\d{4}'
bank_account = "1234569/7890"
check_expression(bank_account_pattern, bank_account)


course_pattern = r'Uvod do programovani 1 - (JavaScript|Python|Java)'
course = "Uvod do programovani 1 - Java"
check_expression(course_pattern, course)


"""
Přidej k regulárnímu výrazu na číslo účtu možnost předčíslí, 
tj. na začátku může být 0 až 6 čísel a za nimi může (ale nemusí) být pomlčka.
"""

bank_account_pattern = r'\d{0,6}-?\d{6,10}/\d{4}'
bank_account = "000-2300117015/2010"
check_expression(bank_account_pattern, bank_account)

"""
Nejmenovaná česká banka rozlišuje typy účtů podle číslic na začátku čísla. 
Například je-li první číslice 1, jedná se o investiční účet, je-li první číslice 2, jde o bankovní účet. 
Uvažujme, že naše tajemná banka má kód (poslední čtyři čísla) 2100.

    Uprav regulární výraz (nemusíš řešit předčíslí) tak, aby na prvním místě mohla být pouze 1 nebo 2.
    Uvažuj, že na druhém místě mohou být jen číslice 0, 1 nebo 2.

"""

bank_account_pattern = r'[12][012]\d{4}/2100'
bank_account = "201234/2100"
check_expression(bank_account_pattern, bank_account)

"""
Standardní registrační značky automobilů, vydané od roku 2004, mají následující formát:

    Na prvním místě je číslo.
    Na druhém místě písmeno, které označuje kraj.
    Na třetím místě je číslo nebo písmeno.
    Na čtvrtém místě je mezera a následuje čtveřice čísel.

Napiš regulární výraz, který bude kontrolovat formát registrační značky. Ověřit si ho můžeš na následujících značkách, které mají správný formát.
"""

license_plate_pattern = r'\d[A-Z]\w \d{4}'
license_plate = "4A6 8244"
check_expression(license_plate_pattern, license_plate)

"""
Zkus nyní regulární výraz ještě zdokonalit a povol na druhém místě pouze znak, který označuje nějaký konkrétní kraj. 
Platné znaky na druhém místě tedy budou tyto: A, B, C, E, H, J, K, L, M, P, S, T, U, Z.
"""

license_plate_pattern = r'\d[ABCEHJKLMPSTUZ]\w \d{4}'
license_plate = "4A6 8244"
check_expression(license_plate_pattern, license_plate)

"""
V Česku máme standardně devítimístná telefonní čísla. Napiš regulární výraz, který sedí na "naše" telefonní čísla.

    Často se telefonní číslo rozděluje na trojice, které jsou odděleny mezerou. 
    Uprav svůj výraz tak, aby odpovídal číslům s mezerou i bez mezery.
    Před telefonní číslo je výhodné přidat mezinárodní předvolbu (v našem případě +420), aby nám mohli volat i lidé ze zahraničí. 
    Přidej to ke svému regulárnímu výrazu.

"""

phone_number_pattern = r'\+420 ?\d{3} ?\d{3} ?\d{3}'
phone_number = "+420 123 456 789"
check_expression(phone_number_pattern, phone_number)

"""
Napiš regulární výraz, který z následujícího řádku vybere celé názvy ministerstev.
Ministerstvo pro místní rozvoj, Celní správa České republiky, Ministerstvo životního prostředí, Ministerstvo práce a sociálních věcí, Český statistický úřad, Nejvyšší kontrolní úřad
"""

ministry_pattern = r'Ministerstvo [^,]+'
ministry = "Ministerstvo pro místní rozvoj, Celní správa České republiky, Ministerstvo životního prostředí, Ministerstvo práce a sociálních věcí, Český statistický úřad, Nejvyšší kontrolní úřad"
check_expression(ministry_pattern, ministry)

"""
Spisová značka, tj. označení spisu u soudu, má zpravidla následující formát:

    číslo soudního oddělení (např. 1 až 2 čísla),
    rejstříková značka (např. jedno až tři velká písmena),
    běžné číslo, podle toho kdy k soudu věc přišla (např. 1 až 4 čísla),
    lomítko a za ním ročník (4 čísla).

Může vypadat například takto: 63 C 397/2014. Napiš regulární výraz a na tomto příkladu jej vyzkoušej.
"""

court_case_pattern = r'\d{1,2} [A-Z]{1,3} \d{1,4}/\d{4}'
court_case = "63 C 397/2014"
check_expression(court_case_pattern, court_case)

"""
Římské číslice se dodnes používají například pro označení století, pořadí panovníků, papežů atd. 
Zkus sestavit regulární výraz, který zachytí římské číslice v následujících řetězcích. 
Nemusíš vytvářet obecný regulární výraz pro římské číslice, ale pouze výraz, který bude fungovat na dané řetězce.

IX. století
Matematika pro VII. třídu
Star Trek III
Karel IV.
papež Benedict V.
Bělá je X. část statutárního města Děčín.
III. patro
II. stupeň povodňové aktivity
Konstantin XI. Dragases

"""

# roman_number_pattern = r'[IVX]+\.?'
roman_number_pattern = r'[IVX]+([ .]|$)'
roman_number = "IX."
check_expression(roman_number_pattern, roman_number)

