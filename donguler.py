# for -- iteration --

ogrenciler = ["Fatih", "Aykut","Eyyub", "Deniz"]
for ogrenci in ogrenciler:
    if(ogrenci.lower()=="fatih".lower()):
        print("OKEY")
# öğrenci ismi Fatih ise ekrana "Okey" yazsın

ogrenciler = ["Fatih", "Aykut","Eyyub", "Deniz"]
for sayi in range(50,100,3): # 50 dahil fakat 100 dahil değil. 3er 3er gider
    if(sayi % 2 == 0):
        print(sayi)

# while
sayac = 0
while sayac < 50:
    print(sayac)
    sayac += 1 # kendisinin üzerine 1 ekler

# kullanıcı x kadar not ortalaması girmek istiyor
# girdiği not ortalamalarında 50'den büyük ve eşit olanlar geçti
# consoleda : "50 dersten 25ini geçtiniz"
# girdiği tüm notları tek tek görmek istiyor

girilecekNotSayisi = int(input("Kaç adet not gireceksiniz?"))
geçilenDersSayisi = 0
girilenNotlar = []
for note in range(girilecekNotSayisi):
    girilenNot = float(input(f"{note+1}. notu giriniz"))
    girilenNotlar.append(girilenNot)
    if(girilenNot >= 50):
        geçilenDersSayisi += 1
print(f"{girilecekNotSayisi} dersten {geçilenDersSayisi} kadar dersi geçtiniz.")
print(f"Girdiğiniz notlar {girilenNotlar}")

i = 0
for girilenNot in girilenNotlar:
    print(f"{i+1}. girdiğiniz not :{girilenNot} ")
    i+=1

#program sonunda girdiği notları kaçıncı not olduğu bilgisiyle beraber yazdır
#kişi direkt ortalama not girmek yerine vize final girecek, siz oradan
#o dersin ortalamasını hesaplayıp geçip kalma durumuna göre işlem yapacaksınız
#vize %40, final %60

vize = int(input("Vize notu:"))
final = int(input("Final notu:"))
ortalama = vize * 0.4 + final * 0.6
if ortalama > 50:
    print(f"Ortalama: {ortalama} Geçtiniz:)")
else:
    print(f"Ortalama: {ortalama} Kaldınız:(")
print(f"Girdiğiniz vize notu: {vize}")
print(f"Girdiğiniz final notu: {final}")



