lista = ["kék", "zöld", "piros", "fehér"]

if 'piros' in lista:
    print("Van piros a listában")
else:
    print("Nincs piros a listában")

print(lista.count('piros'))

#for - lista elemek
mennyi = 0
for elem in lista:
    if elem == 'piros':
        mennyi += 1
print(mennyi)

#for ciklus index-szel
hanyszor_fordul_elo = 0
for index in range(len(lista))