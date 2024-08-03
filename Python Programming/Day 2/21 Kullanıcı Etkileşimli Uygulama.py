sinir = 5000
magaza_adi = input('Magaza Adi Nedir: ')
gelir = int(input('Geliriniz Nedir: '))

if gelir < sinir:
    print('Geliriniz sinirdan daha dusuk, geliriniz: ' + str(gelir))

elif gelir == sinir:
    print('Geliriniz sinirla esit')
    
else:
    print('Geliriniz sinirdan daha yuksek, tebrikler ' + magaza_adi)