#"BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste yap
from audioop import reverse


arabalar = "BMW Mercedes Opel Mazda"
arabalar= arabalar.split()
print(arabalar)
#kaç elemanlı?
print(len(arabalar))
#listenin ilk ve son elemanı
print(arabalar[0], arabalar[-1])
#mazda değerini toyata ile değiştir
arabalar[-1]="Toyota"
print(arabalar)
#Mercedes listenin bir elemanı mı?
test = "Mercedes" in arabalar
print(test)
#-2 deki değer
print(arabalar[-2])
#ilk 3 elemanı al
print(arabalar[:3])
#listenin son 2 elamanı yerine "Subaru" ve "TOGG" EKLE
arabalar[-2:]= ["Subaru","TOGG"]
print(arabalar)
#Audi ve nissan ekle
arabalar = arabalar + ["Audi","Nissan"]
print(arabalar)
#son elemanı sil
del arabalar[-1]
print(arabalar)
#tersten yaz listeyi
print(arabalar[::-1])
# studentA: Yiğit Bilgi 2010, (70,50,26)
# studentB: Hamdi Kereste 2006, (77,90,26)
# studentC: Sena Salca 2008, (70,50,63)  liste yapınız
studentA = ["Yiğit","Bilgi", 2010, [70,50,26]]
studentB = ["Hamdi","Kereste", 2006, [77,90,26]]
studentC = ["Sena","Salca", 2008, [70,50,63]]
print(studentA, studentB, studentC)
print(f"{studentA[0:2]} , {studentA[2]} yılında doğmuş olup not ortlaması {(studentA[-1][0]+studentA[-1][1]+studentA[-1][2])/3}")
