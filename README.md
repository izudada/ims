#   Task Description

Create an API for an Inventory Management System.
While the number and endpoints specifics are left to your imagination, the API should handle:

Product creation, deletion, update and retrieval.
Adding product to cart and purchasing product
Keeping track of product quantity in regards to purchase or add to cart functions, i.e the product quantity should reduce when a purchase is made, or when it is added to the "user's" cart; users should be informed when a product is "out of stock"
Products should have (name, category, labels(e.g size, colour etc), quantity, price) A product can have one or more labels.

##  Important Notes:

The User APIs can be ignored, it is assumed that there are users already registered who can purchase or add to cart (this section may be hardcoded or discarded)
There is no need to integrate an actual payment API and extra marks won't be given for it. You can assume that your payment endpoint will debit the user and perform a payment provider shenanigans.


##  Nice to have:
A documentation of the API either on swagger or postman
Handling conditions where two users try purchasing the last item of a product at once


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/ims.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install pipenv:

https://pypi.org/project/pipenv/

then to activate a virtual enviroment:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```


Use migrate command to effect database model:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Start the server with:
```sh
(folder_name)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`


### Useful resources

- [Medium](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f) - How to use environmental values
