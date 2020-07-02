import time
print("""


*****************************
Sınav Programına Hoş Geldiniz
*****************************

@author Yaman Durmaz


""")






while True:
        import time
        a = input("Vize Puanını Giriniz: ")
        if a < "35":
            print("Finale girmeye hak kazanamadınız!")
            break
        b = input("Final Puanını Giriniz: ")
        islem = (int(a) + int(b))/2

        if islem <= 35:
            print("hesaplanıyor")
            time.sleep(2)
            print("DD")
        elif islem <= 45:
            print("hesaplanıyor")
            time.sleep(2)
            print("DC")
        elif islem <= 55:
            print("hesaplanıyor")
            time.sleep(2)
            print("CC")
        elif islem <= 65:
            print("hesaplanıyor")
            time.sleep(2)
            print("CB")
        elif islem <= 75:
            print("hesaplanıyor")
            time.sleep(2)
            print("BB")
        elif islem <= 85:
            print("hesaplanıyor")
            time.sleep(2)
            print("BA")
        elif islem > 85:
            print("hesaplanıyor")
            time.sleep(2)
            print("AA")
