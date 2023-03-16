#  CS 3B Intermediate Software Design in Python
#  Lab # 4
#  Module: Abstract Data Types
#  Description: This class creates a custom-made Linked List containing
#               a linked list constructor and associated methods.
#  Development Env:  Windows 10
#  Version:  Python 3.11
#  Module filename:  aldosiswantoListNode.py
#  Date:  3/2/23
#


# Class Import
from aldosiswantoListNode import ListNode


class LinkedList:
    # Constants
    DEFAULT_HEAD_VALUE = None
    DEFAULT_ERROR_RETURN = None

    """
    Constructs a linked list object along with multiple helper methods
    @param item_value: item value to be inserted in the head, default = None
    """
    def __init__(self, item_value=None):
        if item_value:
            self.head = ListNode(item_value)
        else:
            self.head = LinkedList.DEFAULT_HEAD_VALUE

    """
    Finds the length of the linked list
    @return length: the length of the linked list
    """
    def length(self):
        current_node = self.head
        length = 0

        while current_node:
            length += 1
            current_node = current_node.nextNode

        return length

    """
    Appends an item onto the end of the list
    @param itemValue: the value of the item to be appended to the end of the 
                      list
    """
    def append(self, item_value):
        current_node = self.head

        if current_node:
            while current_node.nextNode:
                current_node = current_node.nextNode

            current_node.nextNode = ListNode(item_value)
        else:
            self.head = ListNode(item_value)

    """
    Get an item at a specified index position on the list
    @param index: the position in the list from which the desired value is 
                  held
    @return value: the value of the desired node
    """
    def get(self, index):
        if 0 < index <= self.length():
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.nextNode

            return current_node.nodeValue
        else:
            print("Invalid index. Index is larger than LinkedList length.")
            return LinkedList.DEFAULT_ERROR_RETURN

    """
    Set an item at a specified index position on the list
    @param index: the position in the list in which the desired value is
                  to be set
    @param item_value: the item value to be set in the specified 
                  index
    """
    def set(self, index, item_value):
        if 0 < index <= self.length():
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.nextNode

            current_node.nodeValue = item_value
        else:
            print("Invalid index. Index is larger than LinkedList length.")
            return LinkedList.DEFAULT_ERROR_RETURN
    """
    Check if linked list is empty
    @return empty: bool if list is empty
    """
    def is_empty(self):
        if self.length() == 0:
            return True
        else:
            return False

    """
    Insert an item at a specified index position on the list
    @param index: the position in the list in which the desired value is
                  to be inserted
    @param item_value: the item value to be inserted in the specified 
                  index
    """
    def insert(self, index, item_value):
        if (self.is_empty() and index == 1) or \
                ((not self.is_empty()) and 0 < index <= self.length()):
            previous_node = None
            current_node = self.head

            if index == 1:  # if node length = 1
                new_node = ListNode(item_value)
                new_node.nextNode = current_node
                self.head = new_node

            else:  # if node length > 1
                for i in range(index-1):
                    previous_node = current_node
                    current_node = current_node.nextNode

                new_node = ListNode(item_value)
                previous_node.nextNode = new_node
                new_node.nextNode = current_node

        else:
            print("Invalid index.")
            return LinkedList.DEFAULT_ERROR_RETURN

    """
    Delete an item at a specified index position on the list
    @param index: the position in the list in which the item is
                  to be deleted
    """
    def delete(self, index):
        if self.is_empty() or \
                ((not self.is_empty()) and 0 < index <= self.length()):
            previous_node = self.head
            current_node = self.head

            if index == 1:  # if node length = 1
                self.head = current_node.nextNode

            else:  # if node length > 1
                for i in range(index - 1):
                    previous_node = current_node
                    current_node = current_node.nextNode

                previous_node.nextNode = current_node.nextNode

        else:
            print("Invalid index.")
            return LinkedList.DEFAULT_ERROR_RETURN

    """
    Return and remove the last item from the list
    @return itemValue: the item value of the last item
    """
    def pop(self):
        previous_node = None
        current_node = self.head

        if current_node:
            if self.length() == 1:  # if node length = 1
                self.head = None
                return current_node.nodeValue

            else:  # if node length > 1
                while current_node.nextNode:
                    previous_node = current_node
                    current_node = current_node.nextNode

                previous_node.nextNode = None
                return current_node.nodeValue

        else:  # if node length is 0
            print("Node is empty. Cannot pop.")
            return LinkedList.DEFAULT_ERROR_RETURN


class LinkedListIterator:
    """
    Constructs an iterator object for the LinkedList object
    @param linked_list_object: the linked list object to be iterated
    """
    def __init__(self, linked_list_object):
        self.ll = linked_list_object

    """
    Iterator property for the LinkedList object
    @return iterator_object: the iterator object
    """
    def __iter__(self):
        self.current = self.ll.head
        return self

    """
    Next property of the iterator
    @return current_value: the next value in the iterator
    """
    def __next__(self):
        if self.current:
            current_value = self.current.nodeValue
            self.current = self.current.nextNode
            return current_value
        else:
            raise StopIteration
