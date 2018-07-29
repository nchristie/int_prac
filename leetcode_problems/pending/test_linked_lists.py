from Design_Linked_List import MyLinkedList

##################################################################################################
obj = MyLinkedList()
functions = 0
args = 0

# for i in range(len(functions)):
#     print('obj.{}({})'.format(functions[i], str(args[i]).replace('[','').replace(']','')))
################################################################################
def test_something():
    obj=MyLinkedList()
    obj.addAtHead(7)
    assert obj.return_whole_list() == [7]
    obj.addAtHead(2)
    assert obj.return_whole_list() == [2, 7]
    obj.addAtHead(1)
    assert obj.return_whole_list() == [1, 2, 7]
    obj.addAtIndex(3, 0)
    assert obj.return_whole_list() == [1, 2, 7, 0]
    obj.deleteAtIndex(2)
    assert obj.return_whole_list() == [1, 2, 0]
    obj.addAtHead(6)
    assert obj.return_whole_list() == [6, 1, 2, 0]
    obj.addAtTail(4)
    assert obj.return_whole_list() == [6, 1, 2, 0, 4]
    assert obj.get(4) == 4
    obj.addAtHead(4)
    assert obj.return_whole_list() == [4, 6, 1, 2, 0, 4]
    obj.addAtIndex(5, 0)
    assert obj.return_whole_list() == [4, 6, 1, 2, 0, 0, 4]
    obj.addAtHead(6)
    assert obj.return_whole_list() == [6, 4, 6, 1, 2, 0, 0, 4]

