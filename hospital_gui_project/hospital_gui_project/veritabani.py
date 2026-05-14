import sqlite3


class HastaneDB:
    def __init__(self):
        self.baglanti = sqlite3.connect("hastane.db")
        self.cursor = self.baglanti.cursor()
        self.tablolari_kur()

    def tablolari_kur(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS doktorlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            uzmanlik TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS randevular (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hasta_ad TEXT,
            doktor_id INTEGER
        )
        ''')

        self.baglanti.commit()

    def doktor_ekle(self, doktor):
        self.cursor.execute(
            "INSERT INTO doktorlar(ad, uzmanlik) VALUES (?, ?)",
            (doktor.tam_ad(), doktor.uzmanlik)
        )
        self.baglanti.commit()

    def doktorlari_getir(self):
        return self.cursor.execute(
            "SELECT * FROM doktorlar"
        ).fetchall()

    def randevu_al(self, hasta_ad, doktor_id):
        self.cursor.execute(
            "INSERT INTO randevular(hasta_ad, doktor_id) VALUES (?, ?)",
            (hasta_ad, doktor_id)
        )
        self.baglanti.commit()

    def randevulari_getir(self):
        query = '''
        SELECT randevular.id,
               randevular.hasta_ad,
               doktorlar.ad
        FROM randevular
        JOIN doktorlar
        ON randevular.doktor_id = doktorlar.id
        '''

        return self.cursor.execute(query).fetchall()