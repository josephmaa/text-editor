from node2way import Node2Way
import unittest

from cursor_based_list import CursorBasedList
from node2way import Node2Way


class testCursorBasedList(unittest.TestCase):
    def simpleTestList():
        lst = CursorBasedList()
        node = Node2Way(5)
        lst.insertAfter(5)
        print(lst)
        return lst

if __name__ == "__main__":
    unittest.main()
