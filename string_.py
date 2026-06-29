name = 'Rümeysa'
surname = 'Kirik'
age = '20'

print('My name is {}'.format (name))
print('My name is {}{}'.format(name,surname))
print('My name is {1}{0}'.format(name,surname)) #sırayı değiştirmek iiçin bu şekilde yazabilirisin
print('My name is {n}{s}'.format(n=name,s=surname))
print('My name is {}{}. I am {} years old.' .format(name,surname,age))

number=5/3
print('The result {n:1.3}' .format(n=number))
#Bölümde elde edilen sayı ondalıklı ise n:1.3 şeklinde virgülden sonra 3 basamağı gösterir