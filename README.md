# Desafio backend-br  - Empréstimos

Desafio proposto pela comunidade [backend-br](https://github.com/backend-br/desafios). A descrição do desafio pode ser encontrada nesse mesmo repositório, [link](https://github.com/backend-br/desafios/blob/master/loans/PROBLEM.md), mas será resumido aqui.

A estrutura do repositório foi baseada em [The Hitchhiker’s Guide to Python - Structuring Your Project](https://docs.python-guide.org/writing/structure/).

## To-Do

Controle interno

- [X] Implementar API
- [X] Inserir validação de valores de entrad de acordo com os requisitos da [Entradas e Saídas](#entradas-e-saídas)
  - Implementado por meio dos schemas
- [ ] Implementar testes
- [ ] Dockerizar
- [ ] Criar scripts de configuração, inicialização e afins

## Descrição do Desafio

Implementação de um serviço que determina as modalidades de empréstimos que uma pessoa tem acesso. Os empréstimos são permitidos a cada pessoa com base em suas características: idade, salário e localização.

### Tipos e taxas de cada empréstimo

- Empréstimo pessoal: Taxa de juros de 4%
- Empréstimo consignado: Taxa de juros de 2%
- Empréstimo com garantia: Taxa de juros de 3%

### Regras de Negócio

- Conceder o empréstimo pessoal se o salário do cliente for igual ou inferior a R$ 3000
- Conceder o empréstimo pessoal se o salário do cliente estiver entre R$ 3000 e R$ 5000, se o cliente tiver menos de 30 anos e residir em São Paulo (SP)
- Conceder o empréstimo consignado se o salário do cliente for igual ou superior a R$ 5000
- Conceder o empréstimo com garantia se o salário do cliente for igual ou inferior a R$ 3000
- Conceder o empréstimo com garantia se o salário do cliente estiver entre R$ 3000 e R$ 5000, se o cliente tiver menos de 30 anos e residir em São Paulo (SP)

### Entradas e Saídas

Esse serviço deve ser disponibilizado no endpoint `/customer-loans`, que recebe uma requisição do tipo `POST` de acordo com as especificações abaixo:

|Chave|Valor|Descrição|Requisito|
|:--:|:--:|:--:|:--|
|age|int|Idade|valor>=0|
|cpf|str|CPF|Formato: XXX.XXX.XXX-XX ou XXXXXXXXXXX|
|name|str|Nome||
|income|float|Renda|Valor>=0|
|location|str|Localização. Sigla de estado brasileiro.|tamanho=2|

Exemplo:

```json
{
  "age": 55,
  "cpf": "123.456.789-00",
  "name": "Sebastião Rodrigues Maia",
  "income": 1000000.00,
  "location": "RJ"
}
```

Por fim, ela deve retornar o nome do cliente e os empréstimos que a pessoa tem acesso, com a devida especificação:

|Campo|Tipo|
|:--:|:--:|
|customer|str|
|loans|list of dicts with "type": str, "interest_rate": int|

Exemplo:

```json
{
"customer": "Sebastião Rodrigues Maia",
  "loans": [
    {
      "type": "PERSONAL",
      "interest_rate": 4
    },
    {
      "type": "GUARANTEED",
      "interest_rate": 3
    },
    {
      "type": "CONSIGNMENT",
      "interest_rate": 2
    }
  ]
}
```

## Executando a Aplicação

### Requisitos

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
