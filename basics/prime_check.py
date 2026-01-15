sayi= int(input("Sayi giriniz:"))
if sayi<2:
    print("Asal sayı değildir.")
else:  
    for i in range(2, sayi):
        if sayi%i==0:
            print(sayi, "Asal sayı değildir.")
            break
    else: 
        print(sayi,"Asal bir sayıdır.")
