.PHONY: install
install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	pip3 install poetry
	poetry install

.PHONY: runserver
runserver: ## Run the server
	@echo "🚀 Running the server"
	poetry run uvicorn widget_server.app:app --reload

.PHONY: lint
lint: ## Run code quality tools.
	@echo "🚀 Linting code: Running ruff"
	poetry run ruff check 

.PHONY: format
format: ## Format the code using black
	@echo "🚀 Formatting code: Running black"
	poetry run black widget_server tests

.PHONY: typing
typing: ## Run mypy to check typing
	@echo "🚀 Checking typing: Running mypy"
	poetry run mypy widget_server tests

.PHONY: test
test: ## Run the tests
	@echo "🚀 Running tests: Running pytest"
	poetry run pytest tests

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
