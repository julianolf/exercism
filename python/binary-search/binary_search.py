def find(search_list, value):
    start = 0
    end = len(search_list) - 1
    middle = 0

    while start <= end:
        middle = (start + end) // 2

        if search_list[middle] < value:
            start = middle + 1
        elif search_list[middle] > value:
            end = middle - 1
        else:
            return middle

    raise ValueError("value not in array")
