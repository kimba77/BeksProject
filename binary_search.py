def binarySearch(idea, start, stop, search):
    while True:
        middle = stop + (start - stop) // 2
        if idea[middle] == search:
            return middle
        elif idea[middle] > search:
            return binarySearch(idea, start, middle-1, search)
        else:
            return binarySearch(idea, middle+1, stop, search)


idea = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200, 300, 400]
search = 40
result = binarySearch(idea, 0, len(idea) - 1, search)

if result != -1:
    print("Элемент найден в индексе % d" % result)
else:
    print("Элемент не находится в списке")
