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

   
           
        
def zadani_cisla():
        tip_cisel = (input("Napis svuj tip: "))
        for x in tip_cisel:
            tipovana_cisla.append(x)
        kontrola_pismen(tip_cisel)
        kontrola_poctu(tip_cisel)
        kontrola_duplicit(tipovana_cisla)
        kontrola_nuly(tipovana_cisla)
        
        
def kontrola_pismen(tip_cisel):
    if not tip_cisel.isdigit():
        print(f"{chyba} Nezadal jsi cisla!!")
        tipovana_cisla.clear()
        zadani_cisla()
        
              
def kontrola_poctu(tip_cisel):
    if len(tip_cisel) != 4:
        print(f"{chyba}Nezadal jsi 4 cisla!!")
        tipovana_cisla.clear()
        zadani_cisla()
               

def kontrola_nuly(tipovana_cisla):
    prvni_cislo = int(tipovana_cisla[0])
    if prvni_cislo == 0:
        print(f"{chyba} Cislo zacina nulou!!")
        tipovana_cisla.clear()
        zadani_cisla()
        
        
def kontrola_duplicit(tipovana_cisla):
    for cislo in tipovana_cisla:
        double = tipovana_cisla.count(cislo)
        if double > 1:
            print(f"{chyba}  Duplicita cisel!!")
            tipovana_cisla.clear()
            zadani_cisla()
            
            
print(f'''
Vitam te v nasi hre Bulls and Cows!
{cara}
Vygeneruji pro tebe 4 nahodna cisla, ktere musis uhadnout.
Zadej 4 cisla ktera nesmi zacinat 0 a zadne cislo
se nesmi opakovat.
{cara}''')

gen_cisel()
print(generovana_cisla)
zadani_cisla()
print(cara)
print(tipovana_cisla)
