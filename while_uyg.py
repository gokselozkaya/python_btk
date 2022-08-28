sayilar=[1, 3, 5, 7, 9, 12, 19, 21]
'''
#while ile listeyi yazdır
i= 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1

#başlangıç ve bitişi al. aradaki tekleri yazdır
x = int(input("başlangıç sayısı: "))
y = int(input("bitiş sayısı: "))
i=x+1
while i<y:
    if i %2 !=0:
        print(i)
    i += 1
#1-100 arasındaki sayıları azalan şekilde yazdır
i = 100
while i >0:
    i -= 1
    print(i)
#5 sayı al ve sıralı yazdır
list=[]
i=0
while i<5:
    num = int(input("sayı: "))
    list.append(num)    
    i += 1
list.sort()
print(list)

# sınırsız üründen oluşan dic (name,price) oluştur
list=[]
num = int(input("ürün sayısını girin: "))
i = 0
while i<num:
    n = input("ürün adını girin: ")
    p = input("ürün değeri: " )
    list.append({
        "name":n,
        "price":p
         })
    i += 1
print(list)
'''









        
        


