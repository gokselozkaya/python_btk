'''
--- girilen sayı 1-100 arası mı

a = int(input("bir sayı giriniz: "))
res = a >= 1 and a <= 100
print(res)

--- girilen sayı pozitif çift sayı mı 

a = int(input("bir sayı giriniz: "))
res = (a > 0) and ( a % 2 == 0 )
print(res)

--- e-mail ve parola ile giriş kontrolü

mailadres = input("mail adresi: ")
parola = input("parola: ")
adres = "kk@gmail.com"
par = "1234kk"
res = mailadres == adres and parola == par
print(f"adres ve parola geçerli : {res} ")

--- girilen 3 sayıyı büyüklük açısından karşılaştır

x = int(input(" x değeri giriniz: "))
y = int(input(" y değeri giriniz: "))
z = int(input(" z değeri giriniz: "))

if x > y and x > z:
    print("x en büyük sayıdır")
elif y > x and  y > z:
    print("y en büyük sayıdır")
    if z > x and z > y:
        print("z en büyük sayıdır")
else:
    print("aynı sayılar girmayin lütfen!!!")
    x = int(input(" x değeri giriniz: "))
    y = int(input(" y değeri giriniz: "))
    z = int(input(" z değeri giriniz: "))
    if x > y and x > z:
        print("x en büyük sayıdır")
    elif y > x and  y > z:
        print("y en büyük sayıdır")
        if z > x and z > y:
            print("z en büyük sayıdır")


            
--- 2 vize bir  final. > 50 is geçer
    - final 50 olmalı
    - final 70 ise ortalama önemli değil

vize1 = float(input("1. vize sonucu: "))    
vize2 = float(input("2. vize sonucu: "))    
final = float(input("final sonucu: "))    
ort = (((vize1+vize2)/2)*(0.6) + (0.4)*final)
res = ((final > 49) and  (ort > 49)) or (final > 69)
print(f"{ort} ile geçer not aldınız:{res}")

---ad, kilo ve boy ile kilo endeksi hesapla
    - kilo/boy**2 = formül
    - 0-18.4 zayıf
    - 18.5 - 24.9 normal
    - 25- 29.9 fazla kilo
    -30- 34.9 obez
'''
name = input("adınız: ")
kilo = float(input("kilonuz: "))
boy = float(input("boy: "))
form = kilo/(boy**2)
if form > 0 and form < 18.4:
    print(f"{name} zayıftır.")
elif form > 18.5 and form < 24.9:
    print(f"{name} normal kilodadır.")
    if form > 25 and form < 29.9:
        print(f"{name} fazla kiloludur.")
else:
    print(f"{name} obezdir.")            




