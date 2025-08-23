def saddle_points(matrix):
    row_sizes = {len(elem) for elem in matrix}

    if len(row_sizes) > 1:
        raise ValueError("irregular matrix")

    points = []

    for i, values in enumerate(matrix):
        for j, value in enumerate(values):
            if value >= max(matrix[i]) and value <= min(v[j] for v in matrix):
                points.append({"row": i + 1, "column": j + 1})

    return points
