#markalar = ["opel","nissan","bmw"]
#obj1 = enumerate(markalar)

#print(type(obj1))
#print(list(obj1))

#for index,value in enumerate(markalar):
#    print(f"{index-10}-{value}")

#öğrenciler = ["burak","nil","duru","mehmet"]
#notlar = [90,67,89,67.5]
#for i in range(len(öğrenciler)):
#    s = öğrenciler 
#    g = notlar
#    print(s,g)

#for i in zip(s,g):
#    print(i)


#satış = [4500, 4500, 4500, 4500]
#maliyet = [3000, 4000, 4000, 4000]


#for i in range(len(maliyet)):
#    s = satış[i]
#    c = maliyet[i]    
#    kar = s - c
#    print(f"total kazan: {kar}")

#for s, c in zip(satış,maliyet):
#    kar = s - c
#    print(f"total prfit: {kar}")

#for i in range(1,11):
#    print("---")
#    for k in(1,11):
#        print("{} x {} = {}".format(i,k,(i*k)))


#s = rakamlar = [4,5,6,8,9]
#n = sayılar = [12,14,13,11,10]
# for i in (s):                      SENDE SORUN VAR AMK 
#    print("---")
#    for n in(n):
#        print("{} x {} = {} ".format(s,n,(s*n)))



sayı = int(input("Sayıyı Girin: "))
if sayı > 1:
    for i in range(2, sayı):
        if (sayı % i) == 0:
            print(sayı, " Asal Sayı Değildir. ")
            break
    else:
        print(sayı, "Asal Sayıdır. ")
else:
    print(sayı, "Asal Sayı Değildir. ")


