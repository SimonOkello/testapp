# TestApp

TestApp is a simple Python/Django web app for a timed online test.

## Setup

The first thing to do is to clone the repository:.

```bash
git clone https://github.com/SimonOkello/testapp.git
cd testapp
```

## Create a virtual environment to install dependencies in and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```
## Then install the dependencies:

```bash
pip install -r requirements.txt
```
## Usage

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

http://127.0.0.1:8000/

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)