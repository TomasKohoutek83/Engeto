import random

#
# list_cisel = []
# for i in range(0,4):
#     n = random.randint (1,9)
#     list_cisel.append(n)

vybrana_cisla = []
list_cisel=[0,1,2,3,4,5,6,7,8,9]


while True:
    n= random.choice(list_cisel)
    print(n)
    if n not in vybrana_cisla and n is not vybrana_cisla[4]:
        vybrana_cisla.append(n)









# cara = "-"*60
#
#
#
# print(f'''
# Vitam te v nasi hre!
# {cara}
# Vygeneruji pro tebe 4 nahodna cisla, ktere musis uhadnout.
# Tato hra se jmenuje Bulls and Cows.
# {cara}''')
# #int(input("Napis svuj typ (ctyrmistne cislo): "))
#
# #print(f"{cara}")
# print(list_cisel)







