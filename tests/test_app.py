from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_dev_retornar_OK_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}

# chave: fabioborges-py
# ssh-keygen -t rsa -b 4096 -C "fabio.borges.py@gmail.com"
# SHA256:m9zUfHQFjp1U6/D5boX0nrKgZVFEzwUbrR1HWYDSswA fabio.borges.py@gmail.com

