"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
вернуть первый и последний элемент в списке
"""


def get_first_last(collection: list) -> tuple:
    # TODO вставить код ниже
    result = [collection[0], collection[-1]]
    return tuple(result)


if __name__ == '__main__':
    assert (1, 7) == get_first_last([1, 2, 3, 4, 5, 6, 7])
    print('Решено!')
