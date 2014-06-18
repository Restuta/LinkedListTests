import unittest
from LinkedList import *

# todo: add tests to make sure class implement iterators (so it can be enumerated through for loop: https://docs.python.org/2/tutorial/classes.html#iterators)
class get_first_and_get_last_tests(unittest.TestCase):
    def test_when_adding_several_items_should_be_able_to_get_last_one(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        last_node = linked_list.get_last()
        self.assertEqual(last_node.value, 'test item 1')

    def test_when_one_item_has_been_added_it_should_be_returned_as_last_one(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        self.assertEqual(linked_list.get_last().value, 'test item 0')

    def test_when_one_item_has_been_added_it_should_be_returned_as_first_one(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        self.assertEqual(linked_list.get_first().value, 'test item 0')

    def test_when_adding_several_items_should_be_able_to_get_first_one(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        first_node = linked_list.get_first()
        self.assertEqual(first_node.value, 'test item 0')


class add_get_tests(unittest.TestCase):
    def test_when_adding_second_element_previous_one_should_point_to_it(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        first_node = linked_list.get(0)

        linked_list.add('test item 1')

        self.assertEqual(first_node.next_node, linked_list.get_last())

    def test_when_adding_several_items_should_be_able_to_get_arbitrary_node_by_index(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.add('test item 2')
        linked_list.add('test item 3')
        node = linked_list.get(2)
        self.assertEqual(node.value, 'test item 2')

    def test_when_adding_several_items_should_be_able_to_get_first_node_by_index(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.add('test item 2')
        linked_list.add('test item 3')
        first_node = linked_list.get(0)
        self.assertEqual(first_node.value, 'test item 0')

    def test_when_adding_several_items_should_be_able_to_get_last_node_by_index(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.add('test item 2')
        linked_list.add('test item 3')
        last_node = linked_list.get(3)
        self.assertEqual(last_node.value, 'test item 3')


class count_tests(unittest.TestCase):
    def test_when_no_items_has_been_added_should_return_count_equal_to_0(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.count, 0)

    def test_when_one_item_has_been_added_should_return_count_equal_to_1(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        self.assertEqual(linked_list.count, 1)

    def test_when_two_items_have_been_added_should_return_count_equal_to_2(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        self.assertEqual(linked_list.count, 2)


class remove_tests(unittest.TestCase):
    def test__remove__when_one_item_have_been_added_and_then_removed_then_count_should_be_0(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.remove(0)
        self.assertEqual(linked_list.count, 0)

    def test_when_3_items_have_been_added_and_last_one_removed_then__get_last__should_return_second_item_with_no_next_node(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.add('test item 2')
        linked_list.remove(2)
        last_node = linked_list.get_last()
        self.assertEqual(last_node.value, 'test item 1')
        self.assertIsNone(last_node.next_node)

    def test_when_3_items_have_been_added_and_then_middle_item_removed_then__get_last__should_return_third_node_with_no_next_node(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.add('test item 2')
        linked_list.remove(1)
        last_node = linked_list.get_last()
        self.assertEqual(last_node.value, 'test item 2')
        self.assertIsNone(last_node.next_node)

    def test_when_3_items_have_been_added_and_then_middle_item_removed_then_first_item_should_point_to_third_one(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.add('test item 2')
        linked_list.remove(1)

        first_node = linked_list.get_first()
        self.assertEqual(first_node.next_node.value, 'test item 2')

    def test_when_3_items_have_been_added_and_then_first_item_removed_3_times_count_should_be_0(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.add('test item 1')
        linked_list.add('test item 2')
        linked_list.remove(0)
        linked_list.remove(0)
        linked_list.remove(0)
        self.assertEqual(linked_list.count, 0)

    def test_when_1_item_have_been_added_and_removed_then_first_item_should_not_be_present(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.remove(0)
        self.assertIsNone(linked_list.get_first())

    def test_when_1_item_have_been_added_and_removed_then_last_item_should_not_be_present(self):
        linked_list = LinkedList()
        linked_list.add('test item 0')
        linked_list.remove(0)
        self.assertIsNone(linked_list.get_last())


if __name__ == '__main__':
    unittest.main()