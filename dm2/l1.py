from pprint import pprint
import lib.utils as utils

arr = [[0, 3, None, None, 4, 4, 4, 4, None, 3, 4, None],
       [3, 0, 1, None, None, None, None, 4, None, 2, None, None],
       [None, 1, 0, 5, None, None, None, None, 3, 1, None, None],
       [None, None, 5, 0, 1, 4, 1, None, 4, 5, 4, None],
       [4, None, None, 1, 0, 1, None, None, None, 3, None, None],
       [4, None, None, 4, 1, 0, 2, None, None, None, 4, None],
       [4, None, None, 1, None, 2, 0, None, None, 4, None, 1],
       [4, 4, None, None, None, None, None, 0, 3, 3, None, 5],
       [None, None, 3, 4, None, None, None, 3, 0, None, 5, None],
       [3, 2, 1, 5, 3, None, 4, 3, None, 0, 2, None],
       [4, None, None, 4, None, 4, None, None, 8, 2, 0, 4],
       [None, None, None, None, None, None, 1, 5, None, None, 4, 0]]

g = utils.normalize(arr)
utils.latex(arr)


print('Исходная таблица соединений R:')
print(utils.latex(arr))


def sus(g):
    step = 0
    colors = [0 for i in range(len(g))]
    ignore = []

    def susm(line):
        s = 0
        for x, val in enumerate(line):
            if x not in ignore:
                s += val
        return s
    while 0 in colors:
        step += 1
        print(f'{step}. Положим j = {step}')
        s = [(i, susm(line), line) for i, line in enumerate(g)]
        
        for i, sumed, line in s:
          if (i not in ignore):
              print(i, sumed)
                
        s = sorted(s, key=lambda x: x[1], reverse=True)

        def can(idx, step):
            for i, e in enumerate(g):
                if i == idx:
                    continue
                if e[idx] == 1:
                    if colors[i] == step:
                        return False

            return True

        for i, sumed, line in s:
            if (i not in ignore):
                print(i + 1, end=',')
                
        print('')
        for i, sumed, line in s:
            if (i not in ignore) and can(i, step):
                colors[i] = step
                print(i + 1, end=',')

        print('')
        ignore = []
        for i, color in enumerate(colors):
            if color != 0:
                ignore.append(i)
        # step += 1
        # print(f'{step}. Упорядочим вершины графа в порядке не возрастания ri')
        # print(', '.join([x[0] for x in s]))
        # pprint(s)


print(sus(g))
