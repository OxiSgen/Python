scope = {'global': {'parent': 'None', 'variables': set()}}


def create(ns, parent):
    scope.update({ns: {'parent': parent, 'variables': set()}})


def add(ns, var):
    scope[ns]['variables'].add(var)


def get(ns, var):
    if var in scope[ns]['variables']:
        print(ns)
    else:
        if scope[ns]['parent'] == 'None':
            print(scope[ns]['parent'])
        else:
            return get(scope[ns]['parent'], var)


for _ in range(int(input())):
    cmd, namespace, arg = input().split()
    # словарь глобальных переменных. Ключ - имя функции, в круглых скобках позиционные параметры
    globals()[cmd](namespace, arg) 
