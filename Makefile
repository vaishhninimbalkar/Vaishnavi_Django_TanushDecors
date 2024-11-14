default:
	grep -E ':\s+#' Makefile

install:
	uv pip install -r pyproject.toml

clearcache:	# Clear Cache
	python3 manage.py clearcache

run:		# Run Server
	python3 manage.py runserver 8000

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser --email admin@via-internet.de --username admin

