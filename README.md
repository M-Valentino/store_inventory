# store_inventory
This is store inventory management system website coded in Django. The back end uses python and a SQLite database, and the front end uses javascript, Bootstrap for styling, and D3 for charts.

## Features
### Product Data
Products can be added to the system. All products have a description, a category, and a unique UPC code. Scannable barcodes are dynamically generated based on UPC codes. The quantity of products (QTY) is updated with sales and restocks. Sales of products over time are rendered in charts.

### Finding Products
Products can be sorted by name, QTY, and UPC. Products can be searched for by name or by UPC. Additionally, products can be filtered by category.

### Spreadsheet Export
Product data from the current view of products displayed in the table can be exported to a CSV. The CSV will have the following data for each product:
- Name
- Category
- UPC
- QTY
- Description
- Date Added

## Screenshots
<img width="550" alt="Screenshot 2024-10-26 at 7 32 26 PM" src="https://github.com/user-attachments/assets/0d511263-11ee-4996-a259-28e54fd4218b">

<img width="550" alt="Screenshot 2024-10-26 at 10 33 24 PM" src="https://github.com/user-attachments/assets/a5bb7dbf-d6fd-4a66-91d2-1f2f0f8ef9fe">

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
