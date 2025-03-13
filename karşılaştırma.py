numbers =(3, 5, 7, 8, 9)
number1 = numbers[1]
number2 = numbers[2]

result =(number1 > number2) # True or False 
print(result)

number3 = int(input('sayı 1: '))
number4 = int(input('sayı 2: '))

result2 = (number3 > number4) # True or False 
print(result2)


Numbers = int(input("Sayı : "))
result3 = (Numbers % 2 == 0) # True or False 
print(result3)

number5 = float(input("sayı : "))  # float to int if write 12.5 not WORKİNG
result5 = (number5 > 0) # Pozitif ----- True 
print(f"Girilen sayı pozitif : {result5} ")

visa1 = float(input("vize1 : "))
visa2 = float(input("vize2 :  "))
finale1 = float(input("final1 : "))

result6 = ((((visa1 + visa2) / 2) * 0.60) + (finale1 * 0.40))
result6 = (result6 > 50) # Pozitif ----- True 
        #True == 1  NOT WORKİNG 
print(result6)

_email = "info@sadıkturan.com"
_passwold = "12345"

email = input("email : ")
passworld = input("passworld : ")

isEmail = (email.lower().strip() == _email)
isPassworld = (passworld.strip() == _passwold)

print(f"email doğruluğu : {isEmail} ve parola doğruluğu : {isPassworld}")







