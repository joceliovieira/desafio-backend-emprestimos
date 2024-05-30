# Desafio backend-br  - Empréstimos

Desafio proposto pela comunidade [backend-br](https://github.com/backend-br/desafios). A descrição do desafio pode ser encontrada nesse mesmo repositório, [link](https://github.com/backend-br/desafios/blob/master/loans/PROBLEM.md), mas será resumido aqui.

A estrutura do repositório foi baseada em [The Hitchhiker’s Guide to Python - Structuring Your Project](https://docs.python-guide.org/writing/structure/).

## Descrição do Desafio

Implementação de um serviço que determina as modalidades de empréstimos que uma pessoa tem acesso. Os empréstimos são permitidos a cada pessoa com base em suas características: idade, salário e localização.

Esse serviço deve ser disponibilizado no endpoint `/customer-loans`, que recebe uma requisição do tipo `POST` de acordo com o exemplo abaixo:

```json
{
    "age": int,
    "cpf": str,
    "name": str,
    "income": float,
    "location": str
}
```

Por fim, ela deve retornar o nome do cliente e os empréstimos que a pessoa tem acesso, no formato seguinte:

```json
{
    "customer": str,
    "loans": [
        {
            "type": str,
            "interest_rate": int
        },
        ...
        {
            "type": str,
            "interest_rate": int
        }
    ]
}
```

Onde os tipos e taxas de cada empréstimos são:

- Empréstimo pessoal: Taxa de juros de 4%
- Empréstimo consignado: Taxa de juros de 2%
- Empréstimo com garantia: Taxa de juros de 3%

Por fim, as regras de negócio a serem aplicadas:

- Conceder o empréstimo pessoal se o salário do cliente for igual ou inferior a R$ 3000
- Conceder o empréstimo pessoal se o salário do cliente estiver entre R$ 3000 e R$ 5000, se o cliente tiver menos de 30 anos e residir em São Paulo (SP)
- Conceder o empréstimo consignado se o salário do cliente for igual ou superior a R$ 5000
- Conceder o empréstimo com garantia se o salário do cliente for igual ou inferior a R$ 3000
- Conceder o empréstimo com garantia se o salário do cliente estiver entre R$ 3000 e R$ 5000, se o cliente tiver menos de 30 anos e residir em São Paulo (SP)

## Executando a Aplicação

### Requisitos

Para ser capaz de executar a aplicação, você precisa de:

- (Docker Engine + Docker compose) ou Docker Desktop
- Python 3.11 + pip

### Execução

Os seguintes comandos devem ser executados para gerenciar a aplicação:

- Criar e executar a aplicação: `make init`
- Encerrar e remover: `make down`
- Pausar: `make pause`
- (re)Executar: `make start`

### Testes

Para testar a aplicação executar o comando: `make test`