def test_first_test_from_leet():
    obj = MyLinkedList()
    obj.addAtHead(8)
    assert obj.return_whole_list() == [8]
    assert obj.get(1) == -1
    obj.addAtTail(81)
    assert obj.return_whole_list() == [8, 81]
    assert obj.deleteAtIndex(2) == None
    assert obj.return_whole_list() == [8, 81]
    obj.addAtHead(26)
    assert obj.return_whole_list() == [26, 8, 81]
    obj.deleteAtIndex(2)
    assert obj.return_whole_list() == [26, 8]
    assert obj.get(1) == 8
    obj.addAtTail(24)
    # assert obj.return_whole_list() == [26, 8, 24]
    # obj.addAtHead(15)
    # assert obj.return_whole_list() == [15, 26, 8, 24]
    # obj.addAtTail(0)
    # assert obj.return_whole_list() == [15, 26, 8, 24, 0]
    # obj.addAtTail(13)
    # assert obj.return_whole_list() == [15, 26, 8, 24, 0, 13]
    # obj.addAtTail(1)
    # assert obj.return_whole_list() == [15, 26, 8, 24, 0, 13, 1]
    # obj.addAtIndex(6, 33)
    # assert obj.return_whole_list() == [15, 26, 8, 24, 0, 13, 33, 1]
    # assert obj.get(6) == 33
    # obj.addAtIndex(2, 91)
    # assert obj.return_whole_list() == [15, 26, 91, 8, 24, 0, 13, 33, 1]
    # obj.addAtHead(82)
    # assert obj.return_whole_list() == [82, 15, 26, 91, 8, 24, 0, 13, 33, 1]
    # obj.deleteAtIndex(6)
    # assert obj.return_whole_list() == [82, 15, 26, 91, 8, 24, 13, 33, 1]
    # obj.addAtIndex(4, 11)
    # assert obj.return_whole_list() == [82, 15, 26, 91, 11, 8, 24, 13, 33, 1]
    # obj.addAtHead(3)
    # assert obj.return_whole_list() == [3, 82, 15, 26, 91, 11, 8, 24, 13, 33, 1]
    # obj.addAtIndex(7, 14)
    # assert obj.return_whole_list() == [3, 82, 15, 26, 91, 11, 8, 14, 24, 13, 33, 1]
    # obj.deleteAtIndex(1)
    # assert obj.return_whole_list() == [3, 15, 26, 91, 11, 8, 14, 24, 13, 33, 1]
    # assert obj.get(6) == 14
    # obj.addAtTail(99)
    # assert obj.return_whole_list() == [3, 15, 26, 91, 11, 8, 14, 24, 13, 33, 1, 99]
    # obj.deleteAtIndex(11)
    # assert obj.return_whole_list() == [3, 15, 26, 91, 11, 8, 14, 24, 13, 33, 1]
    # obj.deleteAtIndex(7)
    # assert obj.return_whole_list() == [3, 15, 26, 91, 11, 8, 14, 13, 33, 1]
    # obj.addAtTail(5)
    # assert obj.return_whole_list() == [3, 15, 26, 91, 11, 8, 14, 13, 33, 1, 5]
    # obj.addAtTail(92)
    # assert obj.return_whole_list() == [3, 15, 26, 91, 11, 8, 14, 13, 33, 1, 5, 92]
    # obj.addAtIndex(7, 92)
    # assert obj.return_whole_list() == [3, 15, 26, 91, 11, 8, 14, 92, 13, 33, 1, 5, 92]
    # obj.addAtHead(57)
    # assert obj.return_whole_list() == [57, 3, 15, 26, 91, 11, 8, 14, 92, 13, 33, 1, 5, 92]
    # assert obj.get(2) == 15
    # assert obj.get(6) == 8
    # obj.addAtTail(39)
    # assert obj.return_whole_list() == [57, 3, 15, 26, 91, 11, 8, 14, 92, 13, 33, 1, 5, 92, 39]
    # obj.addAtTail(51)
    # assert obj.return_whole_list() == [57, 3, 15, 26, 91, 11, 8, 14, 92, 13, 33, 1, 5, 92, 39, 51]
    # obj.addAtTail(3)
    # assert obj.return_whole_list() == [57, 3, 15, 26, 91, 11, 8, 14, 92, 13, 33, 1, 5, 92, 39, 51, 3]
    # obj.addAtTail(22)
    # assert obj.return_whole_list() == [57, 3, 15, 26, 91, 11, 8, 14, 92, 13, 33, 1, 5, 92, 39, 3, 22]
    # obj.addAtIndex(5, 26)
    # assert obj.return_whole_list() == [57, 3, 15, 26, 91, 26, 11, 8, 14, 92, 13, 33, 1, 5, 92, 39, 3, 22]
    # obj.addAtIndex(9, 52)
    # assert obj.return_whole_list() == [57, 3, 15, 26, 91, 26, 11, 8, 14, 52, 92, 13, 33, 1, 5, 92, 39, 3, 22]
    # obj.addAtHead(69)
    # assert obj.return_whole_list() == [69, 57, 3, 15, 26, 91, 26, 11, 8, 14, 52, 92, 13, 33, 1, 5, 92, 39, 3, 22]
    # obj.addAtIndex(5, 58)
    # assert obj.return_whole_list() == [69, 57, 3, 15, 26, 58, 91, 26, 11, 8, 14, 52, 92, 13, 33, 1, 5, 92, 39, 3, 22]
    # obj.addAtTail(79)
    # assert obj.return_whole_list() == [69, 57, 3, 15, 26, 58, 91, 26, 11, 8, 14, 52, 92, 13, 33, 1, 5, 92, 39, 3, 22, 79]
    # obj.addAtHead(7)
    # assert obj.return_whole_list() == [7, 69, 57, 3, 15, 26, 58, 91, 26, 11, 8, 14, 52, 92, 13, 33, 1, 5, 92, 39, 3, 22, 79]
    # obj.addAtHead(41)
    # assert obj.return_whole_list() == [41, 7, 69, 57, 3, 15, 26, 58, 91, 26, 11, 8, 14, 52, 92, 13, 33, 1, 5, 92, 39, 3, 22, 79]
    # obj.addAtHead(33)
    # assert obj.return_whole_list() == [33, 41, 7, 69, 57, 3, 15, 26, 58, 91, 26, 11, 8, 14, 52, 92, 13, 33, 1, 5, 92, 39, 3, 22, 79]
    # obj.addAtHead(88)
    # assert obj.return_whole_list() == [88, 33, 41, 7, 69, 57, 3, 15, 26, 58, 91, 26, 11, 8, 14, 52, 92, 13, 33, 1, 5, 92, 39, 3, 22, 79]
    # obj.addAtHead(44)
    # obj.addAtHead(8)
    # obj.addAtTail(72)
    # obj.addAtHead(93)
    # obj.deleteAtIndex(18)
    # obj.addAtHead(1)
    # obj.get(9)
    # obj.addAtHead(46)
    # obj.get(9)
    # obj.addAtHead(92)
    # obj.addAtHead(71)
    # obj.addAtHead(69)
    # obj.addAtIndex(11, 54)
    # obj.deleteAtIndex(27)
    # obj.addAtTail(83)
    # obj.deleteAtIndex(12)
    # obj.get(20)
    # obj.addAtIndex(19, 97)
    # obj.addAtHead(77)
    # obj.addAtTail(36)
    # obj.deleteAtIndex(3)
    # obj.addAtHead(35)
    # obj.addAtIndex(16, 68)
    # obj.deleteAtIndex(22)
    # obj.deleteAtIndex(36)
    # obj.deleteAtIndex(17)
    # obj.addAtHead(62)
    # obj.addAtTail(89)
    # obj.addAtTail(61)
    # obj.addAtHead(6)
    # obj.addAtTail(92)
    # obj.addAtIndex(28, 69)
    # obj.deleteAtIndex(23)
    # obj.deleteAtIndex(28)
    # obj.addAtIndex(7, 4)
    # obj.addAtHead(0)
    # obj.addAtHead(24)
    # obj.addAtTail(52)
    # obj.get(1)
    # obj.addAtIndex(23, 3)
    # obj.get(7)
    # obj.addAtHead(6)
    # obj.addAtHead(68)
    # obj.addAtHead(79)
    # obj.addAtIndex(45, 90)
    # obj.addAtIndex(41, 52)
    # obj.get(28)
    # obj.addAtHead(25)
    # obj.get(9)
    # obj.get(32)
    # obj.addAtTail(11)
    # obj.addAtHead(90)
    # obj.addAtHead(24)
    # obj.addAtTail(98)
    # obj.addAtTail(36)
    # obj.get(34)
    # obj.addAtTail(26)


def test_get_function1():
    obj = MyLinkedList()
    assert obj.get(0) == -1
    obj.addAtIndex(1,2)
    assert obj.get(0) == -1
    assert obj.get(1) == -1
    obj.addAtIndex(0, 1)
    assert obj.get(0) == 1
    assert obj.get(1) == -1

def test_add_at_head_and_tail():
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    assert obj.get(1) == 2
    obj.deleteAtIndex(1)
    assert obj.get(1) == 3


