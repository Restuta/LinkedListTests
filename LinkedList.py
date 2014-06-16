#implement LinkedList class here

#initialize elements with object and link onto the next element
#add element to the end of list
#delete element by index
#insert element
#fined element


class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return '%s' % self.value

class LinkedList:
    last_node = None
    first_node = None
    def add(self, new_nodes_value):
        if self.last_node is None:
            self.last_node = Node(new_nodes_value)
            self.first_node = Node(new_nodes_value)
        else:
            current_node = Node(new_nodes_value)
            self.last_node.next_node = current_node
            self.last_node = current_node

    #def get(self, node_number):
    #    for index in range(node_number + 1):
            #my_nodes_value = my_nodes_value.next_node
    #    return my_nodes_value


#element1 = Node(5)
#print(element1)
#element2 = Node(6, element1)
#print(element2, element2.next_element)

