x = 76
y = 33

result1 = (x % 2 == 0  )
result  = 50 < x < 100 and 22 < y < 45



Email = "bucketles612@gmail.com"
Passworld = "12345"

email = input('Email : ')
passworld = input('Passwold : ')

isemail = (email.lower().strip() == Email) 
ispassworld = (passworld.strip() == Passworld)

print(f"email doğruluğu : {isemail} ve parola doğruluğu : {ispassworld}")



number = int(input('number: '))
result = ((number > 50 ) and (number <= 100) and (number % 2 == 0))
print(f"{number} :  50 ile 100 arasında ve çift sayı : {result} ")

number = int(input('number : '))
result = (number > 0 ) and (number % 2 == 1)
print(result)  




x  = int(input('x : '))
y  = int(input('y : '))
z  = int(input('z : '))

result = ( x > y ) and (x > z) # X En Büyük 
print(" X  En büyük Sayı : " , result )
result = ( y > x ) and (y > z) # Y En Büyük 
print(" Y  En Büyük Sayı : " , result)
result = ( z > x ) and (z > y) # Z En Büyük 
print(" Z  En Büyük Sayı : " , result )


visa1 = float(input('vize1 : '))
visa2 = float(input('vise2 : '))
final = float(input('final : '))

average = ((((visa1 + visa2) / 2)  * 0.6) + (final * 0.4))
print(f"Öğrenci Not Ortalaması : {average} ve Geçme Durumu : {average >= 50}" )



ad = input('Adınız : ')
kg = float(input('Kilonuz : '))
hg = float(input('Boyunuz : '))

kiloindeks = (kg / ( hg ** 2 ))

Zayıf = (kiloindeks >= 0 ) and (kiloindeks <= 30.5)
Normal = (kiloindeks > 30.5) and (kiloindeks <= 56.7)
Kilolu = (kiloindeks > 56.7 ) and (kiloindeks <= 80.6)
Obez = (kiloindeks >= 80.6) and (kiloindeks <= 122.4)
print(f"{ad} Kilo İndeksi : {kiloindeks} ve Kilo Değerlendirme : {Zayıf}")
print(f"{ad} Kilo İndeksi : {kiloindeks} ve Kilo Değerlendirme : {Normal}")
print(f"{ad} Kilo İndeksi : {kiloindeks} ve Kilo Değerlendirme : {Kilolu}")
print(f"{ad} Kilo İndeksi : {kiloindeks} ve Kilo Değerlendirme : {Obez}")

