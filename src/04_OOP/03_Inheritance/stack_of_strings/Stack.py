from typing import List, Optional

class Stack:
    """
    Create a class Stack that can store only strings and has the following functionality:
    · Instance attribute: data: list
    · Method: push(element) – adds an element at the end of the stack
    · Method: pop() – removes and returns the last element in the stack
    · Method: top() - returns a reference to the topmost element of the stack
    · Method: is_empty() - returns boolean True/False
    · Override the string method to return the stack data in the format:
    """

    def __init__(self):
        self.data: List[str] = []

    def push(self, item: str):
        item_type = type(item).__name__
        if item_type != "str":
            raise ValueError("Cannot insert value of type {item_type} into stack")
        self.data.append(item)

    def pop(self) -> Optional[str]:
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")

        return self.data.pop()

    def top(self) -> Optional[str]:
        if self.is_empty():
            raise IndexError("Cannot top from empty stack")

        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"
