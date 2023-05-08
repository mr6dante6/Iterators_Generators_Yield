# _____Первое задание_____

class FlatIterator:
    def __init__(self, list_of_list):
        self.flat_list = []
        for lst in list_of_list:
            if isinstance(lst, list):
                self.flat_list += lst
            else:
                self.flat_list.append(lst)
        self.index = 0

    def __iter__(self):
        self.index = 0  # обнуление индекса
        return self

    def __next__(self):
        if self.index >= len(self.flat_list):
            raise StopIteration
        else:
            item = self.flat_list[self.index]
            self.index += 1
            print(item)
            return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


# _____Второе задание_____

import types


def flat_generator(list_of_lists):
    for lst in list_of_lists:
        if isinstance(lst, list):
            yield from flat_generator(lst)
        else:
            print(lst)
            yield lst


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()


# _____Третье задание_____

class FlatIterator:

    def __init__(self, list_of_list):
        self.flat_list = []
        self.flatten_list(list_of_list)
        self.index = 0

    def flatten_list(self, lst):
        for item in lst:
            if isinstance(item, list):
                self.flatten_list(item)
            else:
                self.flat_list.append(item)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.flat_list):
            raise StopIteration
        else:
            item = self.flat_list[self.index]
            self.index += 1
            print(item)
            return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()


# _____Четвёртое задание_____

import types


def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            print(item)
            yield item


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
