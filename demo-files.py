def dosya_kopyalama(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        içerik = file.read()

    with open(yeni_dosya_ismi, "w") as new_file:
        new_file.write(içerik)

#dosya_kopyalama("msg.txt","msg_2.txt")

def ters_cevir(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        içerik = file.read()

    with open(yeni_dosya_ismi, "w") as new_file:
        new_file.write(içerik[::-1])

#ters_cevir("msg.txt","msg_ters.txt")

def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satırlar = file.readlines()

    result = {
        "satır_sayısı": len(satırlar),
        "kelime_sayısı": sum(len(satır.split(' ')) for satır in satırlar ),
        "karakter_sayısı": sum(len(satır) for satır in satırlar)
    }
    return result 

print(bilgilendir("msg.txt"))
print(bilgilendir("newfile.txt"))


