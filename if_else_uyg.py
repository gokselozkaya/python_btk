'''
1- ehliyet alabilir miyim?

name = input("adınız: ")
age = int(input("yasınız: "))
scl = input("egitim durumunuz: ")
if (age >= 18) and (scl == "lise" or scl == "üniversite"):
    print(f"{name} ehliyet almaya uygundur.")
else:
    print(f"{name} ehliyet almaya uygun değildir. "
    
2 - DERSTEN KAÇ ALDIM?

exam1 = float(input("1.sınav sonucu: "))
exam2 = float(input("2.sınav sonucu: "))
exam3 = float(input("sözlü sınnav sonucu: "))
ort = (exam1+exam2+exam3)/3
if ort <=24:
    print("DERSTEN SIFR ALDIN")
elif ort >=25 and ort <=44:
    print("DERSTEN 1 ALDIN")
elif ort >=45 and ort <=54:
    print("dersten 2 aldın")
elif ort >=55 and ort <=69:
    print("dersten 3 aldın")
elif ort >=70 and ort <=84:
    print("dersten 4 aldın")
else:
    print("DERSTEN 5 ALDIN, TEBRİKLER")    

3- araç bakım süresi ?

time = int(input("aracınız kac gundur trafikte?: "))
if time > 364 and time < (365*2):
    print("1.yıl bakımı yapılacak")
elif time >= (365*2) and time < (365*3):
    print("2.yıl bakımınız yapılacak")
elif time >=(365*3) and time < (365*4):
    print("3.yıl bakımı yapılacak ")
else:
    print("süre hatalı")


3.a süre bulma

import datetime
time = input("aracınızın trafiğe çıkış tarihi (yıl/ay/gün): ")
time = time.split("/")
trafık_cıkıs= datetime.datetime(int(time[0]), int(time[1]), int(time[2]))
days = (datetime.datetime.now() - trafık_cıkıs).days
print(days)
'''