#!/usr/bin/env python3.5


# Check if list contains an element
lst = [1, 2, 3, 4]
print(3 in lst)


# Iterate 2 lists
lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8, 10]
for i, j in zip(lst1, lst2):
    print('{} {}'.format(i, j))

# 1. Sort a collection
sorted1 = sorted([1, 3, 10, 7, 9])
print(sorted1)


# 2. Sort a collection
sorted2 = [1, 3, 10, 7, 9]
sorted2.sort()
print(sorted2)
