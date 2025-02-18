class Stack:
    def __init__(self, iterable=[]):
        self.__stack = iterable

    def __repr__(self):
        return f"Stack({self.__stack})"

    def __str__(self):
        return "\n".join(["|" + str(i) + "|" for i in reversed(self.__stack)] + ["---"])

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()
        return None

    def top(self):
        if not self.isEmpty():
            return self.__stack[-1]
        return None

    def is_empty(self):
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)


stack = Stack()
stack.push(1)
stack.push(2)
print(stack)
print(stack.pop())
print(stack.is_empty())
print(stack.size())
"""출력
2
False
1
"""
