maaslar = [1000,2000,3000,4000,5000]

def zam_az(x):
    print('Eski Maas: ' + str(x) + ' -> Yeni Maas: ' + str(int(x * 1.20)))

def zam_cok(x):
    print('Eski Maas: ' + str(x) + ' -> Yeni Maas: ' + str(int(x * 1.10)))
    

for i in maaslar:
    if i < 3000:
        zam_az(i)
    
    else:
        zam_cok(i)