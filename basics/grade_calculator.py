vize= int(input("Vize notunuzu giriniz."))
final= int(input("Final notunuzu giriniz."))

öğrencinotortalaması= vize*0.6+final*0.4

if (öğrencinotortalaması>=95 and öğrencinotortalaması<=100):
     print("AA")
if (öğrencinotortalaması>=90 and öğrencinotortalaması<=94):
    print("BA")
if (öğrencinotortalaması>=85 and öğrencinotortalaması<=89):
    print("BB")
elif (öğrencinotortalaması>=80 and öğrencinotortalaması<=84):
    print("CB")
elif (öğrencinotortalaması>=75 and öğrencinotortalaması<=79):
    print("CC")
elif (öğrencinotortalaması>=70 and öğrencinotortalaması<=74):
    print("DC")
elif (öğrencinotortalaması>=65 and öğrencinotortalaması<=69):
    print("DD")
elif (öğrencinotortalaması>=60 and öğrencinotortalaması<=64):
    print("E")
else:
    print("FF")
    
