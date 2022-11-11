install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

all: install lint test