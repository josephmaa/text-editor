"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  Joseph Maa
"""
# NOTE:  You'll probably want to start with insertAfter

from .node2way import Node2Way


class CursorBasedList(object):
    """ Linked implementation of a positional list."""

    def __init__(self):
        """ Creates an empty cursor-based list with header and trailer nodes."""
        self._header = Node2Way(None)
        self._trailer = Node2Way(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        """ Returns True if the current item has a next item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        """ Returns True if the current item has a previous item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no previous item")
        return self._current.getPrevious() != self._header

    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no first item")
        # point current to first "real" data node past the header
        self._current = self._header.getNext()

    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no last item")
        self._current = self._trailer.getPrevious()

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item is has moved to the right one item"""
        if not self.hasNext():
            raise AttributeError("No next node in the list")
        # point current to the next node in the linked list
        self._current = self._current.getNext()

    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one item"""
        if not self.hasPrevious():
            raise AttributeError("No previous node in the list")
        self._current = self._current.getPrevious()

    def insertAfter(self, item: int):
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        temp = Node2Way(item)
        if self._current:
            # Hold reference to next node
            next: Node2Way = self._current.getNext()
            self._current.setNext(temp)
            next.setPrevious(temp)
            temp.setNext(next)
            temp.setPrevious(self._current)
        else:  # list is empty
            self._header.setNext(temp)
            self._trailer.setPrevious(temp)
            temp.setNext(self._trailer)
            temp.setPrevious(self._header)
        self._current = temp
        self._size += 1

    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        temp = Node2Way(item)
        if self._current:
            # Hold reference to next node
            prev: Node2Way = self._current.getPrevious()
            self._current.setPrevious(temp)
            prev.setNext(temp)
            temp.setPrevious(prev)
            temp.setNext(self._current)
        else:  # list is empty
            self._header.setNext(temp)
            self._trailer.setPrevious(temp)
            temp.setNext(self._trailer)
            temp.setPrevious(self._header)
        self._current = temp
        self._size += 1

    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        if self.isEmpty():
            raise AttributeError("Empty list has no current item")
        # returns the data in the current node
        return self._current.getData()

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list cannot remove current item")
        node = self._current
        prev = self._current.getPrevious()
        next = self._current.getNext()
        prev.setNext(next)
        next.setPrevious(prev)
        if self.hasNext():
            self._current = next
        else:
            self._current = self._trailer.getPrevious()
        self._size -= 1
        return node.getData()

    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list cannot remove current item")
        self._current.setData(newItemValue)

    def isEmpty(self):
        """ Returns True if the list is empty; otherwise it return False"""
        if self._size == 0:
            return True
        else:
            return False

    def __len__(self):
        """ Returns the number of items in the list."""
        return self._size

    def __str__(self):
        """Includes items from first through last."""
        resultStr = ""
        temp = self._header.getNext()
        while temp != self._trailer:
            resultStr += str(temp.getData())
            temp = temp.getNext()
        return resultStr


def main():
    lst = CursorBasedList()
    node = Node2Way(5)
    lst.insertAfter(5)
    print(lst)


if __name__ == "__main__":
    main()
