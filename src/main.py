from fastapi import FastAPI

from src.schemas import AvailableLoans, Customer, Loans

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
def get_loans(customer: Customer) -> AvailableLoans:
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
    available_loans = AvailableLoans(customer_name=name)
    
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