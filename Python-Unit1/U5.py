numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_element = numbers[0]
last_element = numbers[-1]
print("First:", first_element, "Last:", last_element)

numbers[2] = 35
print("updated list:", numbers)

first_three = numbers[:3]
middle_part = numbers[3:7]
reversed_list = numbers[::-1]

print("First three:", first_three)
print("Middle :", middle_part)
print("Reversed:", reversed_list)

squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
print("Squares of evens:", squares_of_evens)

