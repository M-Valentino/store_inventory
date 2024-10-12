# store_inventory

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
```sh

You can now see the site running on `http://127.0.0.1:8000/` .


## Running Tests

This command will run back end tests:

```sh
$ python manage.py test
```
