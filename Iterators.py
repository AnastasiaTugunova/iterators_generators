
class FlatIterator:

    def __init__(self, list_of_list):
        self.lists = list_of_list

    def __iter__(self):
        self.outer_list = 0
        self.inner_list = -1
        return self

    def __next__(self):
        self.inner_list += 1
        if self.inner_list == len(self.lists[self.outer_list]):
            self.outer_list += 1
            self.inner_list = 0
        if self.outer_list >= len(self.lists):
            raise StopIteration
        return self.lists[self.outer_list][self.inner_list]


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