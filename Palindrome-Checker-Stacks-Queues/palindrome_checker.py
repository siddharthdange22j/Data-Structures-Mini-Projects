"""Palindrome checker implemented with a stack and a queue."""


class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    """A simple queue implementation using a Python list."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


def normalize_text(text):
    """Keep only letters and digits, and make letters lowercase."""
    return "".join(character.lower() for character in text if character.isalnum())


def check_palindrome(text):
    """Return (normalized_text, is_palindrome) using stack and queue."""
    normalized = normalize_text(text)

    if not normalized:
        return normalized, None

    stack = Stack()
    queue = Queue()

    for character in normalized:
        stack.push(character)
        queue.enqueue(character)

    is_palindrome = True

    while not stack.is_empty():
        stack_character = stack.pop()
        queue_character = queue.dequeue()

        if stack_character != queue_character:
            is_palindrome = False
            break

    return normalized, is_palindrome


def main():
    print("=" * 42)
    print("       PALINDROME CHECKER")
    print("       Using Stack and Queue")
    print("=" * 42)

    while True:
        text = input("\nEnter a word or sentence: ")
        normalized, result = check_palindrome(text)

        if result is None:
            print("Please enter at least one letter or digit.")
        else:
            print("Normalized text:", normalized)
            if result:
                print("Result: It IS a palindrome.")
            else:
                print("Result: It is NOT a palindrome.")

        choice = input("\nCheck another text? (y/n): ").strip().lower()
        if choice != "y":
            print("Thank you for using the Palindrome Checker!")
            break


if __name__ == "__main__":
    main()
