class Kisi:
    def __init__(self, ad, soyad, tc):
        self.ad = ad
        self.soyad = soyad
        self.__tc = tc

    def tam_ad(self):
        return f"{self.ad} {self.soyad}"


class Doktor(Kisi):
    def __init__(self, ad, soyad, tc, uzmanlik):
        super().__init__(ad, soyad, tc)
        self.uzmanlik = uzmanlik


class Hasta(Kisi):
    def __init__(self, ad, soyad, tc, sikayet):
        super().__init__(ad, soyad, tc)
        self.sikayet = sikayet