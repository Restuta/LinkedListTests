import unittest
from LinkedList import *

#todo: add tests to make sure class impelement iterators (so it can be enumerated through for loop: https://docs.python.org/2/tutorial/classes.html#iterators)

class add_and_count_tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_when_one_item_has_been_added_should_return_count_equal_to_one(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        self.assertEqual(linked_list.count, 1)

    def test_when_two_items_have_been_added_should_return_count_equal_to_two(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        self.assertEqual(linked_list.count, 2)

    def test_when_adding_item_should_be_able_to_get_it_back(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        item_from_list = linked_list.get_last()
        self.assertEqual(item_from_list.value, 'test item 0')

    def test_when_adding_several_items_should_be_able_to_get_last_one(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        item_from_list = linked_list.get_last()
        self.assertEqual(item_from_list.value, 'test item 1')

    def test_when_adding_several_items_should_be_able_to_get_first_one(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        item_from_list = linked_list.get(0)
        self.assertEqual(item_from_list, 'test item 0')

    def test_when_adding_several_items_should_be_able_to_get_arbitrary_item_by_index(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.add('test item 2')
        linked_list.add('test item 3')
        item_from_list = linked_list.get(2)
        self.assertEqual(item_from_list, 'test item 2')

class remove_tests(unittest.TestCase):
    def test__remove__when_one_item_have_been_added_and_then_removed_then_count_should_be_0(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.remove(0)
        self.assertEqual(linked_list.count, 0)

    def test_when_two_items_have_been_added_and_then_one_item_removed_then__get_last__should_return_first_item(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.remove(1)
        item_from_list = linked_list.get_last()
        self.assertEqual(item_from_list, 'test item 0')

if __name__ == '__main__':
    unittest.main()