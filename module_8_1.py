def add_everything_up(a, b):
    global TypeError
    try:
        if type(a) != type(b):
            raise TypeError
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


# def add_everything_up(a, b):
#     if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
#         return a + b
#     elif isinstance(a, str) and isinstance(b, str):
#         return a + b
#     else:
#         return str(a) + str(b)
