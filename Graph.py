def rek_obh(parent, child):
    if parent in graph.keys() and child in graph.keys():
        if parent == child or parent in graph[child]:
            return 'Yes'
        for i in graph[child]:
            if rek_obh(parent, i) == 'Yes':
                return 'Yes'
        return 'No'
    else:
        return 'No'


graph = dict()
for string in [input().split(' : ') for i in range(int(input()))]:
    graph[string[0]] = ''.join(string[1:len(string)]).split()  # или просто написать string[2:] и выше .split(' ')
for string in [input().split(' ') for i in range(int(input()))]:
    print(rek_obh(string[0], string[1]))
