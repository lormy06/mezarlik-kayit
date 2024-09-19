import iö_Neset_Goktug_Gorukoglu_lib as proj
try:
    ilk_kurulum = proj.VT_olustur()
    ilk_kurulum.tablolariOlustur()
    ilk_kurulum.verileriGir()
    ilk_kurulum.baglantiyiKapat()
except:    
    print("\n\nKurulum Tamamlanamadı.\n\n")
mezarliknesne=proj.MezarlikClass()
mezarnesne=proj.MezarClass()
definnesne=proj.DefinClass()
def mezarlik_menu():
    while True:
        print("\n\n", "-" * 50)
        print("MEZARLIK MENÜ")
        print("1. Mezarlık Ekle")
        print("2. Mezarlık Güncelle")
        print("3. Mezarlık Sorgula")
        print("4. Mezarlık Sil")
        print("5. Çıkış")
        print("-" * 50)
        kullanici = input("Lütfen bir seçenek girin (1-5): ")
        if kullanici == "1":
            print("Mezarlık Ekle seçildi.")
            mezarliknesne.verileriGir(input('mezarlık adı giriniz.'))
        elif kullanici == "2":
            print("Mezarlık Güncelle seçildi.")
            yeni_mezarlik_adi=input('lütfen yeni mezarlık adını giriniz.')
            mezarlik_id=input('lütfen değişmek istediğiniz mezar isminin idyi girin')
            mezarliknesne.VerileriGuncelle(yeni_mezarlik_adi, mezarlik_id)
        elif kullanici == "3":
            print("Mezarlık Sorgula seçildi.")
            mezarlik_id=input('lütfen güncellemek istediğiniz mezar idyi girin')
            mezarliknesne.VerileriSorgula(mezarlik_id)
        elif kullanici == "4":
            print("Mezarlık Sil seçildi.")
            mezarlik_id=input('lütfen silmek istediğiniz mezar idyi girin')
            mezarliknesne.VerileriSil(mezarlik_id)
        elif kullanici == "5":
            print("Çıkış seçildi.")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1 ile 5 arasında bir sayı girin.")
def mezar_menu():
    while True:
        print("\n\n", "-" * 50)
        print("MEZAR MENÜ")
        print("1. Mezar Ekle")
        print("2. Mezar Güncelle")
        print("3. Mezar Sorgula")
        print("4. Mezar Sil")
        print("5. Çıkış")
        print("-" * 50)
        kullanici = input("Lütfen bir seçenek girin (1-5): ")
        if kullanici == "1":
            print("Mezar Ekle seçildi.")
            mezarlik_id = input('mezarlikid girin')
            mezar_yeri_numarasi = input('mezar yeri numarası girin')
            mezarnesne.VerileriGir(mezarlik_id, mezar_yeri_numarasi)
        elif kullanici == "2":
            print("Mezar Güncelle seçildi.")
            mezar_id=input('lütfen güncellemek istediğiniz mezar yeri numarasının mezar idsini giriniz')
            mezar_yeri_numarasi=input('lütfen yeni mezar yeri numarasını giriniz.')
            mezarnesne.VerileriGuncelle(mezar_id, mezar_yeri_numarasi)
        elif kullanici == "3":
            print("Mezar Sorgula seçildi."),
            mezar_id=input('sorgulamak istediğiniz mezar idyi girin')
            mezarnesne.VerileriSorgula(mezar_id)
        elif kullanici == "4":
            print("Mezar Sil seçildi.")
            mezar_id=input('silmek istediğiniz mezar id yi giriniz')
            mezarnesne.veri_silme(mezar_id)
        elif kullanici == "5":
            print("Çıkış seçildi.")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1 ile 5 arasında bir sayı girin.")
def defin_menu():
    while True:
        print("\n\n", "-" * 50)
        print("DEFİN MENÜ")
        print("1. Defin Ekle")
        print("2. Defin Güncelle")
        print("3. Defin Sorgula")
        print("4. Defin Sil")
        print("5. Çıkış")
        print("-" * 50)
        kullanici = input("Lütfen bir seçenek girin (1-5): ")
        if kullanici == "1":
            print("Defin Ekle seçildi.")
            mezar_id=input("mezar id girin")
            defin_edilen_kisi_adi=input("defin edilen kişinin adını giriniz")
            dogum_tarihi=("dogum tarihini giriniz")
            olum_tarihi=input("ölüm tarihini giriniz.")
            definnesne.VerileriGir(mezar_id, defin_edilen_kisi_adi, dogum_tarihi, olum_tarihi)
        elif kullanici == "2":
            print("Defin Güncelle seçildi.")
            yeni_defin_edilen_kisi_adi=input("güncellenecek isimi yazınız.")
            defin_id=input("defin idyi giriniz")
            definnesne.VerileriGuncelle(yeni_defin_edilen_kisi_adi, defin_id)
        elif kullanici == "3":
            print("Defin Sorgula seçildi.")
            defin_id=input("defin'idyi giriniz.")
            definnesne.VerileriSorgula(defin_id)
        elif kullanici == "4":
            print("Defin Sil seçildi.")
            defin_id=input("silmek istediğiniz defin id yi giriniz")
            definnesne.VerileriSil(defin_id)
        elif kullanici == "5":
            print("Çıkış seçildi.")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1 ile 5 arasında bir sayı girin.")
print("1. Mezarlık")
print("2. Mezar")
print("3. Defin")
hangitablo=input("hangi tabloda işlem yapmak istediğiniz sayıyı yazın")
if hangitablo=='1':
    mezarlik_menu()
elif hangitablo=='2':
    mezar_menu()
elif hangitablo=='3':
    defin_menu()
else:
    print('geçersiz sayı')