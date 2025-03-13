class clas:
    def __init__(self,name,isActive,year):
        self.name = name
        self.isActive = isActive
        self.year = year
    
    def başla(self):
        return(f"Ürün adı :{self.name} Stockta var mı: {self.isActive} ne zaman çıktığı {self.year} ")
    
    def bitiş(self):
        return(f"Kaç sene daha güncelleme alacak : {2030-self.year}")
    
product1 = clas("samsung S23", True, 2023)
product2 = clas("iphone 14",False,2022)

print(product1.başla(),product1.bitiş())
print(product2.başla(),product2.bitiş())

class BankAccount:
    def __init__(self,name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    
hesap = BankAccount("Burak Telli")

print(hesap.getBalance())
hesap.deposit(10000)
print(hesap.getBalance())
hesap.withdraw(4000)
print(hesap.getBalance())

class Pet:
    cinsler = ["Köpek","Kedi","Kuş","Balık"]

    def __init__(self,isim,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins}  evcil hayvan değildir.")
        self.isim = isim
        self.cins = cins

    def cins_öğrenme(self,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins}  evcil hayvan değildir.")
        self.cins = cins

Nugget = Pet("Nugget","Köpek")
Katsu = Pet("Katsu","Kedi")
Farukk = Pet("Farukk","Balık")


print(Farukk.cins_öğrenme("Balık"))


        
                 

    