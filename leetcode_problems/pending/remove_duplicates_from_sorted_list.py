'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.duplicates = self.find_duplicates(head)
        node = head
        
        while type(node.next) == ListNode:
            while node.next.val == node.next.next.val:
                self.delete_next_node(node)
            node = node.next
            
        self.traverse_tree(head, condition = self.is_duplicated, operation = self.delete_next_node)

        return head

    def traverse_tree(self, node, condition=True==True, operation=None):
        """Travses tree and performs an operation on each node. If no operation
        given prints the value of each node"""

        if type(node) != ListNode:
            print('traverse function end')
            return
        else:
            if not operation:
                print(node.val)
            elif condition(node):
                operation(node)
            self.traverse_tree(node.next, condition, operation)

    def find_duplicates(self, node):
        duplicates=[]
        check_list = self.make_check_list(node)
        i = 0
        for i in range(len(check_list)):
            if check_list[i] in check_list[:i]:
                duplicates.append(check_list[i])
        return set(duplicates)
        

    def make_check_list(self, node):
        def append_val(node):
            new_node_list.append(node.val)
            
        new_node_list = []
        self.traverse_tree(node, bool, append_val)
        return new_node_list

    def add_node(self, node, val):
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node
         
    def is_duplicated(self, node):
        if type(node.next) == ListNode:
            return node.next.val in self.duplicates
        
    def delete_next_node(self, node):
        node.next = node.next.next
