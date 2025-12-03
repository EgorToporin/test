# 1

# Напишите программу, которая запрашивает у пользователя два числа и выводит все числа, которые кратны 3 в заданном диапазоне (включая границы).

# user_number1 = int(input("введите первое число : "))
# user_number2 = int(input("введите второе число : "))

# for num in range(user_number1, user_number2):
#     if num % 3 == 0:
#         print(num)





# 2

# Напишите программу, которая запрашивает у пользователя два числа и выводит все нечётные числа в заданном диапазоне (включая границы).

# user_number1 = int(input("write yout first number : "))
# user_number2 = int(input("write your second number : "))

# for num in range(user_number1, user_number2):
#     if num % 2 != 0:
#         print(num)






# 3 

# Напишите программу, которая запрашивает два числа и выводит все числа, которые делятся на оба числа (включая границы).?

# user_number1 = int(input("write your number: "))
# user_number2 = int(input("write your number: "))

# for num in range(user_number1, user_number2 + 1):
#     if num % user_number1 == 0 and num % user_number2 == 0:
#         print(num)



# 4

# Напишите программу, которая запрашивает два числа и выводит все числа, кратные 5, но не кратные 3, в заданном диапазоне.

# user_number1 = int(input("write your first number : "))
# user_number2 = int(input("write your second number : "))

# for num in range(user_number1, user_number2 + 1 ):
#     if num % 5 == 0 and num % 3 != 0:
#         print(num)




# 5

# Напишите программу, которая запрашивает два числа и выводит их сумму всех чётных чисел в этом диапазоне.

# user_number1 = int(input("write your number: "))
# user_number2 = int(input("write your number: "))
# even_summa = 0 

# for num in range(user_number1, user_number2 + 1):
#     if num % 2 == 0:
#         even_summa += num

# print(even_summa)




# 6

# такое же как 5, но и с нечетными 

# user_number1 = int(input("write your number: "))
# user_number2 = int(input("write your number: "))
# even_summa = 0
# odd_summa = 0

# for num in range(user_number1, user_number2 + 1):
#     if num % 2 == 0:
#         even_summa += num
#     else:
#         num % 2 != 0
#         odd_summa += num 

# print(even_summa)
# print(odd_summa)




# 7

# user_number = int(input("write your number: "))
# count = 0 

# for num in range(user_number):
#     if num % 7 == 0:
#         count += 1

# print(count)
























#8
# #Напиши программу, которая находит сумму всех чисел, делящихся на 3 и на 5, в заданном диапазоне
# user_number1 = int(input("write your number: "))
# user_number2 = int(input("write your number: "))
# summa = 0

# for num in range(user_number1 , user_number2 + 1):
#     if num % 3 == 0 and num % 5 == 0:
#         summa += num 

# print(summa)












# 9
# Напиши программу, которая находит сумму всех четных чисел и сумму всех нечетных чисел в заданном диапазоне от a до b, но в конце выводит сумму четных чисел, делённую на 2.

# user_number1 = int(input("write your number: "))
# user_number2 = int(input("write your number: "))
# even_summa = 0
# odd_summa = 0


# for num in range(user_number1, user_number2):
#     if num % 2 == 0:
#         even_summa += num
#     else:
#         odd_summa += num 

# print(even_summa / 2)
# print(odd_summa)




#10
# # Напиши программу, которая находит количество чисел, кратных 7, в диапазоне от a до b.
# user_number1 = int(input("write your number: "))
# user_number2 = int(input("write your number: "))
# numbers = 0 

# for num in range(user_number1 , user_number2):
#     if num % 7 == 0:
#         numbers += 1

# print(numbers)







# Напиши программу, которая находит сумму чисел, которые не делятся на 3, в диапазоне от a до b.


# user_number1 = int(input("write your number: "))
# user_number2 = int(input("write your number: "))
# not3_summa = 0

# for num in range(user_number1, user_number2 + 1):
#     if num % 3 != 0:
#         not3_summa += num 

# print(not3_summa)




