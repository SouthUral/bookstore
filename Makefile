migrate:
	poetry run bookstore/manage.py migrate

makemigrations:
	poetry run bookstore/manage.py makemigrations

runserver:
	poetry run bookstore/manage.py runserver 7002

update:
	poetry run bookstore/manage.py makemigrations
	poetry run bookstore/manage.py migrate