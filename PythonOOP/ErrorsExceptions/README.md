<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# In class activity - Errors and Exceptions

## Description
You are given a software system for managing a cosmetics shop. The system is already implemented and works. It supports one type of products that can be grouped in categories. The user can:
- Create a category;
- Create a product;
- Add a product to a category;
- Show a category;

## Task
Your **task** is to improve the solution by adding proper **error handling** which serves the need to validate the user input and provide informative and useful messages. The user input should meet the following requirements.

### 1. Category
- Name should be between 3 and 10 symbols.
- Name should be unique in the system.

### 2. Product
- Name should be between 3 and 10 symbols.
- Name should be unique in the system.
- Brand should be between 2 and 10 symbols.
- Price cannot be negative.
- Gender type can be **"Men"**, **"Women"** or **"Unisex"**.

### 3. Commands
- Each command expects exact number of parameters.
- Each command expects correct parameters in correct format.

## Constraints
- You cant change class structure (existing attributes/methods)
    - You can (and should) refactor some of the methods
- You can define your **own errors**.
- You can add try-except blocks.
- You should raise proper errors with proper messages.

## Additional notes
- Follow the error handling best practices.
- Throw errors where the program can not continues its normal flow.
- Handle errors where you can address the problem in the best way.
- There is a new way to define enumerations (collection of constants)  
  Check it in the models.gender file. It comes with built-in validation:
    ```python
    # this will raise error if the gender_str is not one of the allowed Gender values
    gender = Gender(gender_str)
    ```


## Step by step guide

**Hint** There are **TODOs** in the code to help you.

**1.** Define your type of error(s) that will serve your needs.

- You can start with one custom error and later add more if you need.
- You can decide to use only built-in errors

**2.** Implement attributes validation.

**3.** Implement command arguments validations (arguments count and value).

**4.** Add error handling to `CommandFactory` class.

- What should happen if the user enters an invalid command?

**5.** Add error handling to the `Engine` class.

## Input example

```
SomeCommand
CreateCategory S
CreateCategory Shampoos
CreateCategory Shampoos
CreateProduct MyMan 10.99 Men
CreateProduct MyMan N 10.99 Men
CreateProduct MyMan Nivea price Men
CreateProduct MyMan Nivea -5.99 Men
CreateProduct MyMan Nivea 10.99 Gender
CreateProduct MyMan Nivea 10.99 Men
CreateProduct MyMan Nivea 10.99 Men
AddProductToCategory Shampo MyMan
AddProductToCategory Shampoos MyBoy
AddProductToCategory Shampoos MyMan
CreateProduct MyWoman Nivea 17.99 Women
AddProductToCategory Shampoos MyWoman
ShowCategory Shampo
ShowCategory Shampoos
Exit
```

## Output Example

```
Command SomeCommand is not supported.
Category name should be between 3 and 10 symbols.
Category with name Shampoos was created!
Category Shampoos already exists.
CreateProduct command expecte 4 parameters.
Product brand should be between 2 and 10 symbols.
Third parameter should be price (real number).
Price can't be negative
'Gender' is not a valid Gender
Product with name MyMan was created!
Product MyMan already exists!
Category Shampo does not exist.
Product MyBoy does not exist.
Product MyMan added to category Shampoos!
Product with name MyWoman was created!
Product MyWoman added to category Shampoos!
Category Shampo does not exist.
#Category: Shampoos
 #MyMan Nivea
 #Price: $10.99
 #Gender: Men
 ===
 #MyWoman Nivea
 #Price: $17.99
 #Gender: Women
 ===
```
