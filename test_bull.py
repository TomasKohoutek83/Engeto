import random



tipovana_cisla = ['0','1']
if tipovana_cisla[0] > 0:
    print("Cislo zacina nulou")


def kontrola_tipu_1():
    while True:
        tip_cisel = str(input("Napis svuj typ (ctyrmistne cislo): "))

        if len(tip_cisel) != 4:
            print("Nezadal jsi 4 cisla")
        elif not tip_cisel.isdigit():
            print("Nezadal jsi cisla")
        else:
            for x in tip_cisel:
                tipovana_cisla.append(x)
            break


def kontrola_nuly():
    if tipovana_cisla[0] == 0:
        print("Cislo zacina nulou")


# kontrola_tipu_1()
# kontrola_nuly()



print(tipovana_cisla[0])
