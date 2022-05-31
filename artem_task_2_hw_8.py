def max_value_of_two(first, second):
    the_max_two = max(first, second)
    return the_max_two


def max_value_of_three(first, second, third):
    one_of_the_max = max_value_of_two(first, second)
    return max_value_of_two(one_of_the_max, third)


print(max_value_of_two(1, 2))

print(max_value_of_three(8, 3, 9))
