
all:
	# Usage: make <prepare|build|run|test>

prepare:
	# Installe les dépendances du projet
	pip install pipenv
	pipenv install

build: 
	# Vide, en python on ne build pas :-)

run:
	# Lance l'application
	pipenv run python app.py

test:
	# Lance les test
	pipenv run pylint *.py
	# pipenv run pytest ...

