def flatten(iterable):
    flat_list = []

    for item in iterable:
        if item is None:
            continue
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list
