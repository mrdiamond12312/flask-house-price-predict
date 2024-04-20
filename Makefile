clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	py -3.9 -m pip install -r requirements.txt

run:
	py -3.9 manage.py run

all: 
	commit-linter install
	install run