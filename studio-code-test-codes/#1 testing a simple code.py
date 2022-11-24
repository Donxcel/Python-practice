def sum_two_smallest_numbers(numbers):
    new_num = []
    numbers.sort()
    total = numbers[0] + numbers[1]
    print(type(total))
    return total
a = [19, 5, 42, 2, 77]
print(sum_two_smallest_numbers(a))