import mysql.connector
class VT_olustur:
    def __init__(self):
        self.mydb = mysql.connector.connect(
          host="localhost",
         user="root",
         password="0215"
        )
        self.imlec = self.mydb.cursor()
        vt_adi = "Neset_Goktug_Gorukoglu"
        print("\n\n---KURULUM İŞLEMLERİ BAŞLATILDI---\n")
        self.imlec.execute(f"CREATE DATABASE IF NOT EXISTS {vt_adi};")
        self.imlec.execute(f"USE {vt_adi}")
        self.mydb.commit()
    def tablolariOlustur(self):
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS mezarlik
                            (
                               mezarlik_id INT PRIMARY KEY AUTO_INCREMENT,
                               mezarlik_adi VARCHAR(255) NOT NULL
                            )ENGINE=InnoDB;""")
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS mezar
                            (
                                mezar_id INT PRIMARY KEY AUTO_INCREMENT,
                                mezarlik_id INT,
                                mezar_yeri_numarasi INT,
                                FOREIGN KEY (mezarlik_id) REFERENCES mezarlik(mezarlik_id)
                            )ENGINE=InnoDB;""")
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS defin
                            (
                                defin_id INT PRIMARY KEY AUTO_INCREMENT,
                                mezar_id INT,
                                defin_edilen_kisi_adi VARCHAR(255) NOT NULL,
                                dogum_tarihi DATE,
                                olum_tarihi DATE,
                                FOREIGN KEY (mezar_id) REFERENCES mezar(mezar_id)
                            )ENGINE=InnoDB;""")
        self.mydb.commit()
        print("Tablolar oluşturuldu.")
    def verileriGir(self):
        mezarlik_data = [
            ('Saklıköy Mezarlığı',),
            ('Arap Mezarlığı',),
            ('Kimsesiz Mezarlığı',),
            ('Orta Mezarlığı',),
            ('Kapıcı Mezarlığı',),
            ('Bebek Mezarlığı',),
            ('Yaşlı Mezarlığı',),
            ('Susurluk Mezarlığı',),
            ('Ankara Mezarlığı',),
            ('Osmanlı Mezarlığı',)
        ]
        mezarlik_ekle = "INSERT INTO mezarlik (mezarlik_adi) VALUES (%s)"
        self.imlec.executemany(mezarlik_ekle, mezarlik_data)
        self.mydb.commit()
        mezar_data = [
            (1, 101),
            (1, 102),
            (2, 201),
            (2, 202),
            (3, 301),
            (3, 302),
            (4, 401),
            (4, 402),
            (5, 501),
            (5, 502)
        ]
        mezar_ekle = "INSERT INTO mezar (mezarlik_id, mezar_yeri_numarasi) VALUES (%s, %s)"
        self.imlec.executemany(mezar_ekle, mezar_data)
        self.mydb.commit()
        defin_data = [
            (1, 'Ahmet Kaya', '1970-01-01', '2000-05-15'),
            (2, 'Ayşe Yılan', '1985-03-12', '2015-11-20'),
            (3, 'Mehmet Demirtaş', '1962-07-22', '2022-02-28'),
            (4, 'Zeynep Ayka', '1978-12-05', '2010-08-10'),
            (5, 'Mustafa Parlak', '1990-04-18', '2021-06-25'),
            (6, 'Fatma Kasko', '1980-09-30', '2019-12-10'),
            (7, 'Ahmet Patates', '1975-06-15', '2005-09-08'),
            (8, 'Ayşe Kemir', '1995-02-28', '2023-03-19'),
            (9, 'Mehmet Bela', '1968-11-10', '2017-07-07'),
            (10, 'Zehra Nesin', '1987-08-20', '2012-04-03')
        ]
        defin_ekle = "INSERT INTO defin (mezar_id, defin_edilen_kisi_adi, dogum_tarihi, olum_tarihi) VALUES (%s, %s, %s, %s)"
        self.imlec.executemany(defin_ekle, defin_data)
        self.mydb.commit()
    def baglantiyiKapat(self):
        self.mydb.close()
        print("Bağlantı kapatıltı\n\n---KURULUM İŞLEMLERİ TAMAMLANDI---\n")
class MezarlikClass():
    def __init__(self):
        self.mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                password="0215",
                database="Neset_Goktug_Gorukoglu" 
        )
        self.imlec = self.mydb.cursor()
    def verileriGir(self, mezarlik_adi):
     try:
        sorgu = "INSERT INTO mezarlik (mezarlik_adi) VALUES (%s)" 
        deger = (mezarlik_adi,)
        self.imlec.execute(sorgu, deger)
        self.mydb.commit()
        print("Veri başarıyla Girildi.")
     except Exception as e:
        print(f"Hata oluştu: {e}")
    def VerileriGuncelle(self, yeni_mezarlik_adi, mezarlik_id):
     try:
        mezarlik_id = int(mezarlik_id)
        sorgu = "UPDATE mezarlik SET mezarlik_adi = %s WHERE mezarlik_id = %s"
        deger = (yeni_mezarlik_adi, mezarlik_id)
        self.imlec.execute(sorgu, deger)
        self.mydb.commit()
        print("Veri başarıyla güncellendi.")
     except Exception as e:
        print(f"Hata oluştu: {e}")
    def VerileriSorgula(self, mezarlik_id):
     try:
        mezarlik_id = int(mezarlik_id)
        sorgu = "SELECT * FROM Mezarlik WHERE mezarlik_id = %s"
        deger = (mezarlik_id,)
        self.imlec.execute(sorgu, deger)
        sonuc = self.imlec.fetchall()
        for row in sonuc:
            print(row)

            print("Veri başarıyla Sorgulandı.")
     except Exception as e:
        print(f"Hata oluştu: {e}")
    def VerileriSil(self, mezarlik_id):
     try:
        mezarlik_id = int(mezarlik_id)
        sorgu = "DELETE FROM defin WHERE mezar_id IN (SELECT mezar_id FROM mezar WHERE mezarlik_id = %s)"
        deger = (mezarlik_id,)
        self.imlec.execute(sorgu, deger)
        sorgu = "DELETE FROM mezar WHERE mezarlik_id = %s"
        self.imlec.execute(sorgu, deger)
        sorgu = "DELETE FROM mezarlik WHERE mezarlik_id = %s"
        self.imlec.execute(sorgu, deger)
        self.mydb.commit()
        print("Mezarlık ve bağlı mezarlar başarıyla silindi.")
     except Exception as e:
        print(f"Hata oluştu: {e}")
class MezarClass:
    def __init__(self):
        self.mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                password="0215",
                database="Neset_Goktug_Gorukoglu" 
        )
        self.imlec = self.mydb.cursor()
    def VerileriGir(self, mezarlik_id, mezar_yeri_numarasi):
        try:
            mezarlik_id = int(mezarlik_id)
            mezar_yeri_numarasi = int(mezar_yeri_numarasi)     
            sorgu = "INSERT INTO mezar (mezarlik_id, mezar_yeri_numarasi) VALUES (%s, %s)"
            veri = (mezarlik_id, mezar_yeri_numarasi)
            self.imlec.execute(sorgu, veri)
            self.mydb.commit()
            print("Veri başarıyla eklendi.")
        except Exception as e:
            print(f"Hata oluştu: {e}")
    def VerileriGuncelle(self, mezar_id, mezar_yeri_numarasi):
     try:
        mezar_id = int(mezar_id)
        sorgu = "UPDATE Mezar SET mezar_yeri_numarasi = %s WHERE mezar_id = %s"
        deger = (mezar_yeri_numarasi, mezar_id)
        self.imlec.execute(sorgu, deger)
        self.mydb.commit()
        print("Veri başarıyla Güncellendi.")
     except Exception as e:
            print(f"Hata oluştu: {e}")        
    def VerileriSorgula(self, mezar_id):
     try:
        mezar_id = int(mezar_id)
        sorgu = "SELECT * FROM Mezar WHERE mezar_id = %s"
        deger = (mezar_id,)
        self.imlec.execute(sorgu, deger)
        sonuc = self.imlec.fetchall()
        for row in sonuc:
            print(row)

        print("Veri başarıyla Sorgulandı.")
     except Exception as e:
            print(f"Hata oluştu: {e}")    
    def veri_silme(self, mezar_id):
     try:
        mezar_id = int(mezar_id)
        sorgu_mezarlik_id = "SELECT mezarlik_id FROM mezar WHERE mezar_id = %s"
        self.imlec.execute(sorgu_mezarlik_id, (mezar_id,))
        mezarlik_id = self.imlec.fetchone()[0]
        sorgu_defin = "DELETE FROM defin WHERE mezar_id = %s"
        self.imlec.execute(sorgu_defin, (mezar_id,))
        sorgu_mezar = "DELETE FROM mezar WHERE mezar_id = %s"
        self.imlec.execute(sorgu_mezar, (mezar_id,))
        sorgu_mezarlik = "DELETE FROM mezarlik WHERE mezarlik_id = %s"
        self.imlec.execute(sorgu_mezarlik, (mezarlik_id,))
        self.mydb.commit()
        print("Mezar ve bağlı mezarlıklar başarıyla silindi.")
     except Exception as e:
        print(f"Hata oluştu: {e}")
class DefinClass():
    def __init__(self):
        self.mydb = mysql.connector.connect(
                 host="localhost",
                 user="root",
                password="0215",
                database="Neset_Goktug_Gorukoglu" 
        )
        self.imlec = self.mydb.cursor()
    def VerileriGir(self, mezar_id, defin_edilen_kisi_adi, dogum_tarihi, olum_tarihi):
     try:
        mezar_id = int(mezar_id)
        sorgu = "INSERT INTO Defin (mezar_id, defin_edilen_kisi_adi, dogum_tarihi, olum_tarihi) VALUES (%s, %s, %s, %s)"
        deger = (mezar_id, defin_edilen_kisi_adi, dogum_tarihi, olum_tarihi)
        self.imlec.execute(sorgu, deger)
        self.mydb.commit()
        print("defin başarıyla eklendi.")
     except Exception as e:
        print(f"Hata oluştu: {e}")
    def VerileriGuncelle(self, defin_id, yeni_defin_edilen_kisi_adi):
      try:
        defin_id = int(defin_id)
        sorgu = "UPDATE Defin SET defin_edilen_kisi_adi = %s WHERE defin_id = %s"
        deger = (yeni_defin_edilen_kisi_adi, defin_id)
        self.imlec.execute(sorgu, deger)
        self.mydb.commit()
        print("defin başarıyla Güncellendi.")
      except Exception as e:
        print(f"Hata oluştu: {e}")
    def VerileriSorgula(self, defin_id):
     try:
        defin_id=int(defin_id)
        sorgu = "SELECT * FROM Defin WHERE defin_id = %s"
        deger = (defin_id,)
        self.imlec.execute(sorgu, deger)
        result = self.imlec.fetchall()
        for row in result:
            print(row)
            print("defin başarıyla Sorgulandı.")
     except Exception as e:
        print(f"Hata oluştu: {e}")
    def VerileriSil(self, defin_id):
     try:
        defin_id=int(defin_id)
        sorgu = "DELETE FROM Defin WHERE defin_id = %s"
        deger = (defin_id,)
        self.imlec.execute(sorgu, deger)
        self.mydb.commit()
        print("defin başarıyla Silindi.")
     except Exception as e:
        print(f"Hata oluştu: {e}")