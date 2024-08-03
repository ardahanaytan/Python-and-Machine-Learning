def direkt_hesap(isi, nem, sarj):
    print((isi+nem)/sarj)
    
cikti = direkt_hesap(25, 40, 70)
print(cikti)  #None



def direkt_hesap(isi, nem, sarj):
    return (isi+nem)/sarj

cikti = direkt_hesap(25, 40, 70)
print(cikti)  #0.9285714285714286
