iller = ["İstanbul","Ankara","İzmir","Bursa"]
sonuc = iller[0:2]
print(sonuc)

iller[0]="Tekirdağ" 
print(iller)
iller[-1] ="Balıkesir"
print(iller)
#Listenin eleman sayisini almak için
sonuc = len(iller)
print(sonuc)

#Listeye elaman eklemek için 
sonuc = iller + ["Adana","Antalya"]
print(sonuc)

#Listedeki elemanları silmek için
del iller[0]
print(iller)


