import random

cara = "-"*60
vybrana_cisla = []
list_cisel=[0,1,2,3,4,5,6,7,8,9]
tipovana_cisla = []


def gen_cisel():
    while len(vybrana_cisla) != 4:
        n= random.choice(list_cisel)
        if n not in vybrana_cisla:
            vybrana_cisla.append(n)
            if vybrana_cisla[0] ==0:
                vybrana_cisla.pop(0)
                m = random.randint(1,9)
                vybrana_cisla.append(m)

def kontrola_tipu_1():
    while True:
        tip_cisel = str(input("Napis svuj typ (ctyrmistne cislo): "))
        tipovana_cisla.append(tip_cisel)
        if len(tip_cisel) != 4:
            print("Nezadal jsi 4 cisla")
        elif not tip_cisel.isdigit():
            print("Nezadal jsi cisla")
        else:
            break



def kontrola_nuly():
    tipovana_cisla.split()



print(f'''
Vitam te v nasi hre!
{cara}
Vygeneruji pro tebe 4 nahodna cisla, ktere musis uhadnout.
Tato hra se jmenuje Bulls and Cows.
{cara}''')

gen_cisel()
kontrola_tipu_1()




print(f"{cara}")
print(vybrana_cisla)
print(tipovana_cisla)







