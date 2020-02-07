def update_dictionary(d, key, value):
    if d.get(key) is None:
        key *= 2
        if d.get(key) is None:
            d[key] = [value]
        else:
            lst = []
            for number in d.get(key):
                lst.append(number)
            lst.append(value)
            d[key] = lst
    else:
        lst = []
        for number in d.get(key):
            lst.append(number)
        lst.append(value)
        d[key] = lst