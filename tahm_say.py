'''
#kelimeyi belirtilen kez göster
def shw(x,y):
    return x*y
shw("selam\n", 10)
#gönderilen parametreleri listeye çevir
def mklist(*params):
    list1= []
    for p in params:
        list1.append(p)
    return list1
res = mklist(5,9,"hello",96,[5,8])
print(res)

# sayı asal mıdır?
sayi = int(input("sayı giriniz: "))
asaldır = True

if sayi == 1:
    asaldır = False

for num in range(2, sayi):
    if (sayi % num == 0):
        asaldır= False
        break

if asaldır:
    print(f"{sayi} asal sayıdır")        
else: 
    print(f"{sayi} asal değil")
'''

def asalbul(x,y):
        for num in range(x,y):
            if num>1:
                for i in range (2,num):
                 if num%i ==0:
                    break
                else:
                    print(num)


res = asalbul(2,9)
print(res)  

        
