scope = {'global': {'parent': 'None', 'variables': set()}}


def create(ns, parent):
    scope.update({ns: {'parent': parent, 'variables': set()}})


def add(ns, var):
    scope[ns]['variables'].add(var)


'''def get(ns, var):
    if var in scope[ns]['variables']:
        print(ns)
    else:
        if scope[ns]['parent'] == 'None':
            print(scope[ns]['parent'])
        else:
            return get(scope[ns]['parent'], var)'''

#Версия короче
def get(ns, var):
    while not (ns == 'None' or var in scope[ns]['variables']):
        return get(scope[ns]['parent'], var)
    print(ns)


for cmd, namespace, arg in [input().split() for i in range(int(input()))]:
    # словарь глобальных переменных. Ключ - имя функции, в круглых скобках позиционные параметры
    globals()[cmd](namespace, arg) 
