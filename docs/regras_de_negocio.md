# Regras de Negócio

Definição das regras de negócio para implementação.

## Definição Original

- Conceder o empréstimo pessoal se o salário do cliente for igual ou inferior a R$ 3000
- Conceder o empréstimo pessoal se o salário do cliente estiver entre R$ 3000 e R$ 5000, se o cliente tiver menos de 30 anos e residir em São Paulo (SP)
- Conceder o empréstimo consignado se o salário do cliente for igual ou superior a R$ 5000
- Conceder o empréstimo com garantia se o salário do cliente for igual ou inferior a R$ 3000
- Conceder o empréstimo com garantia se o salário do cliente estiver entre R$ 3000 e R$ 5000, se o cliente tiver menos de 30 anos e residir em São Paulo (SP)

## Implementação Lógica

|Tipo|Condições|
|:--:|:--|
|Empréstimo pessoal|Salário <= R$ 3000<br>ou<br>(R$ 3000 < Salário < R$ 5000) E (Idade < 30 anos) E Loc. = SP|
|Empréstimo consignado|Salário >= R$ 5000|
|Empréstimo com garantia|Salário <= R$ 3000<br>OU<br>(R$ 3000 < Salário < R$ 5000) E (Idade < 30 anos) E (Loc = SP)|

## Taxas de Juro

|Tipo|Taxa (%)|
|:--:|:--:|
|Empréstimo pessoal|4|
|Empréstimo consignado|2|
|Empréstimo com garantia|3|

## Validações

Definir validações de entrada/saída a serem implementadas, com base na tabela

- age
  - int
  - valor>=0
- CPF
  - string
  - Formato: XXX.XXX.XXX-XX ou XXXXXXXXXXX
- name
  - string
  - len > 0
- renda
  - float
  - Valor>=0
- location
  - string
  - len = 2
  - Valores permitidos: AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO
