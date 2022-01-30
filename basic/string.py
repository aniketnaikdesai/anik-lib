def check_for_sub_string(x,y):
    for z in y:
        if x in z:
            return z
    return 'not found'


def isblank(x):
    return not (x and x.strip()) #test if a string is either None OR Empty OR Blank