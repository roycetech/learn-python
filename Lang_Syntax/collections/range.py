#!/usr/bin/env python3.5

print('\nCheck if element in range')
print(1 in range(1, 4))


print('\nRange slicing')
r = range(0, 13, 2)
print(r[::3])  # => range(0, 10, 6)


print('\nReversing a range: ')
rng3 = range(4)
for x in reversed(rng3):
     print(x)
for x in (rng3[::-1]):
     print(x)


print('\nrange from 3 to 1')
rng = range(3, 0, -1)
for x in rng:
    print(x)


print('\nprint nth item from a range')
rng = range(0,10, 2)
print(rng[2])


print('\nprint nth item from a range')
rng = range(0,10, 2)
print(type(rng))
print(type(range(1)))


print 1

