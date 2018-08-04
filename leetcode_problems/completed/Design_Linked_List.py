'''
Design your implementation of the linked list. You can choose to use the singly
linked list or the doubly linked list. A node in a singly linked list should
have two attributes: val and next. val is the value of the current node, and
next is a pointer/reference to the next node. If you want to use the doubly
linked list, you will need one more attribute prev to indicate the previous
node in the linked list. Assume all nodes in the linked list are 0-indexed.
Implement these functions in your linked list class:
get(index) : Get the value of the index-th node in the linked list. If the
index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked
list. After the insertion, the new node will be the first node of the linked
list.
addAtTail(val) : Append a node of value val to the last element of the linked
list.
addAtIndex(index, val) : Add a node of value val before the index-th node in
the linked list. If index equals to the length of linked list, the node will
be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the
index is valid.
Example:
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:
All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
'''

import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG)
debug = logging.debug

####################################################################################
class Node(object):
    def __init__(self, val=None):
        self.val = None
        self.next_node = None


def debug(arg):
    pass


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.head.next_node = Node()


    def debug_whole_list(self):
        if not self.check_node_has_value(self.head):
            debug('No list to debug')
            return

        current_node = self.head

        list_to_debug = []

        while self.check_node_has_value(current_node):
            list_to_debug.append(current_node.val)
            current_node = current_node.next_node

        debug('{}'.format(list_to_debug))


    def print_whole_list(self):
        if not self.check_node_has_value(self.head):
            print('No list to print')
            return

        current_node = self.head

        list_to_print = []

        while self.check_node_has_value(current_node):
            list_to_print.append(current_node.val)
            current_node = current_node.next_node

        print('{}'.format(list_to_print))


    def return_whole_list(self):
        if not self.check_node_has_value(self.head):
            return('No list to print')
            return

        current_node = self.head

        list_to_return = []

        while self.check_node_has_value(current_node):
            list_to_return.append(current_node.val)
            current_node = current_node.next_node

        return list_to_return


    def check_node_has_value(self, node):
        """
        Checks if a node exists and has a value
        deals with if the value is zero
        :param node: Node() 
        :return: Boolean
        """

        if node.val == 0:
            return True
        elif node.val == None:
            return False
        else:
            return True


    def create_new_node(self, val=None):
        self.new_node = Node()
        self.new_node.val = val
        self.new_node.next_node = Node()
        return self.new_node


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is
        invalid, return -1.
        :type index: int
        :rtype: int
        """
        if not self.check_node_has_value(self.head):
            return -1

        self.current_node = self.head
        debug('---for loop in to get value at index about to begin---')

        for i in range(index):
            self.current_node = self.current_node.next_node
            if not self.check_node_has_value(self.current_node):
                return -1

        return self.current_node.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked
        list.
        :type val: int
        :rtype: void
        """

        new_node = Node()
        new_node.val = val# if val != 0 else 'zero'
        new_node.next_node = self.head
        self.head = new_node
        debug('addAtHead({})'.format(val))


    def traverse_to_tail(self):

        self.current_node = self.head

        while self.check_node_has_value(self.current_node.next_node):
            self.current_node = self.current_node.next_node

        return self.current_node


    def traverse_to_index(self, index):

        if not self.check_node_has_value(self.head)\
                or not self.check_node_has_value(self.head.next_node):
            return self.head

        self.current_node = self.head
        for i in range(index-1):
            self.current_node = self.current_node.next_node
            if not self.check_node_has_value(self.current_node):
                return -1
        return self.current_node


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """

        if not self.check_node_has_value(self.head):
            self.head.val = val
            return

        self.new_node = self.create_new_node(val)
        self.current_node = self.traverse_to_tail()
        self.current_node.next_node = self.new_node


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """

        if index == 0:
            self.new_node = Node()
            self.new_node.val = val
            self.new_node.next_node = self.head
            self.head = self.new_node
            return

        # check if head of list has a value, exit function if not
        if not self.check_node_has_value(self.head):
            return

        # make new node
        self.new_node = self.create_new_node(val)

        # traverse list
        self.current_node = self.traverse_to_index(index)
        if self.current_node == -1:
            return
        else:
            if self.check_node_has_value(self.current_node.next_node):
                self.node_after = self.current_node.next_node
                self.current_node.next_node = self.new_node
                self.new_node.next_node = self.node_after
            else:
                self.current_node.next_node = self.new_node


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        # check if head of list has a value, exit function if not
        if not self.check_node_has_value(self.head):
            return

        self.current_node = self.traverse_to_index(index)
        if self.current_node == -1:
            return

        if not self.check_node_has_value(self.current_node):
            return -1

        # check if the node after the one you want to delete exists
        if not self.check_node_has_value(self.current_node.next_node):
            # assign value of the current_node's next node to None, end function
            self.current_node.next_node = Node()
            debug('Breaking loop for deleteAtIndex as the index to be deleted was the final one')
            return

        # if node two places after exists assign it to current_node.next_node
        self.current_node.next_node = self.current_node.next_node.next_node

        debug('deleteAtIndex({})'.format(index))










