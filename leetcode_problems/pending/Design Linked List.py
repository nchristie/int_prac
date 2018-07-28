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
        self.next_val = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.next_val = None
        self.val = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is
        invalid, return -1.
        :type index: int
        :rtype: int
        """
        self.sought_index = self.head
        for i in range(index):
            self.sought_index = self.next_val
        return self.sought_index
            
            

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked
        list.
        :type val: int
        :rtype: void
        """
        new_node = Node()
        new_node.val = val
        new_node.next_val = self.head
        self.head = new_node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        new_node = Node()
        new_node.val = val

        find_tail = self.head
        
        while find_tail.val:
            find_tail = find_tail.next_val

        find_tail.next_val = new_node
            

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        pass

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        pass

#Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

head = obj.get(0)
print 'expected output = {}, real output = {}'.format(None,head.val)
#expected output = None

obj.addAtHead(1)
head = obj.get(0)
print 'expected output = {}, real output = {}'.format(1,head.val)
#expected output = 1

obj.addAtTail(3)
tail = obj.get(1)
print 'expected output = {}, real output = {}'.format(3,tail.val)
##obj.addAtIndex(1,2)
##obj.deleteAtIndex(1)



       
