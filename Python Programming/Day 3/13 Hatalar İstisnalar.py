a = 10
b = 0

a/b  #ZeroDivisionError

try:
    print(a/b)
except ZeroDivisionError:
    print('Paydada sifir olmaz')



a = 10
b = 2

try: 
    print(a/b)
except TypeError:
    print('Sayi ve string problemi')