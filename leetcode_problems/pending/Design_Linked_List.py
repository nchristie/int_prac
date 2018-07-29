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


class Node(object):
    def __init__(self, val=None):
        self.val = None
        self.next_node = None


# def debug(arg):
#     pass


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.head.next_node = Node()


    def debug_whole_list(self):
        if not self.head.val:
            debug('No list to debug')
            return

        current_node = self.head

        list_to_debug = []

        while current_node.val:
            list_to_debug.append(current_node.val)
            current_node = current_node.next_node

        debug('{}'.format(list_to_debug))


    def print_whole_list(self):
        if not self.head.val:
            print('No list to print')
            return

        current_node = self.head

        list_to_print = []

        while current_node and current_node.val:
            list_to_print.append(current_node.val)
            current_node = current_node.next_node

        print('{}'.format(list_to_print))


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
        if not self.head.val:
            return -1

        self.current_node = self.head

        for i in range(index):
            self.current_node = self.current_node.next_node
            if not self.current_node:
                return -1
            if not self.current_node.val:
                return -1
        debug('get() has run, current_node_val: {}'.format(self.current_node.val))
        return self.current_node.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked
        list.
        :type val: int
        :rtype: void
        """
        if not self.head:
            self.head.val = val
        else:
            new_node = Node()
            new_node.val = val
            new_node.next_node = self.head
            self.head = new_node
        debug('addAtHead({})'.format(val))


    def traverse_to_tail(self):
        i=0
        self.current_node = self.head

        while self.current_node.next_node.val:
            debug('At index {}, value of {}'.format(i, self.current_node.val))
            self.current_node = self.current_node.next_node
            i += 1
        debug('\n---while loop for traverse to tail finished at index {}, value of {}---'.format(
            i, self.current_node.val))
        return self.current_node


    def traverse_to_index(self, index):
        debug('\n---While loop about to begin to traverse to index---')
        for i in range(index - 1):
            debug('At index {}, value of {}'.format(i, self.current_node.val))
            if not self.current_node.next_node or not self.current_node.next_node.val:
                debug('Traverse to index ended, index {} is longer than list of {}'.format(index, i))
                return -1
            self.current_node = self.current_node.next_node
        debug('\n---while loop for traverse to index finished at index {}, value of {}---'.format(
            i + 1, self.current_node.val))
        return self.current_node

    def traverse_list(self, index=None):
        """traverses list from head to tail
        if an index is given will traverse from head up to the position before the index
        """
        i = 0

        self.current_node = self.head
        if not self.current_node.val:
            return self.current_node

        if not self.current_node.next_node:
            return self.current_node

        if not self.current_node.next_node.val:
            return self.current_node.next_node

        if not index:
            self.traverse_to_tail()
        else:
            self.traverse_to_index(index)


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """

        if not self.head.val:
            self.head.val = val
            return

        self.new_node = self.create_new_node(val)

        debug('\n---While loop about to begin for addAtTail---')
        self.current_node = self.traverse_to_tail()

        if self.current_node == -1:
            return

        try:
            if self.current_node \
                    and self.current_node.val \
                    and self.current_node.next_node \
                    and self.current_node.next_node.val:
                debug('current_node.next_node.val is: {}'.format(self.current_node.next_node.val))

            self.current_node.next_node = self.new_node

            debug('current_node.next_node.val is has been changed to new_node, value is: {}'.format(
            self.current_node.next_node.val))

            self.current_node = self.current_node.next_node
            debug('current_node moved forward by one, value of current_node is {}'.format(self.current_node.val))

            debug('current_node.next_node.val is {}'.format(self.current_node.next_node.val))
        except:
            return


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        # check if head of list has a value, exit function if not
        if not self.head.val:

            return

        # initialise node_after
        self.node_after = None

        # make new node
        self.new_node = self.create_new_node(val)

        # traverse list
        self.current_node = self.traverse_list(index)
        if self.current_node == -1:

            return
        else:
            try:
                self.node_after = self.current_node.next_node
                self.current_node.next_node = self.new_node
                self.new_node.next_node = self.node_after
            except:
                pass


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        # check if head of list has a value, exit function if not
        if not self.head.val:
            return

        self.current_node = self.traverse_list(index)
        if self.current_node == -1:
            return

        if not self.current_node or self.current_node.val:
            return -1

        # check if the node after the one you want to delete exists
        if not self.current_node.next_node \
                or not self.current_node.next_node.next_node \
                or not self.current_node.next_node.next_node.val:
            # assign value of the current_node's next node to None, end function
            self.current_node.next_node = Node()
            debug('Breaking loop for deleteAtIndex as the index to be deleted was the final one')
            return

        # if node two places after exists store as node_after
        self.node_after = self.current_node.next_node.next_node
        # assign value of the current_node's next node to the one after the one you want to delete
        self.current_node.next_node = self.node_after
        debug('deleteAtIndex({})'.format(index))


##################################################################################################
def check_output(function_call, expected, actual):
    if expected == actual:
        return
    else:
        if not actual:
            actual = None
        output = ('{}: {}!={}'.format(function_call, expected, actual))
        debug(output)

