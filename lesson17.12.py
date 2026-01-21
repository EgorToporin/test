# def summa(num1, num2):
#     return num1 + num2

# print(summa(1, 10))


# def even_number(arr):
#     result_list = []
#     for i in arr:
#         if i % 2 == 0:
#             result_list.append(i)
#     return result_list   
# mass = [1,2,3,4,5,6,7,8,9,10]
# print(even_number(mass))

# user_age = int(input("write your age : "))

# if user_age < 18:
#     print("you are teenager")
# elif user_age < 61:
#     print("you are adult")
# else:
#     print("you are pensioner")

def user_age(age):
    if age < 18:
        return "you are teenager"
    elif age < 60:
        return "you are adult"
    else:
        return "you are pensioner"
    
print(user_age(60))