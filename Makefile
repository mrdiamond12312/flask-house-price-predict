clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	py -3.9 -m pip install -r requirements.txt

run-deploy:
	export FLASK_APP=manage.py
	flask run --host=0.0.0.0

run:
	py -3.9 manage.py

all: install run