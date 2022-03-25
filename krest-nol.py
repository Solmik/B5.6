# -*- coding: utf-8 -*-
pol = ["-" for i1 in range(3)], ["-" for j1 in range(3)], ["-" for k in range(3)]   # Начальное заполнение поля
z = ["крестик", "нолик"]    # Для вывода в сообщения
z1 = ["o", "x"]     # Символы, для заполнения поля
kor_ist = ['0', '1', '2']  # символы, допустимые для ввода
# pob - выигрышные комбинации
pob = [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]], [[1, 0], [1, 1], [1, 2]],
       [[0, 2], [1, 2], [2, 2]], [[0, 2], [1, 1], [2, 0]], [[2, 0], [2, 1], [2, 2]], [[0, 1], [1, 1], [2, 1]]]


# Вывод поля в консоль
def pnt_pole():
    print(" ", 0, 1, 2)
    for i in range(3):
        print(i, pol[i][0], pol[i][1], pol[i][2])


kor1 = []  # Список координат из input для проверки корректности ввода
kor = []  # Строка из ввода
k1 = []   # список координат для проверки выигрышной ситуации
k2 = []   # выигрышные координаты
k3 = []   # накопление координат для проверки выигрышной комбинации
kor_x = []  # координаты крестиков на поле
kor_o = []  # координаты ноликов на поле
lk = 0  # Количество вводимых символов
u = 0   # флажок окончания игры
h = 0  # индекс для вывода в сообщении крестик/нолик
h1 = "x"   # символ заменяющий символы в выигрышной строчке
con1 = 0  # счетчик символов в строчке, соответствующих символам выигрышной комбинации

print("Игра крестики-нолики")
print("Введите положение крестика или нолика  сначала номер строки,\n затем через пробел номер столбца")
pnt_pole()

while u < 1:
    kor1 = []
    el_cor = 0  # Контроль числа корректно введённых символов
    x, y = 0, 0  # Введенные координаты(введённые символы после проверки)
    while el_cor != 2:
        dtCor = 0
        kor = input("Введите  " + z[h] + "->").split()
        lk = len(kor)
        if lk != 2:  # Проверка количества введенных чисел
            print("Неправильный ввод, введено", lk, "символов")
        else:   # Проверка корректности введённых символов
            el_cor = 0
            for i in range(2):
                if kor[i] not in kor_ist:
                    print("Введён неправильный символ ")
                    break
                else:
                    el_cor += 1

    kor1 = list(map(int, kor))

    x = kor1[0]
    y = kor1[1]
    # Проверка свободной клетки с координатами x, y
    if pol[x][y] != '-':
        print("Клетка занята!", h)
    else:
        # Заполнение поля "х" и "о"
        if h == 0:
            pol[x][y] = "x"
            h = 1
            kor_x.append([x, y])
            k1 = kor_x
            h1 = "\U0000274C"

        else:
            pol[x][y] = "o"
            h = 0
            kor_o.append([x, y])
            k1 = kor_o
            h1 = chr(6105)
    # Проверка на ничью
    con1 = 0
    for i in range(3):
        for j in range(3):
            if pol[i][j] == '-':
                con1 += 1
    if con1 == 0:
        print("Ничья!!!")
        pnt_pole()
        u = 2
        break

    # Проверка выигрышной комбинации
    #
    for i in range(8):
        n = 0
        k3 = []
        for j in range(3):
            if pob[i][j] in k1:

                n += 1
                k3.append(pob[i][j])
                if n == 3:
                    u = 2
                    for i1 in range(3):
                        x1 = k3[i1][0]
                        y1 = k3[i1][1]
                        pol[x1][y1] = h1    # Замена символов в выигрышной строчке
                    if h == 0:
                        print("Победили нолики!!!")
                        break
                    else:
                        print("Победили крестики!!!")
                        break
    pnt_pole()

