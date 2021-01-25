# lojaonline
Modulo para criação de loja virtual

[![Build Status](https://travis-ci.com/JosemarBrito/lojaonline.svg?branch=main)](https://travis-ci.com/JosemarBrito/lojaonline)
[![codecov](https://codecov.io/gh/JosemarBrito/lojaonline/branch/main/graph/badge.svg?token=OUFHVR2DPW)](https://codecov.io/gh/JosemarBrito/lojaonline)
[![Updates](https://pyup.io/repos/github/JosemarBrito/lojaonline/shield.svg)](https://pyup.io/repos/github/JosemarBrito/lojaonline/)
[![Python 3](https://pyup.io/repos/github/JosemarBrito/lojaonline/python-3-shield.svg)](https://pyup.io/repos/github/JosemarBrito/lojaonline/)

josemar

Cosiderar finalizado ate makemigrations

removido configuração codecov

* pipenv install django
* pipenv sync -d
* pipenv install django
* django-admin
* startproject
* manage.py
* runserver

____

* ambiente virtual - alias mng='python $VIRTUAL_ENV/../manage.py (linux e mac)
* ambiente virtual - doskey mng=@python "VIRTUAL_ENV%/../manage.py "$* (windows)
____
* pubilcação no heroku
* pipenv install gunicorn (servidor de apps)
____
* Pytest-django - utilizado para nao permitir que erros cheguem no final da entrrega continua, ajudando o flake8, git-action, travis-CI.
* pipenv install -d 'pytest-django'
* criar variavel de ambiente indicado pelo site (pytest-django.read)
* criar pacote file 'pytest.ini, na raiz do projeto'
pytest.ini (dentro da pasta)
* 1 - [pytest]
* 2 - DJANGO_SETTINGS_MODULE = filhasdorei.settings
____
Na configuração do Pycharm

* Setings
* Integrate
* Defaut test runner (setar como pytest)
* Dentro da pasta base criar
* 1 pasta test
* 2 pacote test_home.py

Comando:

* def test_status_code(client: Client):
* resp = clietn.get ('/)
* assert resp.status_code == 200

Cobertura de testes: -pytest-cov -pipenv install --dev 'pytest-cov' codecov

Gerar relatórios

* pipenv run pytest --cov jbs

Criar no ci travis ou ga 

* configurando postgres
  
*configuração s3 

* configurado banco de dados com Sqlite 
  
* Configurado Backup do Postresql corrigido AKIARZD4SKDJZGOO7Q75

Utilizado

Twiter Bootstrap

Simulador