website = "http://google.com.tr"
course = "Baz Vektörler ve 3 boyutlu gösterimleri"
# " hello world " başındaki ve sonundaki boşluklar silinsin
dizi1 = " hello world "
dizi1= dizi1.strip()
print(dizi1)
dizi2= website.lstrip("tp")
print(dizi2)
# "www.harikaadam.com" harikaadam hariç silin
print("www.harikaadam.com".strip("w.").rstrip("com"))
# couse değişkenleri komple küçük olsun
print(course.lower())
#website içinde kaç tane o var
print(website.count("o"))
#website www ile başlayıp tr ile bitiyor mu
print(website.startswith("http"))
print(website.endswith("tr"))
#website içinde com ifadesi var mı?
print(website.find("com"))
print(website.find("com", 3, 7))
print(course.find("boyut"))
#contents ifadesini satırda 50 karakter içine sokup sağına ve soluna * ekle
islem= "contents"
print(islem.center(50,"*"))
print(islem.ljust(50,"-"))
#coursedizisindeki boşlukları - ile değiştir
print(course.replace(" ", "-"))
# hello world ifadesinde hello yerinde goodbye olsun
print("hello world".replace("hello","goodbye"))
#course u boşluklardan ayırın
print(course.split(" "))




