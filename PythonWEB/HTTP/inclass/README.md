<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# Ordering App

_Part 1_

### 1. Description
The Ordering app has some of its functionality already implemented
- The product endpoints:
    - ✔ GET /products (*with optional query params*)
    - ✔ GET /products/{id}
    - ✔ POST /products
    - ✔ PUT /products/{id}

### 2. Goals  
- Install FastAPI and Uvicorn
- Install Postman
- Run an already implemented FastAPI application
- Use Postman to create HTTP requests for the Ordering app endpoints

### 3. Install FastAPI and Uvicorn

- Skip if already installed
- Since we will be using the FastAPI framework and the Uvicorn http server, we need to install them. The installation is needed because both python packages are not included in the standard python installation
- We will use the **pip** package installer to download and install globally both FastAPI and Uvicorn
    - Open a terminal
    - Run `pip install fastapi` and `pip install uvicorn`
    - Both packages should now be ready to use. 
- You only need to install those packages once; all activities until the end of the course will use the packages we installed today

### 4. Install Postman
- Skip if already installed
- Go to https://www.postman.com/downloads/
- You can optionally use the web version, but it requires creating an account
    - You can skip account creation if you download and install the Postman app

### 5. Run the Ordering app
- Navigate to /src and open a terminal
- Run `uvicorn main:app`
- Open a browser and type `http://127.0.0.1:8000/docs`. There should be documentation of the available endpoints.

### 6. Use Postman to test the Ordering app  

1. The base url is `http://127.0.0.1:8000`
1. Create a GET request for `/products`. You should receive JSON data representing products
    1. Study the endpoint and use query params to receive the products **sorted by price in descending order**
    1. Use the `/products` endpoint to **search for products by name**
1. Create a POST request that creates a new product
    1. Create a json string describing a new product in the Body tab of the Postman request
    1. Don't forget to set the Content-Type header of the request as `application/json`
    1. Try sending invalid product data and inspect the response
    1. Send a new `GET /products` request to verify that the create products are present in the application data
1. Create a GET request that requests for a single product by id.
1. Create a PUT request that updates a specific product