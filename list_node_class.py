#  CS 3B Intermediate Software Design in Python
#  Lab # 4
#  Module: Abstract Data Types
#  Description: This class creates a class describing the list node
#               properties. To be used as a helper class to the linked
#               list class.
#  Development Env:  Windows 10
#  Version:  Python 3.11
#  Module filename:  aldosiswantoListNode.py
#  Date:  3/2/23
#

class ListNode:
    # Constants
    DEFAULT_NODE_VALUE = None
    DEFAULT_NEXT_NODE = None
    """
    Constructs a ListNode object containing a nodeValue and nextNode
    @param inputNodeValue: Value to be inserted into the node
    """
    def __init__(self, input_node_value):
        self.nodeValue = input_node_value
        self.nextNode = ListNode.DEFAULT_NEXT_NODE
