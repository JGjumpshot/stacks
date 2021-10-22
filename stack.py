"""stack module"""
class Stack:
    """stack class"""
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
        """see top of the stack"""
        return self._items[-1]
    def size(self):
        """return size of the stack"""
        return len(self._items)
    def clear(self):
        """clear the stack"""
        return self._items.clear()
    def is_empty(self):
        """check if the stack is empty"""
        if len(self._items) == 0:
            return True
        # return False
    def __str__(self):
        """return string function"""
        return str(self._items)
# print(my_stack)
# print(dir(my_stack))
