import operator
d = {1: 22, 3: 30, 4:8, 2:11, 0:27}
print(d)
t = sorted(d.items(), key = operator.itemgetter(0))
print("In Ascending order by value: ", t)
t = sorted(d.items(), key= operator.itemgetter(0), reverse = True)
print("In Descending order by value: ", t)
