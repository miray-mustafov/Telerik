<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# Ordering App

_Part 3_

### 1. Description
The Ordering app has some of its functionality already implemented
- Product endpoints:
    - ✔ GET /products (*with optional query params*)
    - ✔ GET /products/{id}
    - ✔ POST /products
    - ✔ PUT /products/{id}
- Order endpoints:
    - ✔ GET /orders (*with optional query params*)
    - ✔ GET /orders/{id}
    - ✔ POST /orders
    - ✔ PUT /orders/{id}
    - ✔ DELETE /orders/{id}
- Category endpoints:
    - ✔ GET /categories
    - ✔ GET /categories/{id}
    - ✔ POST /categories
- Missing functionality:
    - Web client (*will be added later by the Frontend team*)
    - Console client (*will be added later by whoever is available*)

### 2. Goals  
- Practice refactoring existing code
- Practice writing routers and services

### 3. Tasks for today:
- Create an `orders` router (Presentaion Layer)
- Create an `orders` service (Business Layer)

### 4. Before you start
One of the other backend developers has already refactored some of the existing functionality and has created a `categories` and `products` routers and also `categories` and `products` services. For inspiration, take a look at their code.

As the newest member of the team, your task is to refactor the `main.py` file. Move all the logic from the `/orders/` endpoints into `orders` router and `orders` service.

Use your better judgement to decide what functions will be needed in the new files.

Try to achieve something similar to the existing routers/services, as consistency in application is important.

### 5. Orders router
- Create an `orders` module in the `routers` folder
- This router will be responsible for all `/orders` endpoints
- Do not forget to include the router in the main app
- Take a look at how existing routers are implemented

### 6. Orders service
- Create an `order_service` module in the `services` folder
- Move some of the functionality from the orders router to the new service. **You** decide what functions with what logic to create - there is no right or wrong, just think, ask yourself questions, and gain experience.
- Take a look at the existing services for inspiration.

#### Hints
1. You can start with the service, and then continue with the router. There are no established procedures such as 'first implement the router, then the service'
2. When you are finished with refactoring an endpoint, test with Postman to verify that everything still works correctly.
3. You are not expected to implement new or modify the existing functionality, only to refactor the code.