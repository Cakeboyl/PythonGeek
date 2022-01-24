def sum_list_1(dataset: list) -> int:
    res = 0
    while dataset != 0:
        res += dataset % 10
        dataset //= 10
    return res # Верните значение полученной суммы

def sum_list_2  (dataset: list) -> int:
    for i in range(len(dataset)):
        dataset[i] += 17
    return sum_list_2(dataset)

my_list = list(range(1, 1001, 2))
for i in range(len(my_list)):
    my_list[1] = my_list[1] ** 3

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
# Не могу понять почему ничего не выводит.