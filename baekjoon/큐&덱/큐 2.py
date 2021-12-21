class Queue:
    def __init__(self):
        self.data = deque([])

    def push(self, X):
        return self.data.append(X)

    def size(self):
        return len(self.data)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.data.popleft()

    def front(self):
        if self.empty():
            return -1
        else:
            return self.data[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.data[-1]

def execute(string):
    inst = string.split(' ')
    if inst[0] == "push":
        queue.push(inst[1])
    elif inst[0] == "pop":
        print(queue.pop())
    elif inst[0] == "size":
        print(queue.size())
    elif inst[0] == "empty":
        print(queue.empty())
    elif inst[0] == "front":
        print(queue.front())
    elif inst[0] == "back":
        print(queue.back())
    else:
        print("Error: undefined instruction")

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import deque
    num_of_instructions = int(readline().strip())
    queue = Queue()
    for _ in range(num_of_instructions):
        execute(readline().strip())