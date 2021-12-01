class Stack:
    def __init__(self):
        self.data = []

    def push(self, X):
        return self.data.append(X)

    def size(self):
        return len(self.data)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.data[-1]

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.data.pop()

def execute(string):
    inst = string.split(' ')

    if inst[0] == "push":
        stack.push(inst[1])
    elif inst[0] == "top":
        print(stack.top())
    elif inst[0] == "size":
        print(stack.size())
    elif inst[0] == "empty":
        print(stack.empty())
    else: # pop
        print(stack.pop())


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_instructions = int(readline().strip())
    stack = Stack()
    for _ in range(num_of_instructions):
        execute(readline().strip())
