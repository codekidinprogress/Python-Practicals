def histogram(number):
    for i in number:
        if i < 0:
            print("Error: Negative number is not supported for this program!")
            continue
        print('*' * i)
print("Histogram for given value")
histogram([-4,9,7])
