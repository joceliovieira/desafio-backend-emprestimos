# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help make

help: ## Exibe essa mensagem de ajuda.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

init: ## Inicializa a aplicação (build + start)
	@docker compose up -d --build --force-recreate

start: ## Inicia a aplicação
	@docker compose up -d

stop: ## Para a aplicação
	@docker compose stop

remove: ## Para e remove a aplicação
	@docker compose down

logs: ## Exibe os logs da aplicação
	@docker compose logs -f --timestamps

test: ## Executa os testes
	@docker exec -t loans-api pytest -s -x --cov=app -vv

post-test: ## Cria o relatório de cobertura dos testes
	@docker exec -t loans-api coverage html

bash: ## Acessa o bash do container
	@docker exec -it loans-api bash
