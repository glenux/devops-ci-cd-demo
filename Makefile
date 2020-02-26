
all:

build: 
	#vide, en python on ne build pas :-)

run:
	pipenv run python app.py

test:
	pipenv run pylint *.py
	# pipenv run pytest ...
