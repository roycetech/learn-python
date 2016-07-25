print("You got {} points".format(99))


# Print the number 1 with guaranteed 4 spaces.
print("Padding {:4d}".format(1))


# Print abc with guaranteed 5 spaces.
print('[{:5s}]'.format('abc'))


# Print abc with guaranteed 5 spaces, right aligned.
print('[{:>5s}]'.format('abc'))


print('Number: {:d}'.format(1))
print('Number: {:.2f}'.format(1))
print('Number: {}'.format(1))


print('\nIndexed interpolation')
print('{0} {1}'.format('Hello', 'World'))


#substring
input = 'abcdef'
print(input[1:len(input) -1])


# ends_with
input = 'abcdef'
print(input[-3:])

