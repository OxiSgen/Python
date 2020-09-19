def foo(x, y):
    x / y


errors = (ZeroDivisionError, ArithmeticError, AssertionError)
try:
    foo(1, 0)
except errors as e:
    print(e.__class__.mro()[e.__class__ not in errors].__name__)

'''
Если "брошенный" класс не находится среди трёх искомых то тогда выражение
в квадратных скобках будет равно еденице и из списка родителей возьмут первый элемент,
т.е. первого родителя,  иначе нулевой элемент - сам вызывающий класс.
'''
