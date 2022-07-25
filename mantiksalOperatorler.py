print("1"=="1") # sağına ve soluna yazılan değerin eşitliğini kontrol eder
print(1 != 2) # sağına ve solunda yazılan değerlerin eşit olmaması durumunu ister
print(1 > 1) # sola yazılan değerin sağa yazılandan büyük olmasını ister
print(1 >= 1) # sola yazılan değerin sağa yazılandan büyük veya eşit olmasını ister

vade = 24
maxVade = 36
kredi = 1000
# true #and #true => true
print(vade > 12 and kredi < 10000) # and - iki koşulun da sağlanmasını istediğimde
print(vade < 12 and kredi < 10000)

#or - iki veya daha fazla koşuldan tek birisinin bile doğru olmasını ister
print(vade < 12 or kredi< 10000)

print(vade < 30 and maxVade == 36 or kredi < 10000)
print((vade > 30 or maxVade == 36) and kredi > 10000)
