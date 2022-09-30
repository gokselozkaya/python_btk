def bölenbul(sayi):
    list1 =[]
    
    for num in range(2,sayi):
        if sayi % num == 0:
            list1.append(num)
    print(list1)

print(bölenbul(12))