class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy!")
        else:
            self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống!")
            return None
        else:
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity

    def count(self):
        return len(self.stack)

    def print_stack(self):
        if self.isEmpty():
            print("Ngăn xếp trống!")
        else:
            print("Nội dung ngăn xếp:", self.stack)
