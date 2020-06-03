num = [24, 100, 144, 90, 125, 25, 145, 29, 1]


def find_median(l):
    for x in range(len(l) - 1, 0, -1):
        print('NEW OUTTER LOOP', x)
        for j in range(x):
            print("Inner loop", x, j)
            if l[j] < l[j + 1]:
                print("Swapped at", l[j], l[j + 1])
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


print('New List', find_median(num))
print('NEw list', sorted(num, reverse=True))
