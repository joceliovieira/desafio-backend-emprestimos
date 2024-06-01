from typing import List, Union, Literal

from pydantic import BaseModel, Field, validator


estados_br = Literal["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

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
    
    

class Loan(BaseModel):
    """Clase que representa um tipo de empréstimo."""
    type: str
    interest_rate: int

class AvailableLoans(BaseModel):
    """Classe que representa a resposta dos empréstimos para um determinado cliente."""
    customer_name: str
    loans: Union[List[Loan], None] = []

class ConsignmentLoan(Loan):
    """Classe que representa o Empréstimo consignado."""
    type: str = "CONSIGNMENT"
    interest_rate: int = 2

class GuaranteedLoan(Loan):
    """Classe que representa o Empréstimo com garantia."""
    type: str = "GUARANTEED"
    interest_rate: int = 3

class PersonalLoan(Loan):
    """Classe que representa o empréstimo pessoal."""
    type: str = "PERSONAL"
    interest_rate: int = 4

class Loans(BaseModel):
    """Classe que contém todos os tipos de empréstimos disponíveis."""
    PersonalLoan: Loan = PersonalLoan()
    ConsignmentLoan: Loan = ConsignmentLoan()
    GuaranteedLoan: Loan = GuaranteedLoan()
