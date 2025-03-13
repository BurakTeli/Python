name = input("isminizi girin: ")
print("hadi başlayalım " + name )

gizli_kelime = "nugget"

canınız = 10 

puan = 100

kelime_tahmini = ''

while canınız > 0:

    karakterden_kalan = 0
    
    for karakter in gizli_kelime:
        if karakter in kelime_tahmini:
            print(karakter)  
        else:
            karakterden_kalan += 1 
            print("_")
            
    
    if karakterden_kalan == 0:
        print("kazandınız")
        print(f"toplam puan : {puan}")
        break


    tahmin = input("tahmin edin:")
    kelime_tahmini += tahmin

    if tahmin not in gizli_kelime:
        puan -= 10 
        canınız -= 1 
        print("yanlış cevap")

        if canınız or puan == 0:
            print("kaybettiniz")
            #print(f"tahmin etmye çalıştığın kelime = {gizli_kelime}" )
        
