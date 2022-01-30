def difference_between_list_unique(x, y):
    set_x = set(x)
    set_y = set(y)
    comparison = set_x.difference(set_y)
    return list(comparison)


def difference_by_function(x, y, fn):
    y = set(map(fn, y))
    return [item for item in x if fn(item) not in y]

def has_duplicates_list(x):
    return len(x) != len(set(x))