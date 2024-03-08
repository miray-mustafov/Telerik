<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# BoardR - Task Organizing System

_Part 1_

## 1. Description

**BoardR** is a task-management system which will evolve in the next several weeks. During the course of the project, we will follow the best practices of `Object-Oriented Programming` and `Design`.

## 2. Goals  

Your goal is to design and implement the main building blocks of the application - the **BoardItem**, **Board** and **ItemStatus** classes.

## 3. Setup

- Create a new folder
- Create a `main.py` file
- Create `board_item.py`, `board.py` and `item_status.py`files
- Define the classes in their respective files. 

## 4. ItemStatus class
### Description
This class will be a collection of constants in a particular order - `'Open', 'Todo', 'In progress', 'Done', 'Verified'`. It will have no instance methods or instance attributes. The purpose of this class is to define the only possible Item Statuses.

```py
class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'
```

Note that these are class attributes and are used through the class name: `ItemStatus.IN_PROGRESS`  
To be able to follow the predefined order of statuses, define two class methods `next` and `previous`

```py
@classmethod
def next(cls, current):
    # logic to return the next valid ItemStatus, based on current   
```

If you implement the `next` and `previous` methods correctly, the behavior should be the following
```py
next = ItemStatus.next(ItemStatus.IN_PROGRESS)     # Done
next = ItemStatus.next(ItemStatus.VERIFIED)        # Verified (returns the last if there is no next)
prev = ItemStatus.previous(ItemStatus.IN_PROGRESS) # Todo
prev = ItemStatus.previous(ItemStatus.OPEN)        # Open (returns the first if there is no previous)
```

## 5. BoardItem class

### Description

This class will model our idea of an **Item** that we can put in a **Board** (check [Trello](https://trello.com/)). A BoardItem can be used to describe anything - a **task**, **bug**, **note**, **assignment**...

A minimum viable BoardItem should have at least a `title` (describes what this item is about), `due_date` (when it should be done), and `status` (describes the state of this item - being worked on, being completed, etc..)  

For a useful BoardItem, the `title` should not be empty. The `due_date` should probably be in the future - we can't expect a task to be finished before we created it. There must be some rules on how a BoardItem changes its state - for example, from a state you can only _advance_ to the next one or _rollback_ to the previous one.  

When creating a BoardItem, we must be forced to provide title and date, and we must start from the initial state (a Initializer with the right arguments will come in handy).

### Note about Dates:
- a date object represents a specific calendar date. More info here: https://docs.python.org/3/library/datetime.html#date-objects
- to simplify the creation of dates in the future, we can use the following code:
```py
from datetime import date, timedelta

def add_days_to_now(d):
    return date.today() + timedelta(days = d)
```

### Initializer

- Should accept a `title`, a `date` and assign those to their respective Attributes
- A new `BoardItem` must have its `status` as `Open`
- Example:

#### Example

```python
item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
print(item.title)
print(item.due_date)
print(item.status)
```

#### Output

```none
Registration doesn't work
2022-03-18 (this will vary depending on when you run the code)
Open
```

### Attributes

- **title**: _str_, should never be empty, and its length should be between [5, 30] ([How to read bracket notation for ranges?](https://stackoverflow.com/questions/4396290/what-does-this-square-bracket-and-parenthesis-bracket-notation-mean-first1-last))
- **due_date**: _date_, should never be in the past
- **status**: _ItemStatus_, `Open -> Todo -> InProgress -> Done -> Verified` 

> Hint: you can **validate** in the Initializer

### Methods
You can rely on the logic defined in the `ItemStatus` class for the following two methods:
- **revert_status()** - returns the `status` to a previous state - e.g. from **Todo** to **Open**, from **Done** to **InProgress**, etc (no effect if the status is **Open**). 
- **advance_status()** - advances the `status` to a next state - e.g. from **Open** to **Todo**, from **Done** to **Verified**, etc (no effect if the status is **Verified**)

#### Example

```python
item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
print(item.status) # Open
item.advance_status()
print(item.status) # Todo
item.advance_status()
print(item.status) # In progress
item.revert_status()
print(item.status) # Todo
```

#### Output

```none
Open
Todo
InProgress
Todo
```

- **info()** - returns information about the current BoardItem in format `title, [status | dueDate]`

#### Example

```python
item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
print(item.info())
```

#### Output

```none
Registration doesn't work, [Open | 2022-03-18]
```

## 5. Board class

### Description

The **Board** class will be used to organize all the BoardItems that we create. In the future, we might want to use it for searching, grouping, viewing, storing...

For now, the **Board** will be no more than a collection of BoardItems. In the next couple of days, we will enhance it.  

### Initializer

Create empty list of BoardItems.

### Attributes

List of BoardItems - we must be able to add items to the board.

### Methods

We will add some in the next chapter.

#### Example

```python
item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
anotherItem = BoardItem('Encrypt user data', add_days_to_now(10))

item.advance_status()

board = Board()

board.items.append(item)
board.items.append(anotherItem)

for board_item in board.items:
    board_item.advance_status()

for board_item in board.items:
    print(board_item.info())

```

#### Output

```none
Registration doesn't work, [In progress | 2022-03-18]
Encrypt user data, [Todo | 2022-03-26]
```
