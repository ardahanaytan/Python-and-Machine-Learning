class VeriBilimci():
    bildigi_diller = ['R', 'Python']
    bolum = ''
    sql = ''
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = []

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append('Python')
ali.bildigi_diller

veli.bildigi_diller
veli.bildigi_diller.append('R')
veli.bildigi_diller

osman = VeriBilimci()
osman.bildigi_diller
osman.bildigi_diller.append('Java')
osman.bildigi_diller
VeriBilimci.bildigi_diller

ali.bolum = 'istatistik'
VeriBilimci.bolum
veli.bolum
veli.bolum = 'end_muh'
veli.bolum
ali.bolum
VeriBilimci.bolum
