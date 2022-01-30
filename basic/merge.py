def merge_dicts(*args):
    if len(args)==0:
        return "empty argument list"
    else:
        x =args[0].copy()
        for arg in args[1:]:
            x.update(arg)
        return x