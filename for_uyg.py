sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
'''
#sayılar listesindeki hangi sayılar üçün katı?
for _ in sayilar:
    if _ %3 == 0: 
        print(_)

#toplamları ne?
top = 0
for _ in sayilar:
    top += _
print(top)

#tek sayıların karesi

for _ in sayilar:
    if _ %2 != 0:
        print(_**2)


#şehirlerden hangileri en fazla beş karakterli

cities = ["kocaeli","ıstanbul","ankara","izmir","rize"]
for c in cities:
    if len(c) <= 5:
        print(c)

ürünler=[
    {"name":"samsung S6","price":"3000"},
    {"name":"samsung S7","price":"4000"},
    {"name":"samsung S8","price":"5000"},
    {"name":"samsung S9","price":"6000"},
    {"name":"samsung S10","price":"7000"},
]

#ürünlerin fiyatları toplamı
top=0
for i in ürünler:
    top += int(i["price"])
print(top)
    
#fiyatı en fazla 5000 olanları göster
for i in ürünler:
    if int(i["price"]) <=5000:
        print(i["name"])
'''
