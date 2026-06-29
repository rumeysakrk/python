#sayilar = [1,2,3,8,12,16]
#print(sayilar[0])
#print(sayilar[1])
#print(sayilar[2])
#print(sayilar[3])
#print(sayilar[4])
#print(sayilar[5])

#for i in sayilar:
   # print(i)

isim = "Rümeysa Kirik"
for i in isim:
    print(i)

tuple =[(1,2),(3,4),(6,9)]
for a,b in tuple:
    print(a,b)

plakalar ={"İzmir":35,"İstanbul":34}
for x in plakalar:
    print(x)

for x in plakalar.keys():
    print(x)

for key,value in plakalar.items():
    print(key,value)

sayilar =[]   

for i in range(1,6):
    sayi = float(input(f"{i}.sayiyi giriniz: "))
    sayilar.append(sayi)

toplam = sum(sayilar)
ort = toplam / len(sayilar)
en_buyuk = max(sayilar)

print("\n-----Sonuçlar------")
print(f"Girdiğiniz Sayilar: {sayilar}")
print(f"toplam: {toplam}")
print(f"ortalama: {ort}")
print(f"maksimum: {en_buyuk}")



