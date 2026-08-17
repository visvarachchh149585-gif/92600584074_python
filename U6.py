my_tuple = (10, 20, 30, 20, 40)

print("Tuple:", my_tuple)
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])
print("Part of tuple:", my_tuple[1:4])
print("Count of 20 :", my_tuple.count(20))
print("Position of 30:", my_tuple.index(30))

a, b, c, d, e = my_tuple
print("Separated values:", a, b, c, d, e)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.add(6)
set1.remove(2)
print("New set1:", set1)

print("All items together:", set1.union(set2))
print("Common items:", set1.intersection(set2))
print("Items only in set1:", set1.difference(set2))
print("Items not in both:", set1.symmetric_difference(set2))


