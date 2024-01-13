.PHONY: install
install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	pip3 install poetry
	poetry install

.PHONY: lint
lint: ## Run code quality tools.
	@echo "🚀 Linting code: Running ruff"
	poetry run ruff check 

.PHONY: format
format: ## Format the code using black
	@echo "🚀 Formatting code: Running black"
	poetry run black data_playground notebooks tests

.PHONY: typing
typing: ## Run mypy to check typing
	@echo "🚀 Checking typing: Running mypy"
	poetry run mypy data_playground tests

.PHONY: test
test: ## Run the tests
	@echo "🚀 Running tests: Running pytest"
	poetry run pytest tests

.PHONY: notebook
notebook: ## Launch a jupyter notebook
	@echo "🚀 Launching a jupyter notebook with the root directory as the project root"
	poetry run jupyter notebook --notebook-dir=./notebooks/

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
