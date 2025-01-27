lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = []
index = 0
while index < len(lista):
    if lista[index] % 3 == 0:
        talalat.append(lista[index])
    index = index + 1

if talalat:
    print("Van hárommal osztható számok: " + str(talalat))
else:
    print("Nincs hárommal osztható szám!")