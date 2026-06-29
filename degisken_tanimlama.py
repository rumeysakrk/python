#KDV Hesaplama

#print (7000+(7000*0.18))
#print (8000+(8000*0.18))

urun1 = 15000
urun2 = 8000
urun3 = 10000
Kdv = 0.20

print (urun1+(urun1*Kdv))
#Değişkenler sayı ile başlamaz.
#Değişkenler arasına boşluk gelmez. "_" kullanılır.

urun4 = 1000
print (urun4)

#Değişkenler tanımlanırken semboller kullanılmaz. urun@ değişkeni oluşturulamaz.
#Değişkenlerde Türkçe karakterler kullanılabilir. Ama diğer dillerde alışkanlık olması için ku
#Python büyük küçük harf duyarlıdır.

sayi=20
SAY1=30
Sayi=40
print (sayi)
print (sayi)
print (Sayi)

#Pythonda tek satırda birden fazla değişkeni tanımlayabiliriz.
a,b,c = 10,20,30
print (a,b, c)

#Tüm değişkenler tek satırda gösterilebilir mi?
a, b, name , isstudent =10 , 40 , "Emir" , False 
print (a,b, name, isstudent)