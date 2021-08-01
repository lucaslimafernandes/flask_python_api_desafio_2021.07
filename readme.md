# Desafio Back-End

Lucas Lima Fernandes

## Instalação

1.  Criar um ambiente virtual (venv)
>python3 -m venv vEnv

2.  Ativar o venv
>source vEnv/bin/activate   #Linux

> source vEnv/Scripts\activate  #Windows

3.  Instalar os pacotes
>python -m pip install --upgrade pip

>pip install -r requirements.txt

4.  Rodar o Flask
>export FLASK_APP=main
>flask run

## API's [GET]

http://127.0.0.1:5000 como URL local

Consulta que retorna JSON de toda a tabela.

*   http://127.0.0.1:5000/consultaTodos/

Consulta conforme algum paramêtro específico.

*   http://127.0.0.1:5000/consulta/?brand=Kuhne - retorna JSON pela busca da marca.
*   http://127.0.0.1:5000/consulta/?categories=Mercearia - retorna JSON pela busca da categoria.
*   http://127.0.0.1:5000/consulta/?name=cafe - retorna JSON pela busca do nome.
*   Importante, a busca é via LIKE, ou seja, Kuh ja retornará os resultados de Kuhne, por exemplo.

Busca pelo id do produto

*   http://127.0.0.1:5000/id/70711087

Os retornos abaixo serão apenas dos campos selecionados pelo chamado

*   http://127.0.0.1:5000/id/70711087/id
*   http://127.0.0.1:5000/id/70711087/image
*   http://127.0.0.1:5000/id/70711087/name
*   http://127.0.0.1:5000/id/70711087/categories
*   http://127.0.0.1:5000/id/70711087/price
*   http://127.0.0.1:5000/id/70711087/brand

## API [PATCH]

PATCH para atualização dos valores, possível alterar um valor ou mais de um ao mesmo tempo.

*   http://127.0.0.1:5000/id/70711087

Headers

*   image
*   name
*   categories
*   price
*   brand

### Observações

O servidor MySQL é um serviço gratuito, as vezes perde a conexão.

Para criar estas API's foi utilizado Python, Flask e MySQL.




Abraço,

Lucas Lima Fernandes