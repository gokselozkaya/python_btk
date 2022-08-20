'''
ögrenciler={
    "120":{
        "ad":"Ali",
        "soyad": "Yılmaz",
        "telefon":"506 500 30 63"
    },
    "125":{
        "ad":"Can",
        "soyad":"Korkmaz",
        "telefon":"532 632 51 29"
    },
    "128":{
        "ad":"Volkan",
        "soyad":"Yükselen",
        "telefon":"529 506 78 93"
    }
}
#bilgileri verilen öğrencileri kullanıcıdan gelenlerle dictionary de sakla

'''

ögrenciler_kayıt={}
i=0
for i in range(3):
    number = input( "ögrenci no: ")
    name1 = input("ögrenci adı: ")
    Surname1= input("ögrenci soyadı: ")
    mobilenumber= input("ögrenci telefon numarası: ")
    ögrenciler_kayıt.update({
    number: {
        "ad": name1,
        "soyad": Surname1,
        "telefon": mobilenumber
    }
    })
    i+=1
'''
ögrenciler_kayıt[number]={
    "ad": name1,
    "soyad": Surname1,
    "telefon": mobilenumber
}
print(ögrenciler_kayıt)
'''
print(ögrenciler_kayıt)
