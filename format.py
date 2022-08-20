from unittest import result


website = "http://www.google.com"
course = "python kursu"
# kursta kaç karakter var?
result = len(course)
result1 = len(website)
print(result)
# www ifadesini alınız
print(str(website[7:10]))
# com u alınız
print(str(website[result1-3:result1]))
#course içinden ilk 5 i ve son 5 i alınız 
print(str(course[0:6]))
print(str(course[result-5:result])) 
#course u tersten yazın
print(str(course[::-1]))
#verilen değişkenlerle  my name is Göksel Özkaya, I am 32 yazdıralım
name, surname, age = "Göksel", "Özkaya" , "32"
print(f"Benim adım {name} {surname}, ben {age} yaşındayım")
selam = "Hello world"
selam1= selam[:6] + "W" + selam[7:]
print(selam1)
# abc yi 5 kere yazdır
tekrar = "abc" * 5 
print(str(tekrar))



