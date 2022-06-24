# def decorator_list(fnc):
#     def inner(list_of_tuples):
#         return [fnc(val[0], val[1]) for val in list_of_tuples]
#     return inner


# @decorator_list
# def add_together(a, b):
#     return a + b


# print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

def meta_decorator(arg):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [(fnc(val[0], val[1])) ** power for val in list_of_tuples]
        return inner
    if callable(arg):
        power = 2
        return decorator_list(arg)
    else:
        power = arg
        return decorator_list


@meta_decorator
def add_together(a, b):
    return a + b
print(add_together([(1,2),(12,12),(25,45),(23,32)]))
