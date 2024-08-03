def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(3) #TypeError


def carpma_yap(x,y=1):
    print(x*y)
    
carpma_yap(3) 
carpma_yap(3,4)
carpma_yap(y=2, x=4)
