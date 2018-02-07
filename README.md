## Setup

To set up the environment:
```
python3 -m venv /tmp/ve/
source /tmp/ve/bin/activate
pip install pytest
pip install Django
```

To run the tests for Problem #1:
```
pytest problem1/problem_1.py
```

To run the service from Problem #2 locally you need a valid gmail account:
```
EMAIL_HOST_USER=<valid_address@gmail.com> EMAIL_HOST_PASSWORD=<password> problem2/manage.py runserver
```
Go to ```http://127.0.0.1:8000/```.
