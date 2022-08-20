from itertools import count
from tkinter import Y


names = ["Ali","Yağmur","Murat","Deniz"]
years = [1995, 1993, 1993, 1999]
#Cenki sona ekle
names.append("Cenk")
print(names)
#Senayı başa ekle
names.insert(0, "Sena")
print(names)
#denizi listeden sil
names.remove("Deniz")
print(names)
#Yağmur indeksi
index1= names.index("Yağmur")
print(index1)
#ali listenin elemanı mı?
count1=names.count("Ali")
print(count1)
#ters çevir listeyi
names.reverse()
print(names)
#sırala
names.sort()
print(names)
years.sort()
print(years)
# str = "Chev", "Dacia" listeye çevir
str = "Chev, Dacia"
list1 = str.split(",")
print(list1)
# min years and max years
print(min(years), max(years))   
# kaç tane 1993 var
print(years.count(1993))
#years tüm elemanları sil
years.clear()
print(years)
#arac sor 3 kere ve listeye ekle
aracmarkaları = []
i=0
for i in range(3):
    marka = input("arac markası gir: ")
    aracmarkaları.append(marka)
    i += 1
print(aracmarkaları)