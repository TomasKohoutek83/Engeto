import random


vybrana_cisla = []
list_cisel=[0,1,2,3,4,5,6,7,8,9]

for n in range(0,4):
    n = random.randint (0,9)
    if n not in vybrana_cisla:
        vybrana_cisla.append(n)

print(vybrana_cisla)



# def vyber():
#     n= random.choice(list_cisel)
#     if n not in vybrana_cisla:
#         vybrana_cisla.append(n)
#     elif vyber():
#         n = random.choice(list_cisel)
#         if n not in vybrana_cisla:
#             vybrana_cisla.append(n)

# vyber()








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







