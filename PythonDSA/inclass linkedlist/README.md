<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

# Linear Data Structures

### 1. Description 

In this exercise, we are going to practice classic problems involving linear data structures. Try your best by following the guides, debugging your implementation, and if all else fails, consulting with the solutions. These tasks are common interview questions and you are **very likely to encounter them again**.

### 2. Project information 
- You are given unit tests to verify the correctness of your implementations.
- Write your code in the provided functions.
- Do not change the function names and signatures

### 3. Middle of the Linked List
Finish the `find_middle_of_list` function:
```py
def find_middle_of_list(head):
    # your implementation:
```

The function takes the `head` of a singly linked list and returns a new list which starts at the middle of the original one:
```
head: 1 -> 2 -> 3 -> None
returns: 2 -> 3 -> None

head: 1 -> 2 -> 3 -> 4 -> None
returns: 3 -> 4 -> None
```

If this was an array, it would be easy, but lists have no indices. One possible solution is to traverse the whole list, store the nodes somewhere and, when finished, return the middle node - `O(n)` time, but `O(n)` additional space

There is another solution, which is `O(n)` time and `O(1)` space


### 4. Merge Sorted Linked Lists 
Finish the `find_middle_of_list` function:
```py
def find_middle_of_list(h1, h2):
    # your implementation:
```
The function takes the heads of the sorted linked lists `(h1, h2)` and returns the head of a new sorted linked list, that is the merge of the other two:
```
h1: 1 -> 2 -> 3 -> None
h2: 1 -> 4 -> None

returns: 1 -> 1 -> 2 -> 3 -> 4 -> None
```

Try to think about the problem for a while, but if you get lost, here are some basic steps:
1. Compare the current h1 value with the current h2 value.
2. Append the lower value to the merged list.
3. Advance the lower of the two nodes to the next node.
4. Repeat until both h1 and h2 are None.
5. Return the head of the merged list.

### 5. Reverse Linked List
Finish the `reverse_list` function:
```py
def reverse_list(head):
    # your implementation:
```
The function takes the `head` of a singly-linked list and returns the head of its reversed counterpart:
```
head: 1 -> 2 -> 3 -> 4 -> None
returns: 4 -> 3 -> 2 -> 1 -> None
```
#### Approach I
You can push all nodes to a stack and then construct the reversed list by popping them.  
This will consume additional O(n) memory.

#### Approach II (Advanced)
You can solve it without additional memory (O(1) complexity) by using one additional reference and constructing the reversed list on the fly. (Each `next` node is actually `prev` for the `current` one in the reversed list.)


### 6. Valid Parentheses
Finish the `validate_parentheses` function:
```py
def validate_parentheses(expression):
    # your implementation:
```
The function takes an `expression` and determines if every closing bracket has a corresponding opening bracket.
```
expression: 1 + (2 * 3)
returns: true

expression: 2 + (1 + (2 * 3)
return: false
```

Try solving it by using a stack. 
1. Think about **when** and **what** to `push` and when to `pop`
1. What happens if its time to `pop` but the stack is empty?
1. If the expression is valid, how many items do you expect to find in the stack?


### 7. Backspace Char Deletion
Finish the `backspace_char` function:
```py
def backspace_char(sequence):
    # your implementation:
```
Imagine a user typing on a keyboard. The keystrokes represent a sequence: 'a', 'b', 'c', 'backspace', 'd'.
The final output on the screen is `abd` because the user has deleted the 'c'.
The backspace keystroke is represented by a '#'.
The `backspace_char` function takes a sequence of keystrokes, represented by a string, and calculates the output for the screen.
```
sequence: 'abc#d'
returns: 'abd'

sequence: 'abcd##e##'
returns: 'a'
```

You can once again use a stack.
1. Most of the keystrokes will be pushed, but sometimes (think when) you need to pop.
1. At the end, you must convert the remaining stack elements to a string.
