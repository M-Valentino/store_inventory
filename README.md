# store_inventory

## Setup

After cloning the repo, navigate to the repo folder in your terminal.
Next, create a virtual environment:
```sh
$ python -m venv myworld
```

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
