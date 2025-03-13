sayi = int(input("Bir sayi giriniz:")) # Girilen sayi
bayrak = 1 # bayrak baslangicta 1 degerinde,  tum sayilar asal olarak kabul ediyoruz.
           # sayet bir sayiya bolunurse bayrak -> 0 olarak olarak degistirilecek, yani asallik bozulacaktir.

if sayi > 1: #sayi 1'den buyukse asalliga bakiyoruz.
    
    if sayi == 2:
        bayrak = 1 # bayrak 1 olarak kaldi..
    
    for i in list(range(2,sayi)): # 2'den girilen sayiya kadar olan (girilen sayi haric) bir liste
        if sayi % i == 0: #sayi tam bolunuyorusa
            bayrak = 0
            break
            
    if bayrak == 0:
        print("{} sayisi asal sayi degildir..".format(sayi))
    else: #bayrak == 1 ise
        print("{} sayisi asal sayidir..".format(sayi))
        
else: # sayi 1'den kucuk veya esitse asal sayi sarti saglanmaz
    print("Lutfen 1'den buyuk bir sayi giriniz..")

    