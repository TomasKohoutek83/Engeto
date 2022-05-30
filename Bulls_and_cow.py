"""
projekt_2: Druhz projekt do Engeto Online Python Akademie

author: Tomas Kohoutek
email: Tomas.kohoutek83@gmail.com
discord: Tomáš - kokes#4989


Komentar ke kodu:
Pro posouzeni posilam asi 4 verzi tohoto kodu. Musim priznat ze me to celkem potrapilo.
Ve finale je to funkcni, ale kod je trosku chaoticky. Hlavni cast porgramu ve funkcich nebyla tak
uplne tezka, ale naslednymi podminkami napr: cislo nesmi zacinat nulou nebo nesmi byt cislo,  mi
to podminkz celkem s komplikovaly.
Ale funguje to :)

"""

import random

# Zakladni promene
cara = "-" * 60
chyba = "Chybné zadání !!!"


# Funkce k vygenerovani hadaneho cisla
def gen_cisla():
    while True:
        cislo = random.randint(1000, 9999)
        if kontrola_duplicit(cislo):
            return cislo

# Funkce ke kontrole duplicit.


def kontrola_duplicit(cislo):
    cisla_do_listu = prevod_cisel_list(cislo)
    if len(cisla_do_listu) == len(set(cisla_do_listu)):
        #print(cisla_do_listu)
        return True
    else:
        return False

# Funkce pro prevod do potrebnho formatu. Listy


def prevod_cisel_list(cislo):
    return [int(i) for i in str(cislo)]


# Funkce pro zjisteni bull and cow. Porovnani pozic mezi listy
def porovani_a_vysledek(cislo, tip):
    bull_and_cow = [0, 0]
    cisla_do_listu = prevod_cisel_list(cislo)
    tip_do_listu = prevod_cisel_list(tip)

    # pouziti metody zip pro slozeni
    for i, k in zip(cisla_do_listu, tip_do_listu):

        # zjisteni pozice a uprava promene bull_and_cow
        if k in cisla_do_listu:
            if k == i:
                bull_and_cow[0] += 1
            else:
                bull_and_cow[1] += 1

    return bull_and_cow


# Vypis funkcnosti a pravidel hry.
print(f'''
Vítám tě v naší hře Bulls and Cows!
{cara}
Vygeneruji pro tebe čtyřmístné číslo, které musíš uhádnout.
Tvým úkolem je zadat čtyřmístné číslo, ale pozor!! 
číslo nesmí začínat nulou!! a žádné číslo
se nesmi opakovat.
{cara}''')

# Spousteni generovani cisla
gen_cislo = gen_cisla()
pokusy = int(input("Napiš na kolik pokusů si troufáš: "))

# Smycka pro kontrolu hodnot a vysledek hry
while pokusy >0:
    tip_hrace = (input("Napiš svůj tip: "))
    if not tip_hrace.isdigit():
        print(f"{chyba} Nezadal jsi čísla!!")
        continue
# Pomocny prevod na int
    prevod = int(tip_hrace)

    if not kontrola_duplicit(tip_hrace):
        print(f"{chyba} Tvůj tip obsahuje duplicitu !!!")
        continue

    if prevod < 1000 or prevod > 9999:
        print(f"{chyba} Tvůj tip nejsou 4 čísla nebo číslo začíná nulou!!!")
        continue

    bull_cow = porovani_a_vysledek(gen_cislo, prevod)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    pokusy -= 1

    if bull_cow[0] == 4:
        print("Gratuluji !!! Přišel jsi na to!!!")
        break
    
else:
    print(f"Zřejmě jsi přecenil svoje síly :) . Hadané číslo bylo {gen_cislo}" )

print(f"{cara}")
