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




#element1 = Node(5)
#print(element1)
#element2 = Node(6, element1)
#print(element2, element2.next_element)

