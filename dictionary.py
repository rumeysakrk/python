#34 => İstanbul
#35 => İzmir
#sehirler = ["İstanbul" ,"İzmir"]
#plakalar = [34,35]
#print(plakalar[0],sehirler[0])
#print(plakalar[1],sehirler[1])

#print(plakalar[sehirler.index("İstanbul")])
#print(plakalar[sehirler.index("İzmir")])                             
                    
#key-value
#plakalar = {"İzmir":35,"İstanbul":34}
#print(plakalar["İstanbul"])

#sözlüğün içerisine eleman eklemk için
#plakalar["Eskişehir"] = 26
#plakalar["Bursa"] = 16

#print(plakalar)

urunler = {
    100:{
        "urunAdi" : "Monitor",
        "urunaciklamasi" :"16 inç",
        "garanti süresi" : 3,
        "fiyati" :[800,914],
    },
    101:{
        "urunAdi" : "SSD",
        "urunaciklamasi" :"Monitor",
        "garanti süresi" : 2,
        "fiyati" :[1500,1770],
    }
}

sonuc = urunler
print(sonuc)
print(type(urunler))

sonuc = urunler[101]["garanti süresi"]
print(sonuc)





