class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        

ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

ali.dil_ekle('R')
ali.bildigi_diller

veli.dil_ekle('Python')
veli.bildigi_diller
