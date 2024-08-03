def kare_al(x):
    print('Girilen Sayinin Karesi:' + x**2)  #TypeError
    
kare_al(3)
    

def kare_al(x):
    print('Girilen Sayinin Karesi:' + str(x**2))  
    
kare_al(3)

def kare_al(x):
    print('Girilen Sayi: ' + str(x) + ', Karesi: ' + str(x**2))
    
kare_al(3)