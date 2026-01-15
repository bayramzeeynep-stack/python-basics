sayi= int(input("Sayı giriniz."))

print("Çift sayılar: ")
for i in range(1, sayi+1):
    if i%2==0:
        print(i, end=" ")
      
print("\n Tek sayılar: ")
for i in range(1, sayi+1):
    if i%2!=0:
        print(i, end=" ") 
