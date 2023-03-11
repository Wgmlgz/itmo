from pprint import pprint
import lib.utils as utils
import math
import queue

# arr = [
# [None, 1   , None, 2   ],    #1
# [1   , None, 5   , None],    #2
# [None, 5   , None, 1   ],    #3
# [2   , None, 1   , None],    #4
# ]


# arr = [[0, 5, None, None, 1, None, None, 1, 1, None, 2, 3],
#        [5, 0, None, None, 5, 2, 4, None, 4, None, 5, 1],
#        [None, None, 0, None, None, 2, 3, 3, 3, None, 4, None],
#        [None, None, None, 0, 4, 2, None, None, None, 1, 3, 3],
#        [1, 5, None, 4, 0, None, None, 1, None, 5, 3, None],
#        [None, 2, 2, 2, None, 0, None, 3, 1, None, None, 1],
#        [None, 4, 3, None, None, None, 0, 2, 5, 2, 3, None],
#        [1, None, 3, None, 1, 3, 2, 0, 5, None, 1, 1],
#        [1, 4, 3, None, None, 1, 5, 5, 0, None, 3, None],
#        [None, None, None, 1, 5, None, 2, None, None, 0, None, 1],
#        [2, 5, 4, 3, 3, None, 3, 1, 3, None, 0, None],
#        [3, 1, None, 3, None, 1, None, 1, None, 1, None, 0]]


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

g = arr
utils.latex(arr)

n = 12
dist = [math.inf for _ in range(n)]
history = []
dist[0] = 0
done = set()
done.add(0)
# print(utils.latex(dist))

time = 0
history.append(dist.copy())

q = queue.PriorityQueue()


def sus(x, w):
    global time
    time += 1

    Ge = []
    for i, v in enumerate(g[x]):
        if v is None or i == x or i in done:
            continue
        else:
            Ge.append(f'e{i + 1}')

    print('\\item ', end='')
    print('Не все вершины имеют постоянные пометки,')
    print()
    print(f'Гe{x + 1} = {{{", ".join(Ge)}}}')
    print()
    if len(Ge) != 0:
        print(f'Временные пометки имеют вершины {", ".join(Ge)} - уточняем их')

        print('\\begin{itemize}')
        for i, v in enumerate(g[x]):
            if v is None or i == x or i in done:
                continue
            a = dist[i]
            b = w
            c = g[x][i]
            m = min(a, b + c)
            q.put((m, i))
            # if m < mm:
            #     mm = m
            #     idx = i
            print(f'\\item $l(e{i+1}) = min({a}, {b} + {c}) = {m}$')
            dist[i] = m
        print('\\end{itemize}')

    mm, idx = math.inf, -1
    while idx == -1 or idx in done:
        mm, idx = q.get()
    print('\\item ', end='')
    print(f'$I(ei+) = min[I(ei)] = l(e{idx+1}) = {mm}$')
    print('\\item ', end='')
    print(
        f'Вершина e{idx+1} получает постоянную пометку l(e{idx+1}) = {mm}+, p = e{idx+1}')

    history.append([None if i in done else (str(x)+'+'if idx == i else x)
                   for i, x in enumerate(dist)])
    done.add(idx)
    print('\\item ', end='')
    print(utils.latex(utils.rotate(utils.rotate(utils.rotate(history))), top_prefix=''))

    if len(Ge) == 0:
        return
    sus(idx, mm)


print('Исходная таблица соединений R:')
print(utils.latex(arr))
print('Найти кратчайшие пути от начальной вершины e1 ко всем остальным вершинам')
print('\\begin{enumerate}')
print('\\item $l(e1) = 0+; l(ei) = \\infty, для всех i \\ne 1, p = e1$')
print(utils.latex(utils.rotate(utils.rotate(utils.rotate(history)))))
sus(0, 0)
print('\\end{enumerate}')
