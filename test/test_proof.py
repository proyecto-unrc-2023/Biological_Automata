import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

def test_answer2():
    assert inc(5) == 6

# @pytest.fixture: nos da la capacidad de definir un paso genérico (ex. orden) de configuración que se puede reutilizar
# y como se usaría una función normal

# Arrange
@pytest.fixture     # se usa este metodo antes de cada test
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]

def test_string(order):
    # Act
    order.append("b")
    # Assert
    assert order == ["a", "a","b"]

def test_int(order):
    # Act
    order.append(2)
    # Assert
    assert order == ["a", "a", 2]

# todas las pruebas automáticamente solicitan aquellos metodos con autouse=True antes de ejecutarse
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry, first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, first_entry, 2]



def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    # assert 0  # for demo purposes


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    # assert 0  # for demo purposes


# test negativo
# def test_wrong_helo():
#     with pytest.raises(ValueError):
#         re = ValueError()
