import time


def one(a, b, c):
    return a + b + c


def two(*args):
    return args[0] + args[1] + args[2]


def three(**args):
    return args['a'] + args['b'] + args['c']


count = 9000000
_startTime = time.time()
for num in range(count):
    one(1, 2, 3)
print("Positional test:", time.time() - _startTime)

_startTime = time.time()
for num in range(count):
    two(1, 2, 3)
print("args as list test:", time.time() - _startTime)

_startTime = time.time()
for num in range(count):
    three(a=1, b=2, c=3)
print("args as dict test:", time.time() - _startTime)


''' Positional test: 1.518535852432251
    args as list test: 2.4950003623962402
    args as dict test: 3.4079999923706055 '''
