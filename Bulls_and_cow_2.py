import random

cara = "-" * 60
generovana_cisla = []
list_cisel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tipovana_cisla = []
chyba = "Chybne zadani !!!"

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


def porovani_a_vysledek(cislo, tip):
    bull_and_cow = [0, 0]
    cisla_do_listu = prevod_cisel_list(cislo)
    tip_do_listu = prevod_cisel_list(tip)

# pouziti metody zip pro slozeni
    for i, j in zip(cisla_do_listu, tip_do_listu):

        # common digit present
        if j in cisla_do_listu:

            # common digit exact match
            if j == i:
                bull_and_cow[0] += 1

            # common digit match but in wrong position
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



#def kontrola_nuly():
    # prvni_cislo =int(tipovana_cisla[0])
    # if prvni_cislo == 0:
    #     print("Cislo zacina nulou!!")
    #     tipovana_cisla.clear()
    #     kontrola_tipu_1()

#def kontrola_duplicit():
    # for cislo in tipovana_cisla:
    #     double = tipovana_cisla.count(cislo)
    #     if double > 1:
    #         print("Duplicita cisel!!")
    #         tipovana_cisla.clear()
    #         kontrola_tipu_1()




print(f'''
Vitam te v nasi hre Bulls and Cows!
{cara}
Vygeneruji pro tebe 4 nahodna cisla, ktere musis uhadnout.
Zadej 4 cisla ktera nesmi zacinat 0 a zadne cislo
se nesmi opakovat.
{cara}''')

gen_cisla()
#kontrola_tipu_1()
#kontrola_nuly()
#kontrola_duplicit()

print(f"{cara}")

# print(tipovana_cisla)
# print(generovana_cisla)








