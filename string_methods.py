yazi = "Benim adim Rümeysa Kirik. Ankara'da yaşiyorum"
sonuc = yazi.upper() #büyük
print(sonuc)

yazi ="Benim adim Rümeysa Kirik. Ankara'da yaşiyorum."
sonuc = yazi.lower() #küçük
print(sonuc)

yazi ="Benim adim Rümeysa Kirik. Ankara'da yaşiyorum."
sonuc = yazi.title() #büyüklebaşlar
print(sonuc)

#captalize
#islower , isupper (hepsi küçükse ya da büyükse true false olarak yazar)
#cümlenin başına ve sonuna boşluk koyarsan komut strip olursa boşluksuz yazar
#split verilen cümledeki her kelimeyi boşluğa ayırıp teker teker yazar
#split('.')şeklinde yazarsan noktadan sonraki kısmı alır???
#join sonuc="-".join(yazi) verilen cümledeki her kelimeyi - ile ayırır. hangi sembolü koyarsan ya da boşluk koyarsan ona göre ayırır
#sonuc=yazi.index('') //cümle içinde bulmak istediğimiz şeyleri tırnak içine yazarız bize nerede olduğunu kaçıncı karakterde old. söyler
#sonuc=yazi.startswith('B') // Başladığı harfi tırnak içine yazarsak true false olarak verir
#endswith //Sonunu yazar
#replace içine değiştirmek istediklerimizi yazaryz ('Istanbul' , "NYC') //Istanbulu NYC olarak değiştirir
#w3schoolsta string method sitesinden bakabilirsin




