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

        if not self.head.val:
            self.head.val = val
        else:
            new_node = Node()
            new_node.val = val

            current_node = self.head

            while current_node.next_node.val:
                current_node = current_node.next_node

            current_node.next_node = new_node


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
        node_before = None
        node_after = None

        # make new node
        new_node = Node()
        new_node.val = val

        # start at head of list
        current_node = self.head

        # navigate to position prior to index in list

        for i in range(index-1):

            # if next_node doesn't exist exit function (as we're navigating to the node before the index we want to add at this is the right thing to do)
            if not current_node.next_node:
                return

            # store position of the node prior to index as node_before
            node_before = current_node

            # store position of index node as node_after
            node_after = current_node.next_node

            # exit loop

        # assign new_node.next_node to node_after
        new_node.next_node = node_after

        # reassign node_before.next_node to new_node
        node_before.next_node = new_node

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


def check_output(function_call, expected, actual):
    if expected == actual:
        pass
    else:
        print '{}: {}!={}'.format(function_call, expected, actual)

#Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

head = obj.get(0) # (Fakenode) -> None
expected_output = None

#expected output = None

obj.addAtHead(1) # 1 -> None
head = obj.get(0) # (1) -> None
print('obj.addAtHead(1)\n head = obj.get(0)\n expected output = {}, real output = {}\n'.format(1,head))
#expected output = 1

obj.addAtHead(2) # 2 -> 1 -> None
head = obj.get(0) # (2) -> 1 -> None
print('obj.addAtHead(2)\n head = obj.get(0)\n expected output = {}, real output = {}\n'.format(2,head))

obj.addAtHead(3) # 3 -> 2 -> 1 -> None
head = obj.get(0) # (3) -> 2 -> 1 -> None
print('obj.addAtHead(3)\n head = obj.get(0)\n expected output = {}, real output = {}\n'.format(3,head))

second_element = obj.get(1)  # 3 -> (2) -> 1 -> None
print('second_element = obj.get(1)\n expected output = {}, real output = {}\n'.format(2,head))

third_element = obj.get(2) # 3 -> 2 -> (1) -> None
print('third_element = obj.get(2)\n expected output = {}, real output = {}\n'.format(1,head))

obj.addAtTail(10) # 3 -> 2 -> 1 -> 10 -> None
tail = obj.get(3) # 3 -> 2 -> 1 -> (10) -> None
print('obj.addAtTail(10)\n tail = obj.get(3)\n expected output = {}, real output = {}\n'.format(10,tail))
##obj.addAtIndex(1,2)
##obj.deleteAtIndex(1)


