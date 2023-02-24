def has_edges(arr: list[list[int | None]]) -> list[list[int]]:
    return [[0 if x == None or x == 0 else 1 for x in line] for line in arr]
