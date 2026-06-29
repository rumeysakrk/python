arabaAudi = {
    "marka" : "Audi",
    "model" : "A5",
    "yil" : "2019",
}

#Değerlere erişmek için
sonuc = arabaAudi["marka"]
sonuc = arabaAudi.get("marka")

#Sorgulama işlemleri
#sonuc = "marka" in arabaAudi

sonuc =len(arabaAudi)
print(sonuc)

#Ekleme işlemleri için
arabaAudi["renk"] = "siyah"
print(arabaAudi)

#Silme işlemleri
#arabaAudi.pop("yil")
#arabaAudi.popitem()
#print(arabaAudi)

#del arabaAudi
#print(arabaAudi) #Hata

#arabaAudi.clear()

#Objeyi kopyalamak için
#araba = arabaAudi.copy()
#araba ["marka"] = "Mercedes"
#araba ["yil"] ="2026"
#print(araba)

#Diğer bir güncelleme metodu
araba = arabaAudi.update({
    "marka" : "BMW",
    "renk" : "beyaz",
})
print(arabaAudi)







