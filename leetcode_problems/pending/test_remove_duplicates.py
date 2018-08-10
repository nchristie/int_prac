import unittest
from remove_duplicates_from_sorted_list import *

class TestMyTests(unittest.TestCase):

    def test_make_a_list(self):
        #given
        root_node = ListNode(1)

        #when
        x = root_node.val
        
        #then
        self.assertEqual(x, 1)


    def test_make_a_list_with_more_things(self):
        #given
        root_node = ListNode(1)
        current_node = root_node

        for i in range(2, 10):
            current_node.next = ListNode(i)
            current_node = current_node.next

        #when
        x = root_node.val
        y = root_node.next.val
        z = root_node.next.next.val
        
        #then
        self.assertEqual([x, y, z], [1, 2, 3])

    def test_traverse_tree_print(self):
        #given
        my_list = ListNode(None)
##        solution = Solution()
        current_node = my_list

        for i in range(1, 11):
            current_node.next = ListNode(i)
            current_node = current_node.next
        
        #when
        solution = Solution()
        x = solution.traverse_tree(my_list,'', '')

        #then
        self.assertEqual(x, None)


    def test_nodes(self):
        #given
        my_list_head = ListNode(1)
        x = type(my_list_head)

        #then
        self.assertEqual(x, ListNode)

    def test_add_node(self):
        #given

        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in range(5):
            solution.add_node(current_node, i)
            current_node = current_node.next

        def append_val(node):
            new_node_list.append(node.val)
            
        new_node_list = []
        solution.traverse_tree(my_list, bool, append_val)
        
        #then
        self.assertEqual(new_node_list,  [None, 0, 1, 2, 3, 4])

    def test_delete_node(self):
        #given

        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in range(5):
            solution.add_node(current_node, i)
            current_node = current_node.next

        #when

        solution.delete_next_node(my_list)

        def append_val(node):
            new_node_list.append(node.val)
            
        new_node_list = []
        solution.traverse_tree(my_list, bool, append_val)
        
        #then
        self.assertEqual(new_node_list,  [None, 1, 2, 3, 4])
 
    def test_make_check_list(self):
        #given
        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in [1, 2, 3, 4, 5, 4, 6, 4, 7]:
            solution.add_node(current_node, i)
            current_node = current_node.next

        #when
        check_list = solution.make_check_list(my_list)

        #then
        self.assertEqual(check_list, [None, 1, 2, 3, 4, 5, 4, 6, 4, 7])

    def test_find_duplicates(self):
        #given
        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in [1, 2, 3, 4, 5, 4, 6, 4, 7]:
            solution.add_node(current_node, i)
            current_node = current_node.next

        #when
        duplicates = solution.find_duplicates(my_list)

        #then
        self.assertEqual(duplicates,set([4]))

    def test_find_duplicates1(self):
        #given
        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in [1, 1, 3, 4, 5, 4, 6, 4, 7]:
            solution.add_node(current_node, i)
            current_node = current_node.next

        #when
        duplicates = solution.find_duplicates(my_list)

        #then
        self.assertEqual(duplicates,set([1, 4]))

    def test_find_duplicates2(self):
        #given
        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in [1, 1, 3, 4, 5, 5, 5, 4, 6, 4, 7]:
            solution.add_node(current_node, i)
            current_node = current_node.next

        #when
        duplicates = solution.find_duplicates(my_list)

        #then
        self.assertEqual(duplicates, set([1, 4, 5]))


    def test_deleteDuplicates(self):
        #given
        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in [1, 2, 3, 4, 5, 4, 6, 4, 7]:
            solution.add_node(current_node, i)
            current_node = current_node.next
        #when
        de_duped_list = solution.deleteDuplicates(my_list)
        end_list = solution.make_check_list(de_duped_list)
        
        #then
        self.assertEqual(end_list, [None, 1, 2, 3, 5, 6, 7] )

    def test_deleteDuplicates1(self):
        #given
        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in [1, 2, 2, 3, 4]:
            solution.add_node(current_node, i)
            current_node = current_node.next
        #when
        de_duped_list = solution.deleteDuplicates(my_list)
        end_list = solution.make_check_list(de_duped_list)
        
        #then
        self.assertEqual(end_list, [None, 1, 3, 4] )

    def test_deleteDuplicates2(self):
        #given
        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in [1, 2, 2, 2, 3, 4, 2, 5, 2]:
            solution.add_node(current_node, i)
            current_node = current_node.next
        #when
        de_duped_list = solution.deleteDuplicates(my_list)
        end_list = solution.make_check_list(de_duped_list)
        
        #then
        self.assertEqual(end_list, [None, 1, 3, 4, 5] )

    def test_deleteDuplicates3(self):
        #given
        my_list = ListNode(None)
        current_node = my_list
        solution = Solution()
        
        for i in [1, 2, 2, 2, 2, 3, 4, 2, 5, 2]:
            solution.add_node(current_node, i)
            current_node = current_node.next
        #when
        de_duped_list = solution.deleteDuplicates(my_list)
        end_list = solution.make_check_list(de_duped_list)
        
        #then
        self.assertEqual(end_list, [None, 1, 3, 4, 5] )
        
if __name__ == '__main__':
    unittest.main()

