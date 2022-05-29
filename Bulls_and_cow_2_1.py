'''
 Ke staremu dodon vypocet na finalni hodnoceni
'''
import random

cara = "-" * 60
generovana_cisla = []
list_cisel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tipovana_cisla = []
chyba = "Chybne zadani !!!"


def gen_cisel():
    while len(generovana_cisla) != 4:
        n = random.choice(list_cisel)
        if n not in generovana_cisla:
            generovana_cisla.append(n)
            if generovana_cisla[0] == 0:
                generovana_cisla.pop(0)
                m = random.randint(1, 9)
                generovana_cisla.append(m)


def kontrola_tipu_1():
    while True:
        tip_cisel = (input("Napis svuj tip: "))

        if len(tip_cisel) != 4:
            print("Nezadal jsi 4 cisla!!")
        elif not tip_cisel.isdigit():
            print("Nezadal jsi cisla!!")
        else:
            for x in tip_cisel:
                tipovana_cisla.append(x)
            break


def kontrola_nuly():
    prvni_cislo =int(tipovana_cisla[0])
    if prvni_cislo == 0:
        print("Cislo zacina nulou!!")
        tipovana_cisla.clear()
        kontrola_tipu_1()

def kontrola_duplicit():
    for cislo in tipovana_cisla:
        double = tipovana_cisla.count(cislo)
        if double > 1:
            print("Duplicita cisel!!")
            tipovana_cisla.clear()
            kontrola_tipu_1()




print(f'''
Vitam te v nasi hre Bulls and Cows!
{cara}
Vygeneruji pro tebe 4 nahodna cisla, ktere musis uhadnout.
Zadej 4 cisla ktera nesmi zacinat 0 a zadne cislo
se nesmi opakovat.
{cara}''')
print()

gen_cisel()
kontrola_tipu_1()
kontrola_nuly()
kontrola_duplicit()

print(f"{cara}")

print(tipovana_cisla)







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


 bull_cow = porovani_a_vysledek(gen_cislo, tip_hrace)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")


    if bull_cow[0] == 4:
        print("Dobra prace !!! Prisel jsi na to!!!")
        break














