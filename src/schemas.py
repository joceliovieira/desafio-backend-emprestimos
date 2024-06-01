from typing import Union

from pydantic import BaseModel


class Customer(BaseModel):
    """Classe que representa um cliente."""
    age: int
    cpf: str
    name: str
    income: float
    location: str

class Loan(BaseModel):
    """Clase que representa um tipo de empréstimo."""
    type: str
    interest_rate: int

class AvailableLoans(BaseModel):
    """Classe que representa a resposta dos empréstimos para um determinado cliente."""
    customer_name: str
    loans: Union[list[Loan], None] = []

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