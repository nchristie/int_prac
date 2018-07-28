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


class Node(object):
    def __init__(self, val=None):
        self.val = None
        self.next_node = None



class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.head.next_node = None
        self.head.val = None


    def print_whole_list(self):
        if not self.head.val:
            print('No list to print')#
            return

        current_node = self.head

        list_to_print = []

        while current_node.val:
            list_to_print.append(current_node.val)
            current_node = current_node.next_node

        print('{}'.format(list_to_print))
        return list_to_print


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
            if not self.current_node.val:
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
        if not self.head:
            self.head.val = val
        else:
            new_node = Node()
            new_node.val = val
            new_node.next_node = self.head
            self.head = new_node
        # if the list was empty
        # list -> fakenode
        # addAtHead(1)
        # addAtHead(2)
        # list = 1 -> 2 -> fakenode

        # emptylist
        # addAtTail(1)
        # addAtTail(2)
        # list = fakenode -> 1 -> 2


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        #print('addAtTail called')
        if not self.head.val:
            self.head.val = val
            print('head.val = None')
            return

        self.new_node = Node()
        #print('new_node created as Node')
        self.new_node.val = val
        #print('new_node value set to {}'.format(self.new_node.val))
        self.new_node.next_node = 'waiting for a better value'
        self.current_node = self.head
        #print('current_node set to self.head')
        i=0
        #print('\n---While loop about to begin---')

        while self.current_node.next_node.val:
            #print('We are at index {}, value of {}'.format(i, self.current_node.val))
            self.current_node = self.current_node.next_node
            i = i+1

        #print('\n---while loop has now ended---')
        #print('We are at index {}, value of {}'.format(i, self.current_node.val))
        #print('current_node.next_node.val is: {}'.format(self.current_node.next_node.val))
        self.current_node.next_node = self.new_node
        #print('current_node.next_node.val is has been changed to new_node, value is: {}'.format(self.current_node.next_node.val))
        self.current_node = self.current_node.next_node
        #print('current_node moved forward by one, value of current_node is {}'.format(self.current_node.val))
        self.current_node.next_node = Node()
        #print('current_node.next_node.val is now {}'.format(self.current_node.next_node.val))


        # while True:
        #     print('We are at index {}, value of {}'.format(i, self.current_node.val))
        #     if not self.current_node.next_node.next_node:
        #         print('\n---Break condition met---')
        #         print('We are at index {}, value of {}'.format(i, self.current_node.val))
        #         self.current_node.next_node = self.new_node
        #         print('current_node.next_node set to new_node')
        #         break
        #
        #     else:
        #         self.current_node = self.current_node.next_node
        #     i = i+1


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

        #initialise node_before and node_after
        self.node_before = None
        self.node_after = None

        # make new node
        self.new_node = Node()
        self.new_node.val = val
        self.new_node.next_node = Node()

        # start at head of list
        self.current_node = self.head

        # navigate to position prior to index in list
        for i in range(index):

            # if next_node doesn't exist exit function (as we're navigating to the node before the index we want to add at this is the right thing to do)
            if not self.current_node.next_node:
                return

            # store position of the node prior to index as node_before
            self.node_before = self.current_node.next_node

            # store position of index node as node_after
            self.node_after = self.current_node.next_node.next_node

            # exit loop

        # assign new_node.next_node to node_after
        self.new_node.next_node = self.node_after

        # reassign node_before.next_node to new_node
        self.node_before.next_node = self.new_node


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        # check if head of list has a value, exit function if not
        if not self.head.val:
            return
        # set current_node at head node
        current_node = self.head

        # start loop - navigate to position before index by setting current_node to next_node
        for i in range(index-1):
            # check if next_node exists, if not exit function
            if not current_node.next_node.val:
                return

            current_node = current_node.next_node
            #exit loop

        # store the node you want prior to the one to delete as node_before
        node_before = current_node

        #check if the node after the one you want to delete exists
        if not current_node.next_node.next_node.val:
            #assign value of the current_node's next node to None, end function
            node_before.next_node = None
            return

        # if node two places after exists store as node_after
        node_after = current_node.next_node.next_node
        #assign value of the current_node's next node to the one after the one you want to delete
        node_before.next_node = node_after


##################################################################################################
def check_output(function_call, expected, actual):
    if expected == actual:
        return
    else:
        if not actual:
            actual = None
        output = ('{}: {}!={}'.format(function_call, expected, actual))
        print(output)
        return output

#Your MyLinkedList object will be instantiated and called as such:
print()

obj = MyLinkedList()

actual_output = obj.get(0) # (Fakenode) -> None
expected_output = -1
check_output('obj.get(0)', expected_output, actual_output)
obj.print_whole_list()
print('(Fakenode) -> None\n')


#print('starts here')
obj.addAtHead(1) # 1 -> None
#print('added at head')
actual_output = obj.get(0) # (1) -> None
#print('set actual output')
expected_output = 1
#print('set expected output')
check_output('obj.addAtHead(1)', expected_output, actual_output)
#print('check_output function run')
obj.print_whole_list()
#print('print_whole_list has run')
print('1 -> None\n')
#print('ends here')

obj.addAtHead(2) # 2 -> 1 -> None
actual_output = obj.get(0) # (2) -> 1 -> None
expected_output = 2
check_output('obj.addAtHead(2)', expected_output, actual_output)
obj.print_whole_list()
print('2 -> 1 -> None\n')


obj.addAtHead(3) # 3 -> 2 -> 1 -> None
actual_output = obj.get(0) # (3) -> 2 -> 1 -> None
expected_output = 3
check_output('obj.addAtHead(3)', expected_output, actual_output)
obj.print_whole_list()
print('3 -> 2 -> 1 -> None\n')

actual_output = obj.get(1)  # 3 -> (2) -> 1 -> None
expected_output = 2
check_output('obj.get(1)', expected_output, actual_output)

actual_output = obj.get(2) # 3 -> 2 -> (1) -> None
expected_output = 1
check_output('obj.get(2)', expected_output, actual_output)

obj.addAtTail(10) # 3 -> 2 -> 1 -> 10 -> None
actual_output = obj.get(3) # 3 -> 2 -> 1 -> (10) -> None
expected_output = 10
check_output('obj.addAtTail(10)', expected_output, actual_output)
obj.print_whole_list()
print('3 -> 2 -> 1 -> 10 -> None\n')

obj.addAtTail(99) # 3 -> 2 -> 1 -> 10 -> None
actual_output = obj.get(4) # 3 -> 2 -> 1 -> (10) -> None
expected_output = 99
check_output('obj.addAtTail(99)', expected_output, actual_output)
obj.print_whole_list()
print('3 -> 2 -> 1 -> 10 -> 99 -> None\n')

obj.addAtIndex(2,15) # 3 -> 2 -> 15 -> 1 -> (10) -> None
actual_output = obj.get(2)
expected_output = 15
obj.print_whole_list()
print('3 -> 2 -> 15 -> 1 -> 10 -> 99 -> None\n')

obj.deleteAtIndex(1) # 3 -> 15 -> 1 -> 10 -> None
obj.print_whole_list()
print('3 -> 15 -> 1 -> 10 -> 99 -> None\n')


# numbers = MyLinkedList()
# numbers.addAtHead('two')
# numbers.addAtHead('one')
# numbers.addAtHead('zero')
# numbers.print_whole_list()
#
# print('\n---Adding Three to tail---')
# numbers.addAtTail('Three')
# numbers.print_whole_list()
#
#
# print('\n\n\n---Adding Four to tail---')
# numbers.addAtTail('Four')
# numbers.print_whole_list()


