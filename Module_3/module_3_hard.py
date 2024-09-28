data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}]),
                  ]
sum_ = 0


def calculate_structure_sum(data):
    global sum_

    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for item in data:
            calculate_structure_sum(item)
    elif isinstance(data, dict):
        for value in data.values():
            calculate_structure_sum(value)
        for key in data.keys():
            calculate_structure_sum(key)
    elif isinstance(data, int) or isinstance(data, str):
        if isinstance(data, int):
            sum_ += data
        elif isinstance(data, str):
            sum_ += len(data)
    return sum_


result = calculate_structure_sum(data_structure)
print(result)
