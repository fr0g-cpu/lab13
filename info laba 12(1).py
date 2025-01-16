#1
#a)
numbers = [12, 24, 36, 48, 109, 187]
variant_number = 1
multiplier = variant_number + 7
def multiply(x):
    return x * multiplier
result = list(map(multiply, numbers))

print(result)

#b)
numbers = [12, 24, 36, 48, 109, 187]
variant_number = 1
multiplier = variant_number + 7
result = list(map(lambda x: x * multiplier, numbers))

print(result)

#2
my_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
other_number = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result = list(map(lambda x, y: x * y, my_number, other_number))

print(result)

#3
my_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
variant_number = 3
multiplied_numbers = list(map(lambda x: x * variant_number, my_number))
even_numbers = list(filter(lambda x: x % 2 == 0, multiplied_numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, multiplied_numbers))
print("Четные числа:", even_numbers)
print("Нечетные числа:", odd_numbers)

#4
phone_number_str = "1234567890"
variant_number = 4
int_divided_numbers = list(map(lambda x: int(x) // variant_number, phone_number_str))
float_divided_numbers = list(map(lambda x: int(x) / variant_number, phone_number_str))

print("Целочисленное деление:", int_divided_numbers)
print("Дробное деление:", float_divided_numbers)


