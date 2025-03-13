x = int(input("Sayı giriniz: "))
y = int(input("Sayı giriniz: "))
mat = input("Birini seçiniz  +,-,*/ =  ") 


def hesap(x,y,mat):
    if mat == "+" :
        return(str(x) + " " + mat + " " + str(y) + " = " + str(x+y))
    elif mat == "-":
        return(str(x) + " " + mat + " " + str(y) + " = " + str(x-y))
    elif mat == "/":
        return(str(x) + " " + mat + " " + str(y) + " = " + str(x/y))
    elif mat == "*":
        return(str(x) + " " + mat + " " + str(y) + " = " + str(x*y))
    elif mat not in "+-/*":
        return "Bunları seçin +-/*"
        
print(hesap(x,y,mat))

    

    