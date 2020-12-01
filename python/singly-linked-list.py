class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next:
            current_node = current_node.next
            total += 1

        return total

    def __repr__(self):
        items = []
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            items.append(current_node.data)

        return items

    def get(self, index=None, data=None):
        if index:
            if index >= self.length():
                return None
        elif not data:
            return None

        current_node, current_idx = self.head, 0
        while current_node.next:
            current_node = current_node.next
            if current_idx == index or current_node.data == data:
                return current_node.data
            else:
                current_idx += 1

    def append(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        new_node = Node(data)
        current_node.next = new_node

    def delete(self, index=None, data=None):
        if index:
            if index >= self.length():
                return None
        elif not data and not index:
            return None

        current_node, current_idx = self.head, 0
        while current_node.next:
            current_node = current_node.next
            if current_idx == index or current_node.data == data:
                current_node.next = None
                return None
            else:
                current_idx += 1
