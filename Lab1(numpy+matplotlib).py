import numpy as np
import matplotlib.pyplot as plt

try:
    inp = input("Введите три числа через пробел для первой строки: ")
    numbers = inp.split(" ")
    if len(numbers) != 3:
        print("Вы ввели не три числа!")
    else:
        inp2 = input("Введите три числа через пробел для второй строки: ")
        numbers2 = inp2.split(" ")
        if len(numbers2) != 3:
            print("Вы ввели не три числа!")
        else:
            M1 = np.array([[numbers[0], numbers[1]], [numbers2[0], numbers2[1]]], dtype=float)
            v1 = np.array([numbers[2], numbers2[2]], dtype=float)
            M2 = np.array([[numbers[0], numbers[1], numbers[2]], [numbers2[0], numbers2[1], numbers2[2]]], dtype=float)
            det = np.linalg.det(M1)
            rank1 = np.linalg.matrix_rank(M1)
            rank2 = np.linalg.matrix_rank(M2)
            if det == 0:
                if rank1 != rank2:
                    print("Система не имеет решений")
                    x = list(range(- 10, 10))
                    y1 = [(int(numbers[2]) - int(numbers[0]) * x1) / int(numbers[1]) for x1 in x]
                    y2 = [(int(numbers2[2]) - int(numbers2[0]) * x1) / int(numbers2[1]) for x1 in x]
                    plt.plot(x, y1)
                    plt.plot(x, y2)
                    plt.xlabel("x")  # подписываем ось х
                    plt.ylabel("y")  # подписываем ось у
                    plt.title("Система не имеет решений")  # подписываем график
                    plt.grid(True)
                    plt.show()
                else:
                    print("Система имеет бесконечное число решений")
                    x = list(range(- 10,10))
                    y1 = [(int(numbers[2]) - int(numbers[0]) * x1) / int(numbers[1]) for x1 in x]
                    plt.plot(x, y1)
                    plt.xlabel("x")  # подписываем ось х
                    plt.ylabel("y")  # подписываем ось у
                    plt.title("Система имеет бесконечное число решений")  # подписываем график
                    plt.grid(True)
                    plt.show()
            else:
                print("Решение: ")
                rezult = np.linalg.solve(M1, v1)
                print(rezult)
                x = list(range(int(rezult[0]) - 10, int(rezult[0]) + 10))
                y1 = [(int(numbers[2]) - int(numbers[0]) * x1) / int(numbers[1]) for x1 in x]
                y2 = [(int(numbers2[2]) - int(numbers2[0]) * x1) / int(numbers2[1]) for x1 in x]
                plt.plot(x, y1, label="y=(b11-a11*x)/a12")
                plt.plot(x, y2, label="y=(b21-a21*x)/a22")
                plt.scatter(float(rezult[0]), float(rezult[1]), c='purple')
                plt.xlabel("x")  # подписываем ось х
                plt.ylabel("y")  # подписываем ось у
                plt.title("Единственное решение")  # подписываем график
                plt.grid(True)
                plt.show()
except ValueError:
    print("Вы ввели не число!")
except ZeroDivisionError:
  print("Деление на ноль!")
