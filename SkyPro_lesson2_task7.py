lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

for x in range(0, 13):
    if (lst[x] < 30) and (lst[x] % 3 == 0):
        print(lst[x])
