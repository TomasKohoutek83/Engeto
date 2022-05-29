import random

cara = "-" * 60
chyba = "Chybné zadání !!!"


# Funkce k vygenerovani hadaneho cislaL?::":>:>efff:>:>
def gen_cisla():
    while True:
        cislo = random.randint(1000, 9999)
        if kontrola_duplicit(cislo):
            return cislo


def kontrola_duplicit(cislo):
    cisla_do_listu = prevod_cisel_list(cislo)
    if len(cisla_do_listu) == len(set(cisla_do_listu)):
        #print(cisla_do_listu)
        return True
    else:
        return False

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


print(f'''
Vítám tě v naší hře Bulls and Cows!
{cara}
Vygeneruji pro tebe čtyřmístné číslo, které musíš uhádnout.
Tvým úkolem je zadat čtyřmístné číslo, ale pozo!! číslo nesmí začínat nulou!! a žádné číslo
se nesmi opakovat.
{cara}''')

gen_cislo = gen_cisla()

while True:
    tip_hrace = (input("Napiš svůj tip: "))
    if not tip_hrace.isdigit():
        print(f"{chyba} Nezadal jsi čísla!!")
        continue

    prevod = int(tip_hrace)

    if not kontrola_duplicit(tip_hrace):
        print(f"{chyba} Tvůj tip obsahuje duplicitu !!!")
        continue

    if prevod < 1000 or prevod > 9999:
        print(f"{chyba} Tvůj tip nejsou 4 čísla nebo číslo začíná nulou!!!")
        continue

    bull_cow = porovani_a_vysledek(gen_cislo, prevod)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")

    if bull_cow[0] == 4:
        print("Gratuluji !!! Přišel jsi na to!!!")
        break

print(f"{cara}")
