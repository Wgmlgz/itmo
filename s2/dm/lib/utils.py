from pprint import pprint


Graph = list[list[int | None]]


def normalize(g: Graph) -> list[list[int]]:
    return [[0 if x == None or x == 0 else 1 for x in line] for line in g]


def as_str(g: Graph) -> list[list[str]]:
    return [['' if x == None else str(x) for x in line] for line in g]


def latex(g: Graph) -> str:
    s = as_str(g)

    s = [[f'e{i + 1}', *line] for i, line in enumerate(s)]

    s = [['v/v', *(f'e{i + 1}' for i, line in enumerate(s))], *s]
    
    s = [' & '.join(line) for line in s]
    return s
    # return str([[0 if x == None or x == 0 else 1 for x in line] for line in as_str(g)])
