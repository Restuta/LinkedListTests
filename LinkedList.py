#implement LinkedList class here

#initialize elements with object and link onto the next element
#add element to the end of list
#delete element by index
#insert element
#find element


class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return '%s' % self.value

class LinkedList:
    last_node = None
    first_node = None
    count = 0
    has_loops = False

    def __repr__(self):
        return 'first element in list is %s' % self.first_node

    def has_loop(self):
        if self.count < 2:
            self.has_loops = False
        else:
            current_node = self.first_node
            for index in range (self.count):
                if current_node is self.last_node:
                    if index is not (self.count - 1):
                        self.has_loops = True
                else:
                    if index is (self.count - 1):
                        self.has_loops = True
        if self.last_node.next_node is not None:
            self.has_loops = True
        return self.has_loops



    def add(self, new_nodes_value):
        if self.last_node is None:
            self.last_node = Node(new_nodes_value)
            self.first_node = self.last_node
            self.count = 1
        else:
            current_node = Node(new_nodes_value)
            self.last_node.next_node = current_node
            self.last_node = current_node
            self.count += 1


    def get(self, node_number):
        current_node = self.first_node
        if node_number > 0:
            for index in range(1, node_number + 1):
                current_node = current_node.next_node
        return current_node

    def get_last(self):
        return self.last_node

    def get_first(self):
        return self.first_node

    def remove(self, removed_node_number):
        node_before_removed_node = self.get(removed_node_number - 1)
        if removed_node_number == self.count - 1:
            node_before_removed_node.next_node = None
            self.last_node = node_before_removed_node
        else:
            node_before_removed_node.next_node = node_before_removed_node.next_node.next_node
        self.count -= 1
        if self.count == 0:
            self.first_node = None
            self.last_node = None




