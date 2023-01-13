from collections import deque
 
 
# A Linked List Node
class Node:
    def __init__(self, data, next, child):
        self.data = data
        self.next = next
        self.child = child
 
 
# Function to convert a multilevel linked list into a singly linked list
def convertList(head):
 
    curr = head
    q = deque()
 
    # process all nodes
    while curr:
 
        # last node is reached
        # dequeue the front node and set it as the next node of the current node
        if curr.next is None and len(q) > 0:
            curr.next = q.popleft()
 
        # if the current node has a child
        if curr.child:
            q.append(curr.child)
 
        # advance the current node
        curr = curr.next
 
    return head
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, '—> ', end='')
        ptr = ptr.next
    print('None')
 
 
# Helper function to create a linked list with elements of a given input
def createHorizontalList(input):
 
    head = None
    for i in reversed(range(len(input))):
        head = Node(input[i], head, None)
 
    return head
 
 
if __name__ == '__main__':
 
    # create a multilevel linked list
    head = createHorizontalList([1, 2, 3, 4, 5])
    head.child = createHorizontalList([6, 7])
    head.next.next.child = createHorizontalList([8, 9])
    head.child.next.child = createHorizontalList([10, 11])
    head.child.next.child.child = createHorizontalList([12])
 
    convertList(head)
    printList(head)