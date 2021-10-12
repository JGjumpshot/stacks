class Stack:
    def __init__(self):
        """Create new stack"""
        self._items = []

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)
    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()
    def top(self):
        return self._items[-1]
    def size(self):
        return len(self._items)
    # def clear(self):
