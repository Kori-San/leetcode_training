# https://leetcode.com/problems/add-two-numbers/

# It creates a class called ListNode that has a value and a pointer to the next node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        """
        A constructor for the linked list.
        
        Args:
          val: the value of the node. Defaults to 0
          next: the next node in the linked list
        """
        self.val = val
        self.next = next

class Solution(object): 
    def addTwoNumbers(self, l1, l2):
        """
        Given two non-empty linked lists representing two non-negative integers, the digits are stored in
        reverse order and each of their nodes contain a single digit, add the two numbers and return it as a
        linked list
        
        Args:
          l1: ListNode
          l2: ListNode

        Returns:
          The return value is a ListNode.
        """
        # It's converting the linked list into a number.
        num = listNode_to_num(l1) + listNode_to_num(l2)

        # It's creating a new node.
        node = ListNode()
        
        # It's converting the number into a linked list.
        for digit in str(num)[::-1]:
            listNode_push(node, int(digit)) 

        # Push node.next to avoid displaying the default 0 when creating a ListNode
        return node.next

def listNode_push(node, digit):
    """
    While the next node exists, keep moving to the next node. When the next node doesn't exist, create a
    new node and set it as the next node.
    
    Args:
      node: the node to which we want to add a new node
      digit: the digit to be added to the end of the list
    """
    # It's moving to the next node.
    while node.next:
        node = node.next
 
    # It's creating a new node and setting it as the next node.
    node.next = ListNode(digit)

def listNode_to_num(node):
    """
    It converts a linked list into a number
    
    Args:
      node: the node that we're currently on
    
    Returns:
      A number
    """
    # It's creating two variables called index and number and setting them to 0.
    index = 0
    number = 0

    # It's creating an infinite loop.
    while True:
        # It's converting the linked list into a number.
        number += node.val * 10 ** index
        index += 1

        # It's checking if the next node exists. If it does, it moves to the next node. If it doesn't, it
        # breaks out of the loop.
        if node.next:
            node = node.next
        else:
            break
        
    return number
