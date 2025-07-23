# Challenge number 1: Even vs. Odd
def even_or_odd(number):
    result = number%2
    if result == 0:
        return 'Even'
    else:
        return "Odd"
    
# Challenge number 2: Convert a number into a string
def number_to_string(num):
    return str(num)

# Challenge number 3: Remove all spaces
def no_space(x):
    text = x
    return text.replace(" ", "")

