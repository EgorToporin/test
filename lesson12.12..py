# matrix =  [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# summa = 0

# for row in matrix:
#     for item in row:
#         if item % 2 == 0:
#             summa += item

# print(summa)





# def input_matrix():
#     # Вводим размеры матрицы
#     rows = int(input("Введите количество строк: "))
#     cols = int(input("Введите количество столбцов: "))
    
#     matrix = []
    
#     # Вводим элементы матрицы
#     print("Введите элементы матрицы:")
#     for i in range(rows):
#         row = list(map(int, input(f"Строка {i + 1}: ").split()))
#         while len(row) != cols:
#             print(f"Количество элементов в строке должно быть равно {cols}. Попробуйте снова.")
#             row = list(map(int, input(f"Строка {i + 1}: ").split()))
#         matrix.append(row)
    
#     return matrix

# # Пример использования
# matrix = input_matrix()

# # Выводим введенную матрицу
# print("Введенная матрица:")
# for row in matrix:
#     print(row)



matrix = [
    [4,5,6],
    [7,8,9],
    [10,18,22]
]
user_number = int(input("write your number: "))

for row in matrix:
    for item in range(len(row)):
        row[item] *= user_number
print(matrix)




# matrix = [
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 18, 22]
# ]

# user_number = int(input("write your number: "))

# # Перебираем строки и элементы строк
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         matrix[i][j] *= user_number  # Умножаем элемент на число и сохраняем в матрице

# # Выводим измененную матрицу
# for row in matrix:
#     print(row)
