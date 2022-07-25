print("Operatorler")
sayi = 150
print( sayi + 10)
print( sayi - 10)
print( sayi * 10)
print( sayi / 10)
print("****")
Sayi = sayi + 10
print( sayi + 10)
print( sayi - 10)
print( sayi * 10)
print( sayi / 10)

print(sayi % 2) # mod operatörü

ondalikSayi = 10.5
print( ondalikSayi + 10)
print( ondalikSayi - 10)
print( ondalikSayi * 10)
print( ondalikSayi / 10)

sayi = 100
print(sayi ** 2); # üs alma işlemi
print(sayi //15); # tam bölme işlemi

baslik = "merhaba"
isim = "Engin Demiroğ"
print(baslik + " Etiya")
print(baslik + " Kodlamaio " + "Engin Demiroğ")

## string format
print("{title} Sayın {name}".format(title=baslik,name=isim))


print(baslik*10)

print(baslik.lower())
print(baslik.upper())
print(len(baslik))

# print(17%2)

## input => kullanıcıdan veri alma
vade = input()
print(f"Vadenin tipi ilk başta: {type(vade)}")
vade = int(vade)
vade = vade + 10
print(f"Vadenin tipi dönüşümden sonra: {type(vade)}")
print(f"Girdiğiniz vade: {vade}")






