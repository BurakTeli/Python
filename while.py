#i = 3 # başlangıç sayısı
#while i <= 20:    # gideceiği sayıya kadar 
#    if (i % 2 == 0):
#        print('tek sayı:', i)
#    else:
#        print('çift sayı:', i)
#    i += 1  

#username = 'a'

#print(bool(username))


#username = ''
#while not  username:
#    username = input('kulanıcı adınız :')

#print("girdiğimiz kullanıcı adı: ",username)


#sayılar = [4,6,9,10,35,57,89,125,244,367]

# 1: sayılar listesinde while ile ekrana yazdırın 

#for i in sayılar:
#    print(i)

#i = 0
#while  (i<len(sayılar)):
#    print(sayılar[4])
#    i += 1
#i = 0
#while sayılar:
#    if((i % 2 == 0)):
#        if(sayılar.pop()): # pop içerisine 0 yazarsan baştaki sayıları silmeye başlar 
#            print(sayılar)

# 2. başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdır.

#başlangıç = int(input("başlangıç: "))
#bitiş = int(input("bitiş: "))

#i = başlangıç 

#while i < bitiş:
#    i += 1
#    if (i%2==1):
#        print(i)


# 3. 1-100 arasındaki sayıları azlan şekilde yazdırın.

#i = 100 
#while (i>=0):
#    print(i)
#    i -= 1


#sayılar = []
#i = 0 
#while (i<=5):
#    sayı = int(input('sayı: '))
#    sayılar.append(sayı)
#    i += 1

#sayılar.sort()
#print(sayılar)

name = 'burak telli'
for harf in name:
    if (harf == 't'):
        continue
    if (harf == 'l'):
        break
    print(harf)


sayılar = [3,5,4,6,7,13]

for rakam in sayılar:
    if (rakam > 8):
        break
    print(rakam)


#i = 0 
#while (i < 9):
#    i += 1
#    if ( i== 5):
#        continue
#    if ( i == 8):
#        break
#    print(i)

#print("Döngü Bitti")

#i = 1 
#while (i < 100):
#    i +=1 
#    if ( i % 2 == 1):
#        continue
#    if (i == 76):
#        continue
#    if ( i >= 93):
#        break
#    print(i)

#i = 0 
#toplam = 0 

#while ( i <= 100):
#    i += 1 
#    if (i % 2 == 1):
#        continue
#    toplam += i
#    i += 1 

#print(f"toplam: {toplam}")   

#r = range(100)

#a = 0 
#for r in range(50,100,2):
#    a += 1 
#    print(r)
#i = 0
#toplam = 0 
#for i in range(100,200):
#    i += 1
#    if( i % 2 == 1):
#         continue
#    if(i > 156 and i % 2 == 0):
#        break
#    print(i)

import random 

sayı = random.randint(1,67)
hak = 6
sayaç = 0 

while hak > 0:
    hak -= 1
    sayaç += 1 
    tahmin = int(input("Tahmin: "))

    if sayı == tahmin:
        print(f'Tebrikler {sayaç}. Defada Bildiniz. Toplam Puan : {100 - (20) * (sayaç-1) }')
        break
    elif sayı > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"Hakkınız Bitti. Tutulan Sayı : {sayı}")




