# num_list = [1,2,3,4,5,6,7,8,9,10]
# sum_num_list = 0

# for i in range(len(num_list)):
#     sum_num_list += i

# print(sum_num_list)






num_list = [1,2,3,4,5,6,7,8,9,10]
even_list = []
odd_list = []
sum_even_list = 0
sum_odd_list = 0


for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        sum_even_list += num_list[i]
        even_list.append(num_list[i])
    else:
        sum_odd_list += num_list[i]
        odd_list.append(num_list[i])

if sum_even_list > sum_odd_list:
    print(f"парные числа больше {sum_even_list} от непарных на {sum_even_list - sum_odd_list} ")
else:
    print(f"непарные числа больльше {sum_odd_list} от парных на {sum_odd_list - sum_even_list}")

print(sum_even_list)
print(sum_odd_list)




