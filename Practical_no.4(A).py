def find_common(L1, L2):
    for x in L1:
        for y in L2:
            if x == y:
                return True
        return False

print(find_common([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
print(find_common([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
