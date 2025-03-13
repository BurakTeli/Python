AHesap = { 
        "Ad" : "Burak",
        "Hesap No" : "12345678",
        "Bakiye" : 3000,
        "EkHesap" : 2000
}


BHesap = { 
        "Ad" : "Ebru",
        "Hesap No" : "87654321",
        "Bakiye" : 2000,
        "EkHesap" : 1000
}

def ParaÇek(Hesap, Miktar):
    print(f"Merhaba {Hesap['Ad']}")

    if (Hesap['Bakiye'] >= Miktar):
        Hesap['Bakiye'] -= Miktar
        print("Paranızı Çekebilirsiniz")
    else:
        toplam = Hesap['Bakiye'] + Hesap['EkHesap']

        if (toplam >= Miktar):
            EkHesapKullanımı : input('Ek Hesap Kullanılsın mı? (e\h)')

            if EkHesapKullanımı == "e" :
                print('Paranızı Alabilirsiniz.')
            else:
                print(f"{Hesap['HesapNo']} nolu hesabınızda {Hesap['Bakiye']} bulunmaktadır")
        else:
            print('Limitiniz Yetersizdir')

#ParaÇek(AHesap, 2000)
ParaÇek(BHesap, 3000)
print(ParaÇek)
        


# Doğru olan (ek hesap çalışıyor) Bundada sıkıntı var 



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

#ParaÇek(AHesap, 2000)
ParaÇek(BHesap, 3000)
