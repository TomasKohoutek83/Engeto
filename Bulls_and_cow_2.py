import random

cara = "-" * 60
chyba = "Chybne zadani !!!"


# Funkce k vygenerovani hadaneho cisla
def gen_cisla():
    while True:
        cislo = random.randint(1000, 9999)
        if kontrola_duplicit(cislo):
            return cislo


def kontrola_duplicit(cislo):
    cisla_do_listu = prevod_cisel_list(cislo)
    if len(cisla_do_listu) == len(set(cisla_do_listu)):
        print(cisla_do_listu)
        return True
    else:
        return False

def prevod_cisel_list(cislo):
    return [int(i) for i in str(cislo)]



#Funkce pro zjisteni bull and cow. Porovnani pozice mezi listy
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



def kontrola_tipu_1():
    while True:
        tip_cisel = (input("Napis svuj tip: "))
        prvni = int(tip_cisel[0])
        for cislo in tip_cisel:
            double = tip_cisel.count(cislo)
            if double > 1:
                print(f"{chyba}Duplicita cisel!!")
                break
        if len(tip_cisel) != 4:
            print(f"{chyba}Nezadal jsi 4 cisla!!")
        elif not tip_cisel.isdigit():
            print(f"{chyba}Nezadal jsi cisla!!")
        elif prvni == 0:
            print(f"{chyba}Cislo zacina nulou!!")

        else:
            for x in tip_cisel:
                tipovana_cisla.append(x)
                break

print(f'''
Vitam te v nasi hre Bulls and Cows!
{cara}
Vygeneruji pro tebe 4 nahodna cisla, ktere musis uhadnout.
Zadej 4 cisla ktera nesmi zacinat 0 a zadne cislo
se nesmi opakovat.
{cara}''')

gen_cislo = gen_cisla()

while True:
    tip_hrace = int(input("Napis svuj tip: "))

    if not kontrola_duplicit(tip_hrace):
        print(f"{chyba} Tvuj tip obsahuje duplicitu !!!")
        continue
    if tip_hrace < 1000 or tip_hrace > 9999:
        print(f"{chyba} Tvuj tip ma vice nez 4 cisla!!!")
        continue

    bull_cow = porovani_a_vysledek(gen_cislo, tip_hrace)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")


    if bull_cow[0] == 4:
        print("Dobra prace !!! Prisel jsi na to!!!")
        break

print(f"{cara}")










