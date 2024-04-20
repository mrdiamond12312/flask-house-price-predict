clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install: 
	pip install --default-timeout=100 -r requirements.txt

install39:
	py -3.9 -m pip install -r requirements.txt

run-deploy:
	export FLASK_APP=manage.py
	flask run --host=0.0.0.0

run:
	py -3.9 manage.py run

all: install run

up:
	docker-compose up -d --remove-orphans --build

down:
	docker-compose down