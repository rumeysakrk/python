#list
#tuble
#dictionary
#set

markalar = {"Audi","Mercedes","BMW","Honda"}
#sonuc = markalar[0]

#Sorgulama
sonuc = "BMW" in markalar
print(sonuc)

#Yeni eleman ekleyebiliriz
markalar.add("Opel")

markalar.update(["Toyoto","Scoda"])
print(markalar)


sonuc = len(markalar)
print(sonuc)

markalar.remove("Opel")
print(markalar)

sonuc = markalar.pop() #rastgele olarak siler
print(sonuc)

#markalar.clear()

markalar2 = {"Renoult","Toyota","Scoda"}
sonuc = markalar.union(markalar2)
print(sonuc)





