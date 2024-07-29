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
# SHA256:mRvGgQqjLUH1EtUt+YqpViZGegt3+Xlcy4VjQkprTxg fabio.borges.py@gmail.com

#git clone https://github.com/fabioborges-py/exoteric_core.git

#git remote add origin git@github.com:fabioborges-py/exoteric_core.git

# Your identification has been saved in fabioborges-py
# Your public key has been saved in fabioborges-py.pub
# The key fingerprint is:
# SHA256:mRvGgQqjLUH1EtUt+YqpViZGegt3+Xlcy4VjQkprTxg fabio.borges.py@gmail.com
# The key's randomart image is:
# +---[RSA 4096]----+
# | ..o... o        |
# |.   o  = .       |
# |. o. .. +        |
# | + +.. E *       |
# |o + . = S   .    |
# | + = B B = = .   |
# |  = B o * = +    |
# |   +   o + o     |
# |  .     .        |
# +----[SHA256]-----+
