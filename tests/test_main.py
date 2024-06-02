from fastapi.testclient import TestClient

from app.main import AvailableLoans, Customer, Loans, app


# Criação de testes com a metodologia AAA - arrange, act, assert


# Testes para verificação de cada condição de empréstimo disponível.

# Condição 1 de teste
# Renda <= 3000
def test_get_loans_cond1():

    # Arrange
    client = TestClient(app)
    customer = Customer(
        age=40,
        cpf="123.456.789-00",
        name="Sebastião Rodrigues Maia",
        income=3000,
        location="RJ",
    )
    
    # Act
    response = client.post(
        "/customer-loans", json=customer.__dict__
    )
      
    # Assert
    assert response.status_code == 200
    assert response.json() == AvailableLoans(
        customer_name=customer.name,
        loans=[Loans().PersonalLoan, Loans().GuaranteedLoan]
    )



# Condição 2 de teste
# Renda entre 3000 e 5000, idade menor que 30 e localização em SP
def test_get_loans_cond2():

    # Arrange
    client = TestClient(app)
    customer = Customer(
        age=15, cpf="123.456.789-00", name="Boca", income=4000, location="SP"
    )
    
    # Act
    response = client.post(
        "/customer-loans", json=customer.__dict__
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json() == AvailableLoans(
        customer_name=customer.name,
        loans=[Loans().PersonalLoan, Loans().GuaranteedLoan],
    )



# Condição 3 de teste
# Renda maior ou igual a 5000
def test_get_loans_cond3():

    # Arrange
    client = TestClient(app)
    customer = Customer(
        age=30,
        cpf="123.456.789-00",
        name="Randomio da Silva",
        income=5000,
        location="SP",
    )
    
    # Act
    response = client.post(
        "/customer-loans", json=customer.__dict__
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json() == AvailableLoans(
        customer_name=customer.name, loans=[Loans().ConsignmentLoan]
    )



# Teste para verificação da quarta condição de empréstimo disponível.
# Condição que não atende nenhuma das anteriores, logo não há empréstimo disponível.
def test_get_loans_cond4():

    # Arrange
    client = TestClient(app)
    customer = Customer(
        age=45, cpf="123.456.789-00", name="Sivuca", income=3500, location="SP"
    )

    # Act
    response = client.post("/customer-loans", json=customer.__dict__)

    # Assert
    assert response.status_code == 200
    assert response.json() == AvailableLoans(customer_name=customer.name, loans=None)
