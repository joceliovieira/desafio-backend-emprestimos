# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help make

help: ## Exibe essa mensagem de ajuda.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

init: build start ## Inicializa a aplicação (build + start)

build: ## Constrói a aplicação
	@docker compose build

start: ## Inicia a aplicação
	@docker compose up

stop: ## Para a aplicação
	@docker compose stop

remove: ## Para e remove a aplicação
	@docker compose down

logs: ## Exibe os logs da aplicação
	@docker compose logs -f --timestamps