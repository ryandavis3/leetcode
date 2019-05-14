class ListNode:
    """
    Class for node in linked list.
    """
    def __init__(self, x):
         self.val = x
         self.next = None

def integerAsLinkedList(val : int):
    """
    Represent integer as a linked list.
    """
    digits = [int(digit) for digit in str(val)]
    l = ListNode(digits[-1])
    l0 = l
    for digit in reversed(digits[:-1]):
        l.next = ListNode(digit)
        l = l.next
    return l0

def printLinkedListAsInt(l : ListNode):
    """
    Print linked list as single integer.
    """
    digits = list()
    while l is not None:
        digits.append(l.val)
        l = l.next
    digits = reversed(digits)
    digits = [str(d) for d in digits]
    digits = "".join(digits)
    print(int(digits))

def getVal(l : ListNode):
    """
    Get value from node. Return zero if None passed as argument.
    """
    if l is None:
        return 0
    return l.val

def nextDigit(l : ListNode):
    """
    Go to the next digit in the linked list representation
    of the integer. If None, return None.
    """
    if l is None:
        return None
    return l.next

def newDigit(lcurr : ListNode, val : int):
    """
    Add new digit to integer and update tail of linked list.
    """
    node = ListNode(val)
    lcurr.next = node
    lcurr = node
    return lcurr

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Add two numbers together. 
        """
        carry = 0
        l3 = None
        # Iterate over digits in reverse order
        while l1 is not None or l2 is not None:
            # Get digit in each integer
            v1 = getVal(l1)
            v2 = getVal(l2)
            # Get digit in summed value
            vsum = v1 + v2 + carry
            digit = vsum % 10
            # Get carry over value for next digit
            carry = int(vsum >= 10)
            if l3 is None:
                l3 = ListNode(digit)
                lcurr = l3
            else:
                lcurr = newDigit(lcurr, digit)
            # Go to next digit
            l1 = nextDigit(l1)
            l2 = nextDigit(l2)
        if carry:
            lcurr = newDigit(lcurr, carry)
        return l3
