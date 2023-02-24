from task2 import parse_json
from task4 import read, write


def val2toml(item: any):
    match item:
        case str():
            return item.__repr__()
        case list():
            return f'[{", ".join(val2toml(i) for i in item)}]'
        case _:
            raise RuntimeError('forbidden type')


def obj2toml(item: dict, parent=''):
    res = []

    def tables_at_end(item):
        _, value = item
        return isinstance(value, dict)

    for (key, val) in sorted(item.items(), key=tables_at_end):
        path = f"{parent}.{key}" if parent else key
        match val:
            case dict():
                res.append(f'\n[{path}]\n{obj2toml(val, path)}')
            case list():
                small = True
                if len(val) != 0:
                    if val[0] is dict:
                        small = False
                if small:
                    for i in val:
                        res.append(f'\n[[{path}]]\n{obj2toml(i, path)}')
                else:
                    res.append(f'\n[[{path}]]\n{obj2toml(val, path)}')
            case _:
                res.append(f'{key} = {val2toml(val)}')
    return '\n'.join(res)


def task5():
    s = read()
    d = parse_json(s)
    res = obj2toml(d)
    write(5, res, 'toml')
