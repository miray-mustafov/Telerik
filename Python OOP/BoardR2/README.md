<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# BoardR - Task Organizing System

_Part 2_

## 1. Description

**BoardR** is a task-management system which will evolve in the next several weeks. During the course of the project, we will follow the best practices of `Object-Oriented Programming` and `Design`.

## 2. Goals

Your goals for this part of the project are to properly encapsulate **BoardItem** and **Board**.

You will also enhance individual board items and the board with the ability to **keep track of the history of their changes**.

## 3. Encapsulate the BoardItem Class

### Issues

Currently, the BoardItem class works well, but may be **misused**. All the members of the class are available outside the class, which may lead to mistakes. For example, the **status** can be changed without following the rules:

```python
item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
item.advance_status() # properly changing the status
item.advance_status()
print(item.info()) # Status: InProgress

item.status = ItemStatus.OPEN; # ???
print(item.info()) # Status: Open
```

> **Note**: Developers will not intentionally break code like in the example above; however, a new developer on the team will not be aware that we are not supposed to directly manipulate the **status** attribute. This can lead to subtle bugs.
We can solve the issue with the **status** attribute by restricting who can access it.

The "restricting" is done by **convention** - by prefixing attributes or methods with _ (underscore), we warn unfamiliar developers about using that attribute/method from outside the class.
```python
def __init__(self, title: str, due_date: date):
    # other code
    self._status = ItemStatus.OPEN
```

To let the outside code read this value, we can create a `@property getter`:

```python
@property
def status(self):
    # return the value of the internal status attribute
```

### Description

We are done with the status attribute, but there are two more attributes - **due_date** and **title**. They are still public and can be freely changed. Let's encapsulate those attributes.

- `due_date` - can be changed, but the new value should not be in the past.
- `title` - can be changed, but the new title must be at least 5 characters long, and no more than 30.

You can use `@property setters` the perform the validations:

> Note: Only add setters if you want to allow other code change the value of the attribute.

```python
@property
def title(self):
    return self._title

@title.setter
def title(self, value):
    # perform the necessary validation

    self._title = value
```

After the changes, test with the following code:

```python
item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
item.title = 'Rewrite everything now!!' # Ok
item.title = 'Nah!' # ValueError: Illegal title length [5:30]
```

Perform the same encapsulations for the `due_date` attribute. Ensure that an error is raised if the new date is before `date.today()`

## 4. EventLog class

### Description

In order to keep track of each operation that we perform on an item or in the board, we need a proper model. At the very least, we need a description of **what** happened - a `string`, and a record of **when** it happened - a `datetime`. 

> Note: Difference between `datetime` and `date` - first records date and hour+minutes+seconds+milliseconds, the second - only date. (example: `22/10/2022 17:22:31` vs `22/10/2022` )

An EventLog instance records an event that took place at a specific time. We can't go back in time and change that, so we will keep the properties getter-only (also known as `readonly`).

### Initializer & Attributes

- **description**: _str_; should not be empty
- **timestamp**: _datetime_; should be initialized as `now()`

```python
def __init__(self, description: str):
    # validate that description has some meaningful value (not empty)
        
    self._description = # initialize
    self._timestamp = # initialize
```

### Properties

- **description**: _str_ - getter-only
- **timestamp**: _datetime_ - getter-only

### Methods

- **info**: - should return a displayable string representation of the event, for example `[TimeStamp] Description` e.g. `[15-September-2020 11:36:32] Created task`. Search the vast internet for `datetime` example and find a suitable method to format the datetime into a human-readable string. Stick with the default format if you like it.

#### Example

```python
log = EventLog('An important thing happened')
print(log.description)
print(log.info())
```

> Note: Try setting `description` and `timestamp` properties and see what happens

#### Output

```none
An important thing happened
[03/16/2022, 15:22:57] An important thing happened
```

> **Notes**  
> In the EventLog class, we have bundled data (`_description, _timestamp`) with methods that can access the data (`info()`)  
> This process of 'bundling' is also known as **Encapsulation**.
>
> In addition, each instance of type EventLog is **ensured** to be valid:
>
> 1) The Initializer forces you and other developers to provide non-empty strings
> 2) The `_timestamp` is calculated inside the Initializer, which means that it will be valid
> 3) The class only provides getters, and the attributes are prefixed with underscore (_timestamp), meaning that other developers will try to change those at their own risk.
>
> This is a fairly easy example of how we apply Encapsulation to ensure that each instance has a **valid state**  
> Let's take a look at the BoardItem class and how it manages its eventlog history

## 5. BoardItem class

### Extended functionality

On each of these operations, you should add a new EventLog to the item's history

