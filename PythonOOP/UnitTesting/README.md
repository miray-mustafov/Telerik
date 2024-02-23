<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# In Class Activity - Unit Testing

## Description
You are given a software system for managing a cosmetics shop. The system is already implemented and works. It supports one type of products that can be grouped in categories. The user can:
- Create a category;
- Create a product;
- Add a product to a category;
- Show a category;

## Task
Your **task** is to cover some of the functionality with unit tests.

### 1. Product Tests
- Initializer 
    - should create successfully
    - should raise error with invalid data
- Setters
    - should change value successfully
    - should raise error with invalid data
- to_string
    - should return correctly formatted output
- 10-15 tests total

### 2. Category Tests
- Initializer 
    - should create successfully
    - should raise error with invalid data
- Setters
    - should change value successfully
    - should raise error with invalid data
- add_product
    - inspect the method and write a separate test for each distinct scenario
- remove_product
    - inspect the method and write a separate test for each distinct scenario
- to_string 
    - inspect the method and write a separate test for each distinct scenario
- 10-15 tests total

### 3. Test the `ApplicationData` class
- Initializer 
    - should initialize correctly
- Properties
    - should return collections as tuples
- Methods
    - inspect the methods and write a separate test for each distinct scenario
    - if time is running short, test only product-related OR category-related methods, as they are quite similar in functionality
- 10-12 tests total

### 4. Test the `ShowCategoryCommand` class
- Initializer 
    - should initialize correctly
    - should raise error with invalid params count
- Execute (Advanced)
    - testing this method will be difficult, as it requires extensive setup of an ApplicationData object
    - the proper way to test this method is by using *Mocks*
- 3-4 tests total

## Note
Some of the methods require knowledge of mocking to unit test properly. 
We will learn more about mocks in a session later in the last module of the course.
