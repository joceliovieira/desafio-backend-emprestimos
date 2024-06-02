from app.schemas import ConsignmentLoan, Customer, GuaranteedLoan, Loans, PersonalLoan


# Criação de testes com a metodologia AAA - arrange, act, assert


# Teste do modelo de cada tipo de empréstimo disponível
# ConsignmentLoan
def test_consignement_loan():
    consignment_loan = ConsignmentLoan()
    assert consignment_loan.type == "CONSIGNMENT"
    assert consignment_loan.interest_rate == 2

# GuaranteedLoan
def test_guaranteed_loan():
    guaranteed_loan = GuaranteedLoan()
    assert guaranteed_loan.type == "GUARANTEED"
    assert guaranteed_loan.interest_rate == 3

# PersonalLoan
def test_personal_loan():
    personal_loan = PersonalLoan()
    assert personal_loan.type == "PERSONAL"
    assert personal_loan.interest_rate == 4


# Teste do modelo de empréstimos disponíveis - Loans
def test_loans():
    loans = Loans()
    assert isinstance(loans.PersonalLoan, PersonalLoan)
    assert isinstance(loans.ConsignmentLoan, ConsignmentLoan)
    assert isinstance(loans.GuaranteedLoan, GuaranteedLoan)


# Teste do modelo do cliente - Customer
def test_customer():
    customer = Customer(
        age=80, 
        cpf="123.456.789-00", 
        name="Moacir Santos", 
        income=5000.0, 
        location="PE"
    )
    assert customer.age == 80
    assert customer.cpf == "123.456.789-00"
    assert customer.name == "Moacir Santos"
    assert customer.income == 5000.0
    assert customer.location == "PE"


# Testes de validação de dados do cliente
# Idade
def test_customer_invalid_age():
    try:
        Customer(
            age=-2,
            cpf="123.456.789-00",
            name="Moacir Santos",
            income=5000.0,
            location="PE",
        )
    except ValueError:
        pass

# CPF
def test_customer_invalid_cpf():
    try:
        Customer(
            age=30,
            cpf="dufha89f72gh3u",
            name="Moacir Santos",
            income=5000.0,
            location="PE",
        )
    except ValueError:
        pass
    
# Nome
def test_customer_invalid_name():
    try:
        Customer(
            age=30,
            cpf="123.456.789-00",
            name="",
            income=5000.0,
            location="PE",
        )
    except ValueError:
        pass

# Renda
def test_customer_invalid_income():
    try:
        Customer(
            age=30,
            cpf="123.456.789-00",
            name="Moacir Santos",
            income=-1000.0,
            location="PE",
        )
    except ValueError:
        pass

# Localização
def test_customer_invalid_loc():
    try:
        Customer(
            age=30,
            cpf="123.456.789-00",
            name="Moacir Santos",
            income=5000.0,
            location="XX",
        )
    except ValueError:
        pass
