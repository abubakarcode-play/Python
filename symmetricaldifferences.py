set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result1 = set1 ^ set2
print("Symmetrical Difference using ^ operator:", result1)

result2 = set1.symmetric_difference(set2)
print("Symmetrical Difference using method:", result2)