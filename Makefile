install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test_hello:
	python -m pytest -vv test_hello.py

lint_hello:
		pylint --disable=R,C, hello.py

test_is_leap:
	python -m pytest -vv test_is_leap_year.py

lint_is_leap:
	pylint --disable=R,C is_leap_year.py

lint:
	pylint --disable=R,C,W1203,W0702 app.py

all: install lint
