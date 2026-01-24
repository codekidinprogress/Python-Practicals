a = ['b', 'c', 'd', 'e', 'f', 'g', 'h']
a = [x for (i,x) in enumerate(a)if i not in (0,2,4,5)]
print(a)

