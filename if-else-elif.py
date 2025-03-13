number = int(input('sayı : '))
if (number > 50) and (number <= 100 ):
    print(f"{number} , 50 ile 100 arasındadır")
else: 
    print(f"{number} , 50 ile 100 arasında değildir")

number = int(input("sayı : "))
if (number > 0):
    if(number % 2 == 1):
        print("Girilen Sayı Pozitif Tek Sayıdır")
    else:
        print("Sayı Pozitif Ve Çift Sayıdır")
else:
    print("Girilen Sayı Negatiftir")

benzinfiyatı = 26.3 
dizelfiyatı = 25.22

OrtalamaYakıtTüketimi = float(input("100 Km Ortalama Yakıt Tüketimi : "))
GidilecekYol = float(input("Gidilecek Yol Kaç Km : "))
YakıtTipi = input("Yakıt Tipiniz Nedir : ")

ToplamYakıtTüketimi = GidilecekYol * (OrtalamaYakıtTüketimi / 100 )

if(YakıtTipi == "benzin"):
    ToplamYakıtÜcreti = (benzinfiyatı * ToplamYakıtTüketimi)
elif (YakıtTipi == "dizel"):
    ToplamYakıtÜcreti = (dizelfiyatı * ToplamYakıtTüketimi)
else:
    print("Yanlış Yakıt Tipi")

print(ToplamYakıtÜcreti)


name = input("İsim : ")
age = int(input("Yaşınız : "))
education = input("Eğitiminiz : ")

if (age >= 18):
    if (education == "lise" or education == "üniversite"):
        print("Ehliyet Alabilirsiniz.")
    else:
        print(f"{name} Ehliyet Alamazsını Çünkü Eğitim Durumu Yetersiz.")
else:
    print(f"Ehliyet Alamazsınız Çünkü Yaşınız Yetersiz.")


quiz1 = float(input("1 sınav notunuz : "))
quiz2 = float(input("2 sınav notunuz : "))
sözlü = float(input("sözlü notunuz : "))

ortalama = (((quiz1 + quiz2) + sözlü * 0.6) / 3 )

if(ortalama >= 0) and (ortalama <= 25):
    print(f"ortalaman: {ortalama} ve notunuz :0 ")
elif(ortalama >= 25) and (ortalama < 45):
    print(f"ortalama : {ortalama} ve notunuz : 1 ")
elif(ortalama >= 45) and (ortalama < 55):
    print(f"ortalama : {ortalama} ve notunuz : 2 ")
elif(ortalama >= 55) and (ortalama < 70):
    print(f"ortalama : {ortalama} ve notunuz : 3 ")
