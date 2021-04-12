# Eventex

Sistema criado em Python e Django para gerenciar informações de inscrições de um evento.
Uma versão online pode ser conferida [aqui](https://eventex-davischoll.herokuapp.com/).

## Como desenvolver

1. Clonar o repositório;
2. Criar um virtualenv com Python 3.9;
3. Ativar o virtualenv;
4. Instalar as dependências;
5. Configurar a instância com o .env;
6. Executar os testes.

#### - For Unix/Mac:
```console
git clone https://github.com/davischoll/wttd-eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Criar uma instância no Heroku;
2. Enviar as configurações para o Heroku;
3. Definir uma SECRET_KEY segura para a instância;
4. Definir DEBUG=False;
5. Configurar o serviço de email;
6. Enviar o código para o Heroku.

#### - For Unix/Mac:
```console
heroku create minha_instancia
heroku config:push
heorku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configurar o email
git push heroku main --force
```