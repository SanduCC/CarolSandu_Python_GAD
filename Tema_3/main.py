from recursive_module import *

def sum_fun(*args, **kwargs):
    sum = 0
    for arg in args:
        if (isinstance(arg, float) or isinstance(arg, int)):
            sum += arg
    return sum


print(sum_fun(1, 5, -3, "abc", [12, 56, "cad"]))
print(sum_fun())
print(sum_fun(2, 4, "abc", param_1=2))


def is_integer():
    elem = input("Introduceti elementul: ")
    try:
        isinstance(elem, int)
        print(elem)
    except:
        print(0)

is_integer()

print(full_sum(10))
print(even_element_sum(4))
print(uneven_element_sum(5))