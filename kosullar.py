## koşul yapıları if elif (else if) else
## indent

ortalamaNot = 80

if ortalamaNot < 50:
    print("kaldınız")
elif ortalamaNot >=50 and ortalamaNot <=70:
    print("Normal geçtiniz")
else:
    print("Başarıyla geçtiniz")

print("Her halükarda çalıştırmak istediğim kod")

# kullanıcıdan aldığımız sayıyı çift mi tek mi
sayi = input("Sayıyı giriniz:")
sayi = int(sayi)
if sayi % 2 == 0:
    print("Sayı çifttir")
elif sayi % 2 == 1:
    print("Sayı tektir")
else:
    print("Sayı hesaplanamadı")