- When Initialized - `Item created: 'Refactor this mess', [15-September-2020 11:36:32]`
- When `due_date/title` - `{Property} changed from {previous} to {new}`
- When `revert/advance_status` - `Status changed from {previous} to {next}` or some error message if the status cannot be changed.  

Add a new method:  
**history()** -> `str` - returns the history for this item instance; display **info** about each event log on a new line in chronological order.

View the example below to get a better idea.

Some things to consider:

- How will you store all the EventLogs - will you need some sort of collection?
- If you choose a collection, will you make it **public/private** or something else?
- If the collection of event logs is public, will somebody be able to **modify it from outside** - perhaps adding a EventLog for **an event that never happened**?
- How do you approach this problem without breaking Encapsulation?

#### Example

```python
item = BoardItem('Refactor this mess', add_days_to_now(2))
item.due_date += timedelta(days=365 * 2)  # two years in the future
item.title = 'Not that important'
item.revert_status()
item.advance_status()
item.revert_status()
print(item.history())

print('\n--------------\n')

anotherItem = BoardItem('Dont refactor anything',  add_days_to_now(2))
anotherItem.advance_status()
anotherItem.advance_status()
anotherItem.advance_status()
anotherItem.advance_status()
anotherItem.advance_status()
print(anotherItem.history())
```

#### Output

```none
[03/16/2022, 15:39:46] Item created: Refactor this mess, [Open | 2022-03-18]
[03/16/2022, 15:39:46] DueDate changed from 2022-03-18 to 2024-03-17
[03/16/2022, 15:39:46] Title changed from Refactor this mess to Not that important
[03/16/2022, 15:39:46] Cant change status, already at Open
[03/16/2022, 15:39:46] Status changed from Open to Todo
[03/16/2022, 15:39:46] Status changed from Todo to Open

--------------

[03/16/2022, 15:39:46] Item created: Dont refactor anything, [Open | 2022-03-18]
[03/16/2022, 15:39:46] Status changed from Open to Todo
[03/16/2022, 15:39:46] Status changed from Todo to In progress
[03/16/2022, 15:39:46] Status changed from In progress to Done
[03/16/2022, 15:39:46] Status changed from Done to Verified
[03/16/2022, 15:39:46] Cant change status, already at Verified
```

## 6. Board class

Let's encapsulate the Board class, too. In the previous part, we had a **public** list `items` that was responsible for storing our items.  

This is convenient, but the `list` class has too many methods, and not all of them are useful for our Board.  

Check out this examples:

```python
item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
anotherItem = BoardItem('Encrypt user data', add_days_to_now(10))

board = Board()
board.items.append(item)
board.items.append(anotherItem)
```

So far so good, we want to be able to add items.

```python
items_count = len(board.items);
```

Also good, knowing how many items we have in total is useful.

How about:

```python
board.items.clear();
```

This looks like a problem - we don't want the allow others to `clear()` the board - this will delete all items. What about all the unfinished tasks?

Also, consider this - adding `item1` three times:
```python
board.items.append(item1);
board.items.append(item2);
board.items.append(item1);
board.items.append(item1);

items_count = len(board.items); // count: 4
```

The `add()` method was useful, but it doesn't prevent you from adding duplicate items.


There are more than 30 methods that the `list` class provides - like removing, sorting, reversing, replacing. The Board class exposes all of them through the items attribute which is of list **list**.  
In other words, _the design of the Board class does not reflect the problems that we are trying to solve._

The first step is to fix the main problem - the list is **public** by convention. You should consider prefixing it with underscore to mark it as sensitive data.

Now it is time to add the required public methods to work with the Board properly

**add_item(item: BoardItem)** - adds to the list of items inside the Board. This method has access to the private list. However, this will all be pointless if you leave the method as it is and just add items without checking if they exist. So, you should add the necessary check and see if such an item **already exists** in the internal list.

The other useful functionality that we are missing is knowing how many items we have in the Board. You can add a property:  

**count** - returns the count of items inside the Board.

```python

```

Let's focus on the following code:

```python
item = BoardItem('Refactor this mess', add_days_to_now(2))
anotherItem = BoardItem('Dont refactor anything',  add_days_to_now(2))

board = Board()
board.add_item(item)
board.add_item(anotherItem)
board.add_item(item) # nothing happens
board.add_item(item) # nothing happens

print(board.count) # 2
```

While the **add_item()** method is successful in adding only unique items, when a duplicate is detected the method invocation does **nothing**. Developers should be notified when an operation they perform goes wrong - for example, when you are accessing an index out of range in a list, you get an exception.

**Refactor** the code to raise an ValueError when a duplicate is added.

```python
board.add_item(item)
board.add_item(anotherItem)
board.add_item(item)
```

Output:

```none
ValueError: Item already in the list
```

> **Notes**  
> The developers, using our board will now be aware of this exceptional case and will handle it. You will also handle it in a future part of the project.
