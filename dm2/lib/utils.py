from pprint import pprint
from typing import List, Optional
import math

Graph = List[List[Optional[int]]]


def normalize(g: Graph) -> List[List[int]]:

    return [[0 if x == None or x == 0 else 1 for x in line] for line in g]


def as_str(g: Graph) -> List[List[str]]:
    return [['' if x == None else str(x) for x in line] for line in g]


def latex(g: Graph, top_prefix="e") -> str:
    m = max([len(line) for line in g])
    s = as_str(g)

    s = [[f'e{i + 1}', *line] for i, line in enumerate(s)]
    s = [['v/v', *(f'{top_prefix}{i + 1}' for i in range(m))], *s]

    def sus(x):
        s = str(x)

        if s == 'inf':
            return '$\\infty$'
        return s
    s = [' & '.join([sus(x) for x in line]) for line in s]
    s = ' \\nl '.join(s)
    s = '$$\\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|} \\hline ' + \
        s + '\\nl \\end{tabular}$$'
    return s
    # return str([[0 if x == None or x == 0 else 1 for x in line] for line in as_str(g)])


def rotate(original):
    return list(zip(*original[::]))
