<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# Ordering App

_Part 6_

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
    - ✔ PUT /orders/{id}/products
    - ✔ DELETE /orders/{id}/products
- Category endpoints:
    - ✔ GET /categories
    - ✔ GET /categories/{id}
    - ✔ POST /categories
- User Endpoints:
    - ✔ POST /users/login
    - ✔ GET /users/info
    - ✔ POST /users/register
    - ✖ GET /users/info
- Missing functionality:
    - ✖ Web client (*will be added later by the Frontend team*)
    - ✖ Console client (**will be added today**)

### 2. Goals  
- Practice using HTTP
- Practice working with JSON

### 3. Tasks for today:
- Create a console client that uses the endpoints defined in the **Ordering App Web Service**
- The client already supports the following functionality
    - ✔ Viewing a category by id
    - ✔ Viewing all categories
    - ✔ Creating a new category
- Missing actions:
    - ✖ Orders - creating, updating, viewing, deleting
    - ✖ Products - creating, updating, viewing, deleting
    - ✖ Users - login, register, info

- Implement commands that consume the `users` endpoints and all of the `orders` or the `products` endpoints (your choice). You can also implement both.

### 4. Setup
1. Make sure that the server is working. Go to the `template/server` folder and start it - open with **cmd** ot **git bash** and type `uvicorn main:app`. You need the server to be working while you develop the client, as the client will keep no data, just call the right endpoints based on what the user wants.
1. In the `template/client` folder, some basic functionality is already implemented. Test if the client can connect to the server by trying one of the implemented actions.

### 5. Login requirements
- On startup, the client should prompt the user to login. Think of a way to preserve the login state between different client startups.
- Do not prompt if a user is already logged in.
- "Logout" action should clear the saved authentication information.