#Your MyLinkedList object will be instantiated and called as such:

functions = ["MyLinkedList","addAtHead","get","addAtTail","deleteAtIndex","addAtHead","deleteAtIndex","get","addAtTail","addAtHead","addAtTail","addAtTail","addAtTail","addAtIndex","get"]
args = [[],[8],[1],[81],[2],[26],[2],[1],[24],[15],[0],[13],[1],[6,33],[6]]

# for i in range(len(functions)):
#     print('obj.{}({})'.format(functions[i], str(args[i]).replace('[','').replace(']','')))


obj = MyLinkedList()
obj.print_whole_list()

obj.addAtHead(8)
obj.print_whole_list()

obj.get(1)

obj.addAtTail(81)
obj.print_whole_list()

obj.deleteAtIndex(2)
obj.print_whole_list()

obj.addAtHead(26)
obj.print_whole_list()

obj.deleteAtIndex(2)
obj.print_whole_list()

obj.get(1)

obj.addAtTail(24)
obj.print_whole_list()

obj.addAtHead(15)
obj.print_whole_list()

obj.addAtTail(0)
obj.print_whole_list()

obj.addAtTail(13)
obj.print_whole_list()

obj.addAtTail(1)
obj.print_whole_list()

obj.addAtIndex(6, 33)
obj.print_whole_list()

obj.get(6)

# obj = MyLinkedList()
#
# actual_output = obj.get(0) # (Fakenode) -> None
# expected_output = -1
# check_output('obj.get(0)', expected_output, actual_output)
# obj.debug_whole_list()
# debug('(Fakenode) -> None\n')
#
#
#
# obj.addAtHead(1) # 1 -> None
# actual_output = obj.get(0) # (1) -> None
# expected_output = 1
# check_output('obj.addAtHead(1)', expected_output, actual_output)
# obj.debug_whole_list()
# debug('1 -> None\n')
#
# obj.addAtHead(2) # 2 -> 1 -> None
# actual_output = obj.get(0) # (2) -> 1 -> None
# expected_output = 2
# debug(check_output('obj.addAtHead(2)', expected_output, actual_output))
# obj.debug_whole_list()
# debug('2 -> 1 -> None\n')
#
#
# obj.addAtHead(3) # 3 -> 2 -> 1 -> None
# actual_output = obj.get(0) # (3) -> 2 -> 1 -> None
# expected_output = 3
# check_output('obj.addAtHead(3)', expected_output, actual_output)
# obj.debug_whole_list()
# debug('3 -> 2 -> 1 -> None\n')
#
# actual_output = obj.get(1)  # 3 -> (2) -> 1 -> None
# expected_output = 2
# check_output('obj.get(1)', expected_output, actual_output)
#
# actual_output = obj.get(2) # 3 -> 2 -> (1) -> None
# expected_output = 1
# check_output('obj.get(2)', expected_output, actual_output)
#
# obj.addAtTail(10) # 3 -> 2 -> 1 -> 10 -> None
# actual_output = obj.get(3) # 3 -> 2 -> 1 -> (10) -> None
# expected_output = 10
# debug(check_output('obj.addAtTail(10)', expected_output, actual_output))
# obj.debug_whole_list()
# debug('3 -> 2 -> 1 -> 10 -> None\n')
#
# obj.addAtTail(99) # 3 -> 2 -> 1 -> 10 -> None
# actual_output = obj.get(4) # 3 -> 2 -> 1 -> (10) -> None
# expected_output = 99
# debug(check_output('obj.addAtTail(99)', expected_output, actual_output))
# obj.debug_whole_list()
# debug(('3 -> 2 -> 1 -> 10 -> 99 -> None\n'))
#
# obj.addAtIndex(2,15) # 3 -> 2 -> 15 -> 1 -> (10) -> None
# actual_output = obj.get(2)
# expected_output = 15
# obj.debug_whole_list()
# debug(('3 -> 2 -> 15 -> 1 -> 10 -> 99 -> None\n'))
#
# obj.deleteAtIndex(1) # 3 -> 15 -> 1 -> 10 -> None
# obj.debug_whole_list()
# debug(('3 -> 15 -> 1 -> 10 -> 99 -> None\n'))


##numbers = MyLinkedList()
##numbers.addAtHead('two')
##numbers.addAtHead('one')
##numbers.addAtHead('zero')
##numbers.debug_whole_list()
##
##numbers.addAtTail('Three')
##numbers.debug_whole_list()
##
##numbers.addAtTail('Four')
##numbers.debug_whole_list()
##
##numbers.addAtTail('Six')
##numbers.debug_whole_list()
##
##numbers.addAtIndex(5, 'Five')
##numbers.debug_whole_list()
##
##numbers.addAtIndex(8, 'Eight')
##numbers.debug_whole_list()
##
##numbers.addAtIndex(1, 'Seven')
##numbers.debug_whole_list()
##
##numbers.deleteAtIndex(1)
##numbers.debug_whole_list()







