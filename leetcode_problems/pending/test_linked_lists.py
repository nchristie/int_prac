from Design_Linked_List import *
import unittest


def test_get():
    #GIVEN
    obj = MyLinkedList()

    #WHEN
    text = obj.get(0)

    #THEN
    assertEqual(text, None)