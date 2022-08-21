'''
x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6
#kullanıcıdan 2 sayıyı çarp z,x,y toplamı arasındaki farkı bul
#a = int(input("bir sayı gir: "))
#b = int(input("bir tane daha sayı alayım: "))
toplam = int(x + y + z)
#print(a*b-(toplam))
#y nin x e kalansız bölümü
print(y // x)
#x,y,z topla ve mod 3
print(toplam % 3)
# y nin x. kuvveti
print(y**x)
x, *y, z = numbers
print(z**3) 
print(y[0]+y[1]+y[2])
#girilen iki sayıdan hangisi büyük
'''
'''
from unittest import result


a = int(input("bir sayı giriniz: "))
b = int(input("bir sayı giriniz: "))

if a > b:
    print("a, b den büyük")
elif a < b:
    print("a b den küçük")
else:
    print("bu sayılar eşit") 

res = (a > b)
print(f" a: {a} b: {b} den büyük: {res} ")  

#kullanıcıdan vize final bilgisi ile ort. hesapla, geçti ya da kaldı yazdır
viz1 = float(input("1.vize sonucu: "))
viz2 = float(input("2.vize sonucu: "))
fin = float(input("final sonucu: "))
ort = (((viz1+viz2)/2)*(6/10)) + (fin*(4/10)) 
gec = ort > 50
print(f" ortalaman: {ort} ve geçer not aldın : {gec} ")

#tek mi çift mi
a = int(input("bir sayı giriniz: "))
res = ( a % 2 == 0 )
print(f" a: {a} çift sayıdır: {res}")

a = int(input("bir sayı giriniz: "))
poz = (a > 0)
print(f"{a} pozitif bir sayıdır {poz}")
'''
name = input("adınız: ")
surname = input("soyadınız: ")
nameok = (name == "Göksel")
surnameok = (surname == "Özkaya")
print(f"kimlik bilgileri:  {name} geçerli {nameok} soyadınız {surname} geçerli {surnameok} ")


