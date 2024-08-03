set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

set1.isdisjoint(set2)  #False   Kesişimleri boş küme değil

set1.issubset(set2)  #True    set1, set2'nin alt kümesi

set2.issuperset(set1)  #True   set2, set1'i kapsıyor
