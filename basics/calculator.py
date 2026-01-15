sayi= float(input("Sayı gir."))
sayi1= float(input("Sayı gir."))
print("İşlem seç: (+, /, *, -)")
islem= input("İşlem: ")
if islem=="+":
    print("Sonuç:", sayi+sayi1)
elif islem=="-":
    print("Sonuç:", sayi-sayi1)
elif (islem=="/" and sayi1!=0):
    print("Sonuç:", sayi/sayi1)
elif islem=="*":
    print("Sonuç:", sayi*sayi1)
else:
    print("Geçersiz işlem.Tekrar deneyiniz.")
    
