def _(tape=[]):
    return tape


def execute_pipeline(l=_(), *args, **kwars):
    for index, func in enumerate(_):
        print(func())
        if index == 0:
            result = func(_=_(), *args, **kwars)
        else:
            result = func(result)
    return result

def get10(*args, **kwargs):
    return 10

def push(value, l=_()):
    l.append(value)
    return l

def pop(l=_()):
    return l.pop()

def flush(l=_()):
    _ = []
    return _

def read(i, l=_()):
    try:
        return l[i]
    except:
        expand(i)
        return l[i]

def pp(start=None, end=None, _=_()):
    if start is None and end is None:
        print(_)
    else:
        if start is None:
            start = 0
        elif end is None:
            end = len(_)
        print(_[start:end])

def expand(i, _=_()):
    if i >= len(_):
        diff = i - len(_) + 1
        _ += [0] * (diff)
    return _, diff

def add(v=1, i=None, _=_()):
    if i is None:
        i = len(_) - 1
    _[i] += v
    return _[i], i

def write(i, v, _=_()):
    try:
        _[i] = v
    except:
        expand(i)
        _[i] = v
    return _[i], i

def head(_=_()):
    return _[0]

def tail(_=_()):
    return _[-1]



push(10)
push(3)
push(100)

pop()
push(122)
add()

boy = read(100)
boy = 1
print(read(100))
pp()

print(tail())