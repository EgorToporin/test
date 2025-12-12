num_list = [1,-2,3,-8,6,7,-9,4,-4,-7]
zero_count = 0
one_count = 0
result_list = []
final_list = []
list_summa = 0

for i in range(len(num_list)):
    if num_list[i] > 0:
        zero_count += 1
        result_list.append(0)        
    else:
        one_count += 1
        result_list.append(1)
    list_summa += num_list[i]

for i in range(len(result_list)):
    if result_list[i] == 0:
        final_list.append(1)
    else:
        final_list.append(0)


print(result_list)
print(zero_count)
print(one_count)
print(final_list)
print(list_summa)