# API CRUD COM DJANGO REST FRAMEWORK PARA CONTROLE DE PRODUTOS
[Framework Django REST](http://www.django-rest-framework.org/) é um kit de ferramentas poderoso e flexível para construir APIs da Web.

## Requisitos
- Python 3.6
- Django 3.1
- Estrutura Django REST

## Instalação
Depois de clonar o repositório, você deseja criar um ambiente virtual para ter uma instalação limpa do python.
Você pode fazer isso executando o comando
```
python -m venv venv
./venv/Scripts/Activate.ps1
pip install django
pip install djangorestframework
python manage.py migrar
python manage.py runserver
```

Depois disso, é necessário ativar o ambiente virtual, você pode obter mais informações sobre isso [aqui](https://docs.python.org/3/tutorial/venv.html)

## Estrutura
Em uma API RESTful, os endpoints (URLs) definem a estrutura da API e como os usuários finais acessam os dados de nosso aplicativo usando os métodos HTTP - GET, POST, PUT, DELETE. Os endpoints devem ser logicamente organizados em torno de _collections_ e _elements_, ambos recursos.

No nosso caso, temos 2 recursos, `produtos`, `fornecedores`, então usaremos as seguintes URLS - `/products/` e `/providers` para coleções e elementos, respectivamente:

Terminal |Método HTTP | Método CRUD | Resultado
-- | -- |-- |--
`products` | GET | LEIA | Obtenha todos os produtos
`products/:id` | GET | LEIA | Obtenha um único produto
`products`| POST | CRIAR | Criar um novo produto
`products/:id` | PUT | ATUALIZAÇÃO | Atualizar um produto
`products/:id` | DELETE | APAGAR | Excluir um produto
`providers` | GET | LEIA | Obter todos os fornecedores
`providers/:id` | GET | LEIA | Obtenha um único fornecedor
`providers`| POST | CRIAR | Criar um novo fornecedor
`providers/:id` | PUT | ATUALIZAÇÃO | Atualizar um fornecedor
`providers/:id` | DELETE | APAGAR | Excluir um fornecedor