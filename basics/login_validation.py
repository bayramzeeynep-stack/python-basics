kayitli_şifre="12345"
#örnek amaçlı
kayitli_mail= "student@example.edu"
#örnek amaçlı
girilen_mail= input("Mail gir.").strip()
girilen_şifre= input("Şifreni gir.")
mail_kontrol= girilen_mail.endswith("example.edu")

if not mail_kontrol:
    print("Öğrenci maili değildir.")

elif(kayitli_mail==girilen_mail and kayitli_şifre== girilen_şifre):
    print("Öğrenci mailidir.")
else:
    print("Hatalı giriş yaptınız.")
