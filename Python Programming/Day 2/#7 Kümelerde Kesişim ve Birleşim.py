# intersection() : kesişim
# union() : birleşim

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)

kesisim = set1 & set2

set1.union(set2)

birlesim = set2.union(set1)

set1.intersection_update(set2)

