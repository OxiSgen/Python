'''
def is_child_prev(exception, parent):
    return exception == parent or any(map(lambda pl: is_child_prev(pl, parent), graph[exception]))


graph = dict()
stack = set()
for string in [input().split(' : ') for i in range(int(input()))]:
    graph[string[0]] = ''.join(string[1:len(string)]).split()
for exception_type in [input() for i in range(int(input()))]:
    for it in stack:
        if is_child_prev(exception_type, it):
            print(exception_type)
    stack.add(exception_type)
'''


def checkdup(d):
    return cls[d] is None or any(map(checkdup, cls[d]))


cls = {d[0]: set(d[2:]) for _ in range(int(input())) for d in [input().split()]}

for _ in range(int(input())):
    c = input()
    if checkdup(c):
        print(c)
    cls[c] = None
