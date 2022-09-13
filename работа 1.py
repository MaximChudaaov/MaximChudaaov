start = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]
users = []
while True:

    if len(a) % 9 > 0:
        numbers_of_lines = int(len(a) / 9 + 1)
    else:
        numbers_of_lines = int(len(a) / 9)
    b = []
    for i in range(1, numbers_of_lines + 1):
        b.append(a[10 * (i - 1) - (i - 1):10 * i - 1 - (i - 1)])
    for i in b:
        print(i)
    print("введите колличество исправлений")
    quantity = int(input())
    if quantity == 0:
        new_user = input("Введите ваше имя ")
        users.append([new_user, len(a)])
        for _ in users:
            print(*_)
        print()
        a = start
        continue
    q = []
    for i in range(quantity):
        q.append([int(input()), int(input())])
    a = []
    for i in range(len(b)):
        for ii in range(len(b[i])):
            if not [i + 1, ii + 1] in q:
                a.append(b[i][ii])



