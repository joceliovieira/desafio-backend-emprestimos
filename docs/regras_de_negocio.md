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

Foram implementadas validações nos schemas de entrada `Customer`

```python
class Customer(BaseModel):
    """Classe que representa um cliente."""
    age: int = Field(title="Idade", ge=0) 
    cpf: str = Field(
        title="CPF", 
        min_length=11, 
        max_length=15, 
        regex= r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"
    )
    name: str = Field(title="Nome", min_length=1)
    income: float = Field(title="Renda", ge=0)
    location: str = Field(
        title="Estado", 
        description="Sigla do estado brasileiro.", 
        min_length=2, 
        max_length=2
    )

    @validator("location")
    def validate_location(cls, v):
        if v not in estados_br:
            raise ValueError("Invalid location")
        return v
```
