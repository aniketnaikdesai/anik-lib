def spread_list(x):
    ret = []
    for i in x:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten_list(x):
    flat_list = []
    [flat_list.extend(deep_flatten(a)) for x in x] if isinstance(x, list) else flat_list.append(x)
    return flat_list