AHesap = { 
        "Ad": "Burak",
        "Hesap No": "12345678",
        "Bakiye": 3000,
        "EkHesap": 2000
}

BHesap = { 
        "Ad": "Ebru",
        "Hesap No": "87654321",
        "Bakiye": 2000,
        "EkHesap": 1000
}

def ParaÇek(Hesap, Miktar):
    print(f"Merhaba {Hesap['Ad']}")

    if (Hesap['Bakiye'] >= Miktar):
        Hesap['Bakiye'] -= Miktar
        print("Paranızı Çekebilirsiniz")
    else:
        toplam = Hesap['Bakiye'] + Hesap['EkHesap']

        if (toplam >= Miktar):
            EkHesapKullanımı = input('Ek Hesap Kullanılsın mı? (e\h)')

            if EkHesapKullanımı == "e":
                print('Paranızı Alabilirsiniz.')
            else:
                print(f"{Hesap['Hesap No']} nolu hesabınızda {Hesap['Bakiye']} bulunmaktadır")
        else:
            print('Limitiniz Yetersizdir')

def Hesap_seç():
    hesap_adı = input("Hangi hesabı seçmek istersiniz  (A/B) : ")

    if hesap_adı.upper() ==  "A":
        return hesap_adı

    elif hesap_adı.upper() == 'B':
        return BHesap
    
secilen_hesap = Hesap_seç()
if secilen_hesap:
    Miktar = float(input("Çekmek istediğiniz miktarı girin: "))
    ParaÇek(secilen_hesap, Miktar)


    
    

 

#ParaÇek(AHesap, 4500)
#ParaÇek(BHesap, 4000)
#print(ParaÇek)
