from fastapi import FastAPI
from pydantic import BaseModel


class customer(BaseModel):
    """Classe que define o cliente."""
    age: int
    cpf: str
    name: str
    income: float
    location: str

class AvailableLoans(BaseModel):
    """Classe que representa a resposta dos empréstimos para um determinado cliente."""
    customer: str
    loans: list = []

class Loan():
    def __init__(self, type: str, interest_rate: int):
        self['type'] = type
        self['interest_rate'] = interest_rate

class PersonalLoan(Loan):
    """Classe que representa o empréstimo pessoal."""
    def __init__(self):
        self.type = "PERSONAL"
        self.interest_rate = 4

class ConsignmentLoan(Loan):
    """Classe que representa o Empréstimo consignado."""
    def __init__(self):
        self.type = "CONSIGNMENT"
        self.interest_rate = 2

class GuaranteedLoan(Loan):
    """Classe que representa o Empréstimo com garantia."""
    def __init__(self):
        self.type = "GUARANTEED"
        self.interest_rate = 3

class Loans():
    def __init__(self) -> None:
        self.PersonalLoan = PersonalLoan().__dict__
        self.ConsignmentLoan = ConsignmentLoan().__dict__
        self.GuaranteedLoan = GuaranteedLoan().__dict__


app = FastAPI(
    title='Empréstimos', 
    summary='API de verificação de empréstimos.',
    version='0.1',
    contact={
        "name": "Jocelio Vieira",
        "email": "jocelio.dev@gmail.com"
    }
)

@app.post("/customer-loans")
def get_loans(customer: customer) -> AvailableLoans:
    """Verifica as regras de negócio e retorna os empréstimos disponíveis.

    Args:
        customer (customer): Instância da classe customer com os dados do cliente a ser verificado.

    Returns:
        AvailableLoans: Retorna os empréstimos disponíveis para o cliente.
    """

    name = customer.name
    income = customer.income
    age = customer.age
    loc = customer.location
    
    loans = Loans()
    available_loans = AvailableLoans(customer=name)
    
    if (income <= 3000):
        available_loans.loans.append(loans.PersonalLoan)
        available_loans.loans.append(loans.GuaranteedLoan)
    elif ((3000<income<5000) & (age < 30) & (loc == "SP")):
        available_loans.loans.append(loans.PersonalLoan)
        available_loans.loans.append(loans.GuaranteedLoan)
    elif (income>=5000):
        available_loans.loans.append(loans.ConsignmentLoan)
    else:
        available_loans.loans = None

    return available_loans