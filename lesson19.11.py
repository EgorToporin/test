# def sum_nums(a, b):
#     sum = a + b
#     return sum
#     print("Line is nit executed")


# first_sum = sum_nums(10,5)
# print(first_sum)


# print(sum_nums(50.5, 20))





# my_name = "Bogdan"  # присвоение значения 


# if my_name:
#     print(my_name)  # Условная инструкция



# import datetime  #Импортирование  модуля

# print(datetime.MINYEAR)



#snake_case  # Переменные, функции, методы, модули


#Pascalcase  # Классы


#my-package  # Пакеты


#DB_PASSWORD  # Константы



# my_number = 15
# print(my_number )


# string = "Hello , World"
# print(string)


# my_list = [1,2,3,4,5]
# print(my_list)


# name = "Egor"
# input(str("print your name "))



# my_number = 10
# print(id(my_number))

# other_number = my_number
# print(id(other_number))



# my_name = "Egor"

# print(id(my_name))

# my_num = 100

# print(id(my_num))

# other_num = my_num

# print(id(other_num))


 # 1
#for i in range(1,11):
#    if i % 2 == 0:
#         print(i)



# # 2
# summa = 0
# for i in range(1,21):
#     summa += i

# print(summa)




# # 3
# positive_number = 0
# negative_number = 0
# zero_number = 0

# my_list = [0, -2, 4, 3, -7, 10, -11]


# for num in my_list:
#     if num > 0:
#         positive_number += 1
#     elif num < 0:
#         negative_number += 1
#     else:
#         num = 0
#         zero_number += 1

# print(positive_number)
# print(negative_number)
# print(zero_number)




# name = "Egor"
# print(name.lower())




# positive_number = 0 

#my_list = [0, -2 ,4, 3, -7, 10, -11]

# for num in my_list:
#     if num > 0:
#         positive_number += 1

# print(positive_number)



my_list = [0, -2 ,4, 3, -7, 10, -11]

result_list = []

for num in my_list:
    if num <= 0:
        result_list.append(0)
    else:
        result_list.append(1)

count_zero = 0
count_one = 0

for num in result_list:
   if num == 0:
       count_zero += 1
   else:
       count_one += 1

print(result_list)
print(f"0 in masive { count_zero}")
print(f"1 in masive {count_one}")
 