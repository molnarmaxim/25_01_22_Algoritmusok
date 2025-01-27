szamok = [2, 5, 4, 8, 11, 10, 14, 7, 15]

talalt_szam_indexe = None
index = 0
for index in range(len(szamok)):
    if szamok[index] % 3 == 0:
        talalt_szam_indexe = index
        break

if talalt_szam_indexe:
    print(talalt_szam_indexe)
else:
    print("None")