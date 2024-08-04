def old_sum(a,b):
    return a+b

old_sum(4,5)


new_sum = lambda a,b: a+b
new_sum(4,5)


sirasiz_liste = [('b',3), ('a',8), ('d',12), ('c',1)]

sorted(sirasiz_liste, key = lambda x: x[1])
