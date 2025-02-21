# virtual environment commands
venv-create:
	python3 -m venv venv

venv-activate:
	source venv/bin/activate

venv-deactivate:
	deactivate

# python commands
py-install:
	pip install --upgrade pip
	pip install -r requirements.txt --upgrade

py-run-tests:
	pytest tests

# alembic commands
alembic-init:
    alembic init alembic

# fastapi commands
fastapi-run:
	uvicorn main:app --reload
