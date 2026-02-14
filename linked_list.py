
class Node:
   
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    LinkedList class that stores the head node and supports insertion plus
    recursive sum, search, and in-place reverse.
    """

    def __init__(self):
        # tests expect this attribute to exist
        self.head = None

    # O(1)
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # O(n)
    def insert_at_end(self, data):
        new_node = Node(data)

        # empty list
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # ---------- RECURSION: SUM ----------
    def recursive_sum(self):
        return self._recursive_sum(self.head)

    def _recursive_sum(self, node):
        if node is None:
            return 0
        return node.data + self._recursive_sum(node.next)

    # ---------- RECURSION: SEARCH ----------
    def recursive_search(self, target):
        return self._recursive_search(self.head, target)

    def _recursive_search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._recursive_search(node.next, target)

    # ---------- RECURSION: REVERSE (IN PLACE) ----------
    def recursive_reverse(self):
        self.head = self._recursive_reverse(self.head)

    def _recursive_reverse(self, node):
        # empty list or single node
        if node is None or node.next is None:
            return node

        new_head = self._recursive_reverse(node.next)

        node.next.next = node
        node.next = None

        return new_head
