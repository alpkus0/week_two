ogrenciler = []

def ogrenci_ekle():
    print("\n***Yeni Öğrenci Ekle***\n")
    ad = input("Öğrencinin Adını Giriniz = ")
    soyad = input("Öğrencinin Soyadını Giriniz = ")
    no = int(input("Öğrencinin Numarası Giriniz = "))
    bolum = input("Öğrencinin Bölümünü Giriniz = ")
    not_ortalama = float(input("Öğrencinin Not Ortalamasını Giriniz = "))

    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Numarası": no,
        "Bölümü": bolum,
        "Not Ortalaması": not_ortalama,
    }
    ogrenciler.append(ogrenci)
    print(f"\n{ad} {soyad} adlı öğrenci başarıyla eklendi.\n")
def tum_ogrencileri_listele():
    print("\n***Tüm Öğrencileri Listele***\n")
    if not ogrenciler:
        print("Öğrenci bulunmadı. Lütfen öğrenci kaydı yapınız.\n")
    else:
        print("---Tüm Öğrenciler---\n")
        for i, ogrenci in enumerate(ogrenciler, start=1):
            print(f"{i} - {ogrenci['Ad']} {ogrenci['Soyad']} {ogrenci['Numarası']} ")
def ogrenci_bilgilerini_goruntule():
    print("\n***Öğrenci Bilgilerini Görüntüle***\n")
    num = int(input("Lütfen Öğrencinin Numarasını giriniz = "))

    for ogrenci in ogrenciler:
        if num == ogrenci['Numarası']:
            print("\n-----ÖĞRENCİ BİLGİLERİ-----\n")
            print(f"Adı: {ogrenci['Ad']}")
            print(f"Soyadı: {ogrenci['Soyad']}")
            print(f"Numarası: {ogrenci['Numarası']}")
            print(f"Bölüm: {ogrenci['Bölümü']}")
            print(f"Not Ortalaması: {ogrenci['Not Ortalaması']}\n")
            return
    print("Bu numaraya sahip öğrenci bulunmadı tekrar deneyiniz.\n")
    ogrenci_bilgilerini_goruntule()
def ogrenci_bilgilerini_guncelle():
    print("\n***Öğrenci Bilgilerini Güncelle***\n")
    guncelleme = int(input("Güncellenecek öğrencinin numarasını giriniz = "))

    for ogrenci in ogrenciler:
        if guncelleme == ogrenci['Numarası']:
            while True:
                print(f"\n{ogrenci['Ad']} {ogrenci['Soyad']} adlı öğrenci seçildi.\n")
                print("Güncellenebilir Bilgiler:")
                print("1 - Adı")
                print("2 - Soyadı")
                print("3 - Numarası")
                print("4 - Bölümü")
                print("5 - Not Ortalaması\n")
                print("6 - Ana Menüye Dön\n")

                secim = input("Lütfen güncellemek istediğiniz bilgiyi seçiniz (1-6): ")

                if secim == "1":
                    yeni_ad = input(f"Öğrencinin eski adı {ogrenci['Ad']}, lütfen yeni adını giriniz = ")
                    ogrenci['Ad'] = yeni_ad
                    print(f"\nÖğrencinin adı {yeni_ad} olarak güncellenmiştir.\n")
                elif secim == "2":
                    yeni_soyad = input(f"Öğrencinin eski soyadı {ogrenci['Soyad']}, lütfen yeni soyadını giriniz = ")
                    ogrenci['Soyad'] = yeni_soyad
                    print(f"\nÖğrencinin soyadı {yeni_soyad} olarak güncellenmiştir.\n")
                elif secim == "3":
                    numara = int(input(f"Öğrencini eski numarası {ogrenci['Numarası']}, lütfen yeni numarasını giriniz = "))
                    ogrenci['Numarası'] = numara
                    print(f"\nÖğrencinin numarası {numara} olarak güncellenmiştir.\n")
                elif secim == "4":
                    bolum = input(f"Öğrencinin eski bölümü {ogrenci['Bölümü']}, lütfen yeni bölümünü giriniz = ")
                    ogrenci['Bölümü'] = bolum
                    print(f"\nÖğrencini bölümü {bolum} olarak güncellenmiştir.\n")
                elif secim == "5":
                    ort = float(input(f"Öğrencinin eski not ortalaması {ogrenci['Not Ortalaması']}, "
                                      f"lütfen yeni not ortalamasını giriniz."))
                    ogrenci['Not Ortalaması'] = ort
                    print(f"\nÖğrencinin not ortalaması {ort} olarak güncellenmiştir.\n")
                elif secim == "6":
                    print("Ana menüye dönülüyor...")
                    return
                else:
                    print("\n Hatalı seçim yaptınız. Lütfen 1 ila 6 arasında bir seçim yapınız.\n")
            return
    print("Bu numaraya sahip öğrenci bulunamadı.\n")
    ogrenci_bilgilerini_guncelle()
def ogrenci_sistemden_silme():
    print("\n***Öğrenciyi Sil***\n")
    silme = int(input("Silmek istediğiniz öğrencinin numarasını giriniz = "))
    for ogrenci in ogrenciler:
        if ogrenci['Numarası'] == silme:
            ogrenciler.remove(ogrenci)
            print(f"\n{ogrenci['Ad']} {ogrenci['Soyad']} adlı öğrenci sistemden başarıyla silindi.")
            return
    print("Yanlış öğrenci numarası girdiniz tekrar deneyiniz.")
    ogrenci_sistemden_silme()
def menu():
    while True:
        print("\n***** Öğrenci Yöneti Sistemi *****\n")
        print("1 - Tüm Öğrencileri Listele")
        print("2 - Yeni Öğrenci Ekle")
        print("3 - Öğrenci Bilgilerini Görüntüle")
        print("4 - Öğrenci Bilgilerini Güncelle")
        print("5 - Öğrenciyi Sil")
        print("6 - Çıkış\n")

        secim = input("1 ila 6 arasında bir seçim yapınız: ")

        if secim == "1":
            tum_ogrencileri_listele()
        elif secim == "2":
            ogrenci_ekle()
        elif secim == "3":
            ogrenci_bilgilerini_goruntule()
        elif secim == "4":
            ogrenci_bilgilerini_guncelle()
        elif secim == "5":
            ogrenci_sistemden_silme()
        elif secim == "6":
            print("\nUygulamadan çıkılıyor...\n")
            break
        else:
            print("\nYanlış seçim. Lütfen 1 ila 6 arasında bir seçim yapınız.\n")


menu()