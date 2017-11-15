# Lists
squares = [1, 4, 9, 16, 25]
print(squares)

# Like strings (and all other built-in sequence type), lists can be indexed and sliced:

print(squares[0])  # indexing returns the item

print(squares[-1])

print(squares[-3:])  # slicing returns a new list

# All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:

print(squares[:])

# Lists also support operations like concatenation:

print(squares + [36, 49, 64, 81, 100])