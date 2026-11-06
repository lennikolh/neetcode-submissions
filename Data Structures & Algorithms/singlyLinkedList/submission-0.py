class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        # Dummy-Node initialisieren
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        # CRITICAL FIX: Wenn die Liste vorher leer war, zeigt tail jetzt auch auf new_node!
        if self.tail == self.head:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        
        # Bis zum Knoten VOR dem Ziel-Index wandern
        while i < index and curr.next:
            curr = curr.next
            i += 1
        
        # Wenn ein Element an 'index' existiert
        if curr.next:
            # CRITICAL FIX: Wenn wir das letzte Element löschen, tail zurücksetzen
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
            
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res