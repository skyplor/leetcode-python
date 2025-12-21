class MyQueue:

    array_one = []
    array_two = []
    def __init__(self):
        self.array_one = []
        self.array_two = []

    def push(self, x: int) -> None:
        self.array_one.append(x)

    def pop(self) -> int:
        if self.array_two:
            return self.array_two.pop()
        while self.array_one:
            self.array_two.append(self.array_one.pop())
        return self.array_two.pop()

    def peek(self) -> int:
        if self.array_two:
            return self.array_two[-1]
        while self.array_one:
            self.array_two.append(self.array_one.pop())
        return self.array_two[-1]

    def empty(self) -> bool:
        return len(self.array_two) == 0 and len(self.array_one) == 0