#!/usr/bin/env python3.5


print('/nInitialize Empty')
map = {}
print(map)


print('/nInitialize Map')
map = {1:'a', 2: 'b'}
print(map)


print('/nPrint values of a map')
map = {1:'a', 2: 'b'}
for k, v in map.items():
    print('{}={}'.format(k,v))