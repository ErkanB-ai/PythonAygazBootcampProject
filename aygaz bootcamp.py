import random
def tas_kagit_makes_ERKAN_BÜYÜKKARACIĞAN():
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
    print("Kurallar: Taş makası kırar, Makas kağıdı keser, Kağıt taşı sarar.")
    print("Oyundan ayrılmak istiyorsanız 'a' tuşuna basınız.")

    while True:
        oyuncu_galibiyet = 0
        bilgisayar_galibiyet = 0
        tur_sayisi = 0

        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            print(f"\n{tur_sayisi + 1}. Tur:")
            secenekler = ["taş", "kağıt", "makas"]
            oyuncu_secimi = input("Seçiminiz yapınız: taş, kağıt, makas: ").lower()

            if oyuncu_secimi == "a":
                print("Oyun isteğiniz üzerine sonlandırılmıştır.")
                return
            if oyuncu_secimi not in secenekler:
                print("Geçersiz işlem yaptınız tekrar deneyiniz.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Oyun berabere")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş"):
                print("Bu turu kazandınız")
                oyuncu_galibiyet += 1
            else:
                print("Bu turu bilgisayar kazandı")
                bilgisayar_galibiyet += 1

            tur_sayisi += 1

        if oyuncu_galibiyet == 2:
            print("\nTebrikler oyunu kazandınız")
        else:
            print("\nBilgisayar oyunu kazandı")

        devam = input("Yeni bir oyun oynamak ister misiniz? Cevabınızı evet/hayır olarak giriniz: ").lower()
        if devam != "evet":
            print("Oyun sona erdi!")
            break
tas_kagit_makes_ERKAN_BÜYÜKKARACIĞAN()



