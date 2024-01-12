.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
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
	poetry run black data_playground

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: notebook
notebook: ## Launch a jupyter notebook
	@echo "🚀 Launching a jupyter notebook with the root directory as the project root"
	poetry run jupyter notebook --notebook-dir=./notebooks/

.DEFAULT_GOAL := help
