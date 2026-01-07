number1=int(input("ilk sayı gir:"))
number2=int(input("ikinci sayıyı gir:"))

islem=input("""yapmak istediğiniz işlemi giriniz:
(Toplam:+, Fark:-, çarpma:x, bölme:/)
""")

if islem=="+":
    print("Sonuç:",str(number1+number2))

elif islem=="-":
    print("Sonuç:",str(number1-number2))

elif islem=="x":
    print("Sonuç:",str(number1*number2))

elif islem=="/":
     print("Sonuç:",str(number1/number2))