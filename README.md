# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `products`, so we will use the following URLS - `/products/` and `/products/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`products` | GET | READ | Get all products
`products/:id` | GET | READ | Get a single product
`products`| POST | CREATE | Create a new produc
`products/:id` | PUT | UPDATE | Update a product
`products/:id` | DELETE | DELETE | Delete a product

`providers` | GET | READ | Get all providers
`providers/:id` | GET | READ | Get a single provider
`providers`| POST | CREATE | Create a new provider
`providers/:id` | PUT | UPDATE | Update a provider
`providers/:id` | DELETE | DELETE | Delete a provider
