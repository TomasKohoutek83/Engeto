import random

cara = "-" * 60
generovana_cisla = []
list_cisel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tipovana_cisla = []


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








