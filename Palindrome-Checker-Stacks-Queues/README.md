# Palindrome Checker Using Stacks and Queues

## 1. Introduction
A palindrome is a word, number, or sentence that reads the same forward and backward when the chosen characters are considered. Examples include `MADAM`, `LEVEL`, and `RADAR`.

This project checks whether user-entered text is a palindrome by using both a stack and a queue.

## 2. Problem Statement
Develop a program that accepts text, stores its normalized characters in a stack and a queue, and compares the characters removed from each structure to determine whether the text is a palindrome.

## 3. Aim
To implement a palindrome checker using the Stack and Queue data structures.

## 4. Objectives
- Understand stack and queue operations.
- Demonstrate LIFO (Last In, First Out) and FIFO (First In, First Out).
- Normalize text by ignoring spaces, punctuation, and letter case.
- Compare characters using the two data structures.
- Display a clear result to the user.

## 5. Data Structures Used

### Stack
A stack follows **LIFO**: the last item inserted is the first item removed. The program uses `push()` and `pop()` operations.

### Queue
A queue follows **FIFO**: the first item inserted is the first item removed. The program uses `enqueue()` and `dequeue()` operations.

### Why use both?
The queue returns characters in their original order. The stack returns them in reverse order. If corresponding characters match, the normalized text is a palindrome.

## 6. Algorithm
1. Start the program.
2. Ask the user to enter a word or sentence.
3. Convert the input to lowercase and remove spaces and punctuation by keeping only letters and digits.
4. If no letters or digits remain, display a message and ask for input again.
5. Insert each normalized character into both the stack and queue.
6. Repeatedly pop one character from the stack and dequeue one character from the queue.
7. If any pair differs, mark the text as not a palindrome.
8. Display the normalized text and the result.
9. Ask whether the user wants to check another text.
10. Stop when the user chooses to exit.

## 7. Pseudocode
```text
INPUT text
normalized_text = lowercase letters and digits from text
CREATE empty stack
CREATE empty queue

FOR each character in normalized_text:
    PUSH character onto stack
    ENQUEUE character into queue

palindrome = true
WHILE stack is not empty:
    stack_character = POP stack
    queue_character = DEQUEUE queue
    IF stack_character != queue_character:
        palindrome = false
        BREAK

DISPLAY result
```

## 8. Example
Input:
```text
Enter a word or sentence: Never odd or even
```

Normalized text: `neveroddoreven`

Output:
```text
Result: It IS a palindrome.
```

Another example:
```text
Enter a word or sentence: Hello
```
Output:
```text
Result: It is NOT a palindrome.
```

## 9. Complexity Analysis
Let `n` be the number of letters and digits in the input.
- **Time Complexity:** `O(n)` because each character is inserted and removed at most once.
- **Space Complexity:** `O(n)` because the stack and queue store the normalized characters.

## 10. Applications
- Learning stack and queue operations.
- Text and string-processing exercises.
- Basic palindrome validation in educational programs.

## 11. Advantages
- Simple to understand and demonstrate.
- Uses both required data structures directly.
- Handles uppercase letters, spaces, and punctuation.
- Allows multiple checks in one run.

## 12. Limitations
- This is a console-based educational program.
- It checks textual palindromes, not language-specific spelling rules.
- It ignores spaces, punctuation, and letter case.

## 13. How to Run
Make sure Python 3.8 or newer is installed. In a terminal, run:
```bash
python palindrome_checker.py
```
If your system uses `python3`, run:
```bash
python3 palindrome_checker.py
```

## 14. Conclusion
This project demonstrates how a stack reverses the order of characters and a queue preserves their original order. Comparing the outputs provides a practical example of using stacks and queues together.
