# store_inventory
This is store inventory management system website coded in Django. The back end uses python and a SQLite database, and the front end uses javascript, Bootstrap for styling, and D3 for charts.

## Features
### Product Data
Products can be added to the system. All products have a description, a category, and a unique UPC code. The quantity of products (QTY) is updated with sales and restocks. Sales of products over time are rendered in charts.

### Finding Products
Products can be sorted by name, QTY, and UPC. Products can be searched for by name or by UPC. Additionally, products can be filtered by category.

## Screenshots
<img width="550" alt="Screenshot 2024-10-23 at 2 08 12 AM" src="https://github.com/user-attachments/assets/438726b5-b5d4-4b65-8035-e67835eefd2f">

<img width="550" alt="Screenshot 2024-10-23 at 2 09 17 AM" src="https://github.com/user-attachments/assets/9e1f8f93-9b24-4808-9b6c-2bf84c530f58">

## Setup

First, create a virtual environment:
```sh
$ python -m venv myworld
```

You must then activate the environment by running:
```sh
$ source myworld/bin/activate
```

Navigate to the directory of the environment and clone the repo.

Then install the dependencies:
```sh
$ pip install -r requirements.txt
```

To add 20 dummy items to the database, run:
```sh
$ python manage.py add_items
```

After the dependencies are finished installing, run the command below to start the server:
```sh
$ python manage.py runserver
```

You can now see the site running on `http://127.0.0.1:8000/` .


## Running Tests

This command will run back end tests:

```sh
$ python manage.py test
```
