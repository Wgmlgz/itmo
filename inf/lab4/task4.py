from pathlib import Path


def read():
    return open(Path(__file__).with_name('input.json')).read()


def write(idx: int, out: str, ext='xml'):
    open(Path(__file__).with_name(f'out{idx}.{ext}'), mode="w+").write(out)


def task4():
    from task1 import task1
    from task2 import task2
    from task3 import task3
    from timeit import timeit
    s = read()

    write(1, task1(s))
    write(2, task2(s))
    write(3, task3(s))

    res = '\n'.join(
        s + str(t) for (s, t) in
        [
            ('no lib + no regex: ', timeit("task1(s)", globals=locals(), number=100)),
            ('lib: ', timeit("task2(s)", globals=locals(), number=100)),
            ('regex: ', timeit("task3(s)", globals=locals(), number=100))
        ]
    )
    open(Path(__file__).with_name(f'out4.txt'), mode="w+").write(res)
    print(res)