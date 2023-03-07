dic = {'a': {'b':{'u':1}}, 'c':2, 'f':{'g':{'h':2}}, 'p':{'i':{'j':{'k':14}}}}
print(type(dic))


def find_val(dic, path = None, result = None):
    if path == None:
        path = []
    if result == None:
        result = []
    for key, value in dic.items():
        if not isinstance(value, dict):
            path.append(key)
            result.append((tuple(path), value))
            path.pop()
        else:
            path.append(key)
            find_val(value, path, result)
            path.pop()
    return tuple(result)

print(find_val(dic))
