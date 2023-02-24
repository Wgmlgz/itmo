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

def purge(s, idx: int):
  del s[idx]
  for line in s:
    del line[2][idx]

def sus(g):
    step = 1
    print(f'{step}. Положим j = {step}')

    s = [(f'e{i + 1}', sum(line), line) for i, line in enumerate(g)]
    s = sorted(s, key=lambda x: x[1], reverse=True)
    
    step += 1
    print(f'{step}. Упорядочим вершины графа в порядке не возрастания ri')
    print(', '.join([x[0] for x in s]))
    pprint(s)

print(sus(g))
