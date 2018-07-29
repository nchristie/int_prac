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

        self.current_node = self.head
        if not self.check_node_has_value(self.current_node):
            return self.current_node

        for i in range(index - 1):
            if not self.check_node_has_value(self.current_node.next_node.next_node):
                return -1
            self.current_node = self.current_node.next_node

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

        # initialise node_after
        self.node_after = Node(val)

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


functions = ["MyLinkedList","addAtHead","get","addAtTail","deleteAtIndex","addAtHead","deleteAtIndex","get","addAtTail","addAtHead","addAtTail","addAtTail","addAtTail","addAtIndex","get","addAtIndex","addAtHead","deleteAtIndex","addAtIndex","addAtHead","addAtIndex","deleteAtIndex","get","addAtTail","deleteAtIndex","deleteAtIndex","addAtTail","addAtTail","addAtIndex","addAtHead","get","get","addAtTail","addAtTail","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","addAtHead","deleteAtIndex","addAtHead","get","addAtHead","get","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtTail","deleteAtIndex","get","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtIndex","deleteAtIndex","deleteAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtHead","addAtTail","addAtIndex","deleteAtIndex","deleteAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","get","addAtIndex","get","addAtHead","addAtHead","addAtHead","addAtIndex","addAtIndex","get","addAtHead","get","get","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","get","addAtTail"]
args = [[],[8],[1],[81],[2],[26],[2],[1],[24],[15],[0],[13],[1],[6,33],[6],[2,91],[82],[6],[4,11],[3],[7,14],[1],[6],[99],[11],[7],[5],[92],[7,92],[57],[2],[6],[39],[51],[3],[22],[5,26],[9,52],[69],[5,58],[79],[7],[41],[33],[88],[44],[8],[72],[93],[18],[1],[9],[46],[9],[92],[71],[69],[11,54],[27],[83],[12],[20],[19,97],[77],[36],[3],[35],[16,68],[22],[36],[17],[62],[89],[61],[6],[92],[28,69],[23],[28],[7,4],[0],[24],[52],[1],[23,3],[7],[6],[68],[79],[45,90],[41,52],[28],[25],[9],[32],[11],[90],[24],[98],[36],[34],[26]]

functions = ["MyLinkedList","addAtHead","addAtIndex","get","get","get"]
args = [[],[1],[1,2],[1],[0],[2]]

functions = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
args = [[],[1],[3],[1,2],[1],[1],[1]]

functions = ["MyLinkedList","get","addAtIndex","get","get","addAtIndex","get","get"]
args = [[],[0],[1,2],[0],[1],[0,1],[0],[1]]

# for i in range(len(functions)):
#     print('obj.{}({})'.format(functions[i], str(args[i]).replace('[','').replace(']','')))


obj = MyLinkedList()

def list_len(marker=''):
    length = len(obj.return_whole_list())
    print('{}Length of list: {}'.format(marker, length))

obj.get(0)
obj.addAtIndex(1, 2)
obj.get(0)
obj.get(1)
obj.addAtIndex(0, 1)
obj.print_whole_list()
obj.get(0)
obj.get(1)


obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.get(1)
obj.deleteAtIndex(1)
obj.get(1)


obj.addAtHead(1)
obj.addAtIndex(1, 2)


obj.get(1)
obj.get(0)
obj.get(2)



obj.addAtHead(8)
obj.get(1)
obj.addAtTail(81)
obj.deleteAtIndex(2)
obj.addAtHead(26)
obj.deleteAtIndex(2)
obj.get(1)
obj.addAtTail(24)
obj.addAtHead(15)
obj.addAtTail(0)
obj.addAtTail(13)
obj.addAtTail(1)
obj.addAtIndex(6, 33)
obj.get(6)
obj.addAtIndex(2, 91)
obj.addAtHead(82)
obj.deleteAtIndex(6)
obj.addAtIndex(4, 11)
obj.addAtHead(3)
obj.addAtIndex(7, 14)
obj.deleteAtIndex(1)
obj.get(6)
obj.addAtTail(99)
obj.deleteAtIndex(11)
obj.deleteAtIndex(7)
obj.addAtTail(5)
obj.addAtTail(92)
obj.addAtIndex(7, 92)
obj.addAtHead(57)
obj.get(2)
obj.get(6)
obj.addAtTail(39)
obj.addAtTail(51)
obj.addAtTail(3)
obj.addAtTail(22)
obj.addAtIndex(5, 26)
obj.addAtIndex(9, 52)
obj.addAtHead(69)
obj.addAtIndex(5, 58)
obj.addAtTail(79)
obj.addAtHead(7)
obj.addAtHead(41)
obj.addAtHead(33)
obj.addAtHead(88)
obj.addAtHead(44)
obj.addAtHead(8)
obj.addAtTail(72)
obj.addAtHead(93)
obj.deleteAtIndex(18)
obj.addAtHead(1)
obj.get(9)
obj.addAtHead(46)
obj.get(9)
obj.addAtHead(92)
obj.addAtHead(71)
obj.addAtHead(69)
obj.addAtIndex(11, 54)
obj.deleteAtIndex(27)
obj.addAtTail(83)
obj.deleteAtIndex(12)
obj.get(20)
obj.addAtIndex(19, 97)
obj.addAtHead(77)
obj.addAtTail(36)
obj.deleteAtIndex(3)
obj.addAtHead(35)
obj.addAtIndex(16, 68)
obj.deleteAtIndex(22)
obj.deleteAtIndex(36)
obj.deleteAtIndex(17)
obj.addAtHead(62)
obj.addAtTail(89)
obj.addAtTail(61)
obj.addAtHead(6)
obj.addAtTail(92)
obj.addAtIndex(28, 69)
obj.deleteAtIndex(23)
obj.deleteAtIndex(28)
obj.addAtIndex(7, 4)
obj.addAtHead(0)
obj.addAtHead(24)
obj.addAtTail(52)
obj.get(1)
obj.addAtIndex(23, 3)
obj.get(7)
obj.addAtHead(6)
obj.addAtHead(68)
obj.addAtHead(79)
obj.addAtIndex(45, 90)
obj.addAtIndex(41, 52)
obj.get(28)
obj.addAtHead(25)
obj.get(9)
obj.get(32)
obj.addAtTail(11)
obj.addAtHead(90)
obj.addAtHead(24)
obj.addAtTail(98)
obj.addAtTail(36)
obj.get(34)
obj.addAtTail(26)



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







