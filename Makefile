SHELL = /bin/bash -c
VIRTUAL_ENV = $(shell poetry env info --path)
export BASH_ENV=$(VIRTUAL_ENV)/bin/activate

.PHONY: lint test install clean run build release complexity-baseline

lint: _black _mypy

test: lint complexity-baseline
	pytest --cov --mypy --cov-report term-missing --junitxml=reports/pytest.xml --cov-report xml:reports/coverage.xml

install: $(VIRTUAL_ENV)
	poetry install

clean:
	[[ -d "$(VIRTUAL_ENV)" ]] && rm -rf "$(VIRTUAL_ENV)" || true
	[[ -d .mypy_cache ]] && rm -rf .mypy_cache || true
	[[ -d .pytest_cache ]] && rm -rf .pytest_cache || true
	[[ -d dist ]] && rm -rf dist || true
	[[ -d reports ]] && rm -rf reports || true
	[[ -d pull_request_codecommit/pull_request_codecommit.egg-info ]] && rm -rf pull_request_codecommit/pull_request_codecommit.egg-info || true
	[[ -f .coverage ]] && rm .coverage || true

build:
	python setup.py sdist

release: build
	twine upload dist/*

complexity-baseline:
	$(info Maintenability index)
	radon mi --min A --max A --show --sort pull_request_codecommit
	$(info Cyclomatic complexity index)
	xenon --max-absolute A --max-modules A --max-average A pull_request_codecommit

.PHONY: _black _mypy

_black:
	$(info [*] Formatting python files...)
	black .

_mypy:
	$(info [*] Python static type checker...)
	mypy --junit-xml reports/typecheck.xml pull_request_codecommit

$(VERBOSE).SILENT:
