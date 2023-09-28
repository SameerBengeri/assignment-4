def square_number(x):
    return x**2
numbers = [4, 5, 2, 9]
squared_numbers = list(map(square_number, numbers))
print('Original Numbers', numbers)
print('Squared Numbers', squared_numbers)