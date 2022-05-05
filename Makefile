.PHONY: help dist install uninstall clean upload upload_test tests

RESET := \033[m
BOLD := \033[1m
ITALIC := \033[3m
UNDERLINE := \033[4m

NAME := skyplot
AUTHOR := Shreya Prabhu
ORG := The GHRSS Survey Collaboration
TESTPYPI := https://test.pypi.org/legacy/

help: ## Print this help message.
	@printf "A simple Makefile for ${BOLD}${NAME}${RESET}\n\n"
	@printf "${ITALIC}Written by ${AUTHOR}${RESET}\n"
	@printf "${ITALIC}Maintained by ${ORG}${RESET}\n\n"
	@printf "${UNDERLINE}Plot the sky coverage and discoveries of the GHRSS survey.${RESET}\n\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	 sort | \
	 awk 'BEGIN {FS = ":.*?## "}; {printf "\033[1m%-20s\033[0m \033[3m%s\033[0m\n", $$1, $$2}'

dist: ## Build source distributions and wheels.
	python setup.py sdist bdist_wheel

install: ## Install this package in development mode.
	pip install -e .

uninstall: ## Uninstall this package.
	pip uninstall ${NAME}
	rm -rf src/${NAME}.egg-info

clean: ## Remove all python cache and build files.
	rm -rf tmp
	rm -rf dist
	rm -rf build
	rm -rf .eggs
	rm -f .coverage
	rm -rf .pytest_cache
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

upload: ## Upload source distributions and wheels to the REAL PyPI.
	twine upload dist/*

upload_test: ## Upload source distributions and wheels to the TEST PyPI.
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

tests: ## Run unit tests and print a coverage report.
	nox -s tests
