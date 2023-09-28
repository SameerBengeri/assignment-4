def triple_number(x):
    return x*3
numbers = [1, 2, 3 ,4, 5, 6, 7]
tripled_numbers = list(map(triple_number, numbers))
print('Original Numbers', numbers)
print('Tripled Numbers',tripled_numbers)