<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

# In class activity - Higher-order and Anonymous Functions

In this activity, we will practice using the built-in higher-order functions `map` and `filter` and writing anonymous functions with the `lambda` syntax

### 1. Filter

The filter is applied to a **collection**. It accepts two parameters: 1) a **condition function** (also called a predicate) and 2) a collection of elements It returns a **filter result object** with only the elements for which the **condition** is true. The filter result can be iterated or converted to a list through the list class. 

Example: If we have an list `[4,2,1,3,5,8]` and we want to get only the even numbers, we can create a simple for loop with a condition inside it and push each even number to a new list. On the other hand, wouldn't it be easier if we have the for loop ready to use inside a function, and that function only requires from us to tell it what the condition is? This is exactly what `filter` does.

```python
numbers = [4, 2, 1, 3, 5, 8]
evens = filter(lambda n: n % 2 == 0, numbers)

for n in evens:
    print(n)
```

Important to remember about the `filter` is that the original list is not modified in any way.



Filter can be used on lists with elements of any type. For example, we can filter out the names which start with 'A'.

As you can see, the only real difference with the previous example with numbers, is in the **condition** function: `p => p.startsWith('A')`

```python
people = ['Alice', 'Bob', 'Charlie']
start_with_A = filter(lambda person: person[0] == 'A', people)

for person in start_with_A:
    print(person)
```

Practice several basic tasks for filter:
1. Filter all the numbers which are less than 5 or larger than 15.  
    Example: `[1,15,2,8,31,5,9]` -> `[1,2,31]`
1. Filter all the numbers which are larger than 5 and less than 15.  
    Example: `[1,15,2,8,31,5,9]` ->  `[8,9]`
1. Filter all the numbers which are prime.  
    Example: `[1,15,2,8,31,5,9]` -> `[2,31,5]`
1. Filter all the strings which longer than 5 symbols.  
    Example: `['cat', 'dog', 'elephant', 'cucumber']` -> `['elephant', 'cucumber']`
1. Filter all the strings that include a certain substring.  
    Example: `['cat', 'dog', 'duck', 'cucumber']`, `'uc'` -> `['duck', 'cucumber']`


### Map

Map is similar to filter in usage, but what it does is different. It also accepts two parameters: a **transformation function** and a collection. It returns a **map result object** containing the same number of elements as the original list, but with the transformation applied. The original list is not modified.

Map is a very useful function, because we can use it to transform some data into a more convenient form. For example, if we have some generic string input which we know contains numbers, we can transform it into a collection of numbers. We can safely use arithmetic operators on them later. In this example, we apply the Number function on each element.

```python
strings = ['42', '23', '15', '2'] 
integers = map(int, strings)

for n in integers:
    print(n)
```

Now, solve each of the following tasks by using `map`. 


1. Double each number in an list of numbers.  
    Example: `[1,2,3,4]` -> `[2,4,6,8]`
    
1. Uppercase each string in an list of strings.  
    Example: `['cat', 'dog']` -> `['CAT', 'DOG']`
    
1. Transform each string to the opposite case.  
    Example: `['cat', 'DOG']` -> `['CAT', 'dog']`
    
1. Normalize each string. Normalization means taking a string containing any case letters and making it capitalized.  
    Example: `['eLepHANT', 'CucuMbeR']` -> `['Elephant', 'Cucumber']`
    

### Advanced Task: Reduce

There is another very famous higher-order function reduce, which is similar to `map` and `filter`

The reduce function is the trickiest to learn and most confusing of the three functions. `reduce` accepts an additional argument: an initial value. It is named 'reduce' because it *reduces* a collection of elements to **single** value by applying the **reducer function** to each element. The initial value is used in the first iteration for the 'accumulator'.

The reducing function accepts two parameters - the 'accumulator' and the 'prev' value

Iterating the list, at each step, the reducer function is called. The reducer function receives the **accumulated** value from previous iterations and the **current** element of the collection and combines them in some way.

**Note**: `reduce` is importent from the `functools` module

The simplest example is to sum some numbers. 
```python
numbers = [2,5,7]
total = reduce(lambda accum, current: accum + current, numbers, 0)
print(total)
```
- In the example above, the first parameter of reduce is the reducer function (`lambda accum, current: accum + current`).
- The second parameter is the collection
- The third parameter is the initial value, which is logically 0

- The reducing function will be invoked three times, because we have three elements that we want to sum.
- On each iteration, the reducer function is called with the accumulated value (`accum`), and the current element in the list (`current`)
    - Iteration 1: `lambda 0, 2: 0 + 2` -> **accum** is the initial value 0, **current** is the current element 2. The result 2 is stored for the next iteration
    - Iteration 2: `lambda 2, 5: => 2 + 5` -> **accum** is the previous result 2, **current** is the current element 5. The result 7 is stored for the next iteration
    - Iteration 3: `lambda 7, 7: => 7 + 7` -> **accum** is the previous result 7, **current** is the current element 7. The result 14 is stored for the next iteration.
    - There are no more iterations. The previous result 14 is returned.

Any sort of collection can be reduced. If you don't supply an initial value, the first element of the collection will be used:
In this example, `joined` is the string **'cat, dog'**

```python
animals = ['cat', 'dog']
joined = reduce(lambda res, animal: res + ', ' + animal, animals)
```

In the following example, `joined` is the string **', cat, dog'**. Notice the leading empty string. That is the initial value.

```python
joined = reduce(lambda res, animal: res + ', ' + animal, animals, '') # with initial value
```

Now, let's exercise reduce:
1. Return the product of an list of numbers.  
    Example: `[1,2,3,4,5]` -> `120`
1. Return the maximum number in an list of numbers. *Hint: with reduce you can also replace the result of the previous iteration.*  
    Example: `[7, 13, 72, 14]` -> `72`
1. Return the longest string in an list of strings.   
    Example: `['cat', 'dog', 'elephant', 'cucumber']` -> `elephant`  
1. Reverse a string. *Hint: A string is just an list of characters. To use reduce on a string, you can spread it an list like this: `[...'apple'].reduce(...`*    
    Example: `apple` -> `elppa`

