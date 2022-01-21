def find_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if type(number/2) == int:
            even_numbers.append(number)
    
    return even_numbers
