# Desenvolvimento Web II
2022-2

## Exemplo chave extrangeira

Seja a relação 1 país possui N cidades, e 1 cidade possui apenas um país. Essa associação é também chamada 1-N

Para criar uma associação 1-N entre a tabela paises e cidades:

```sql
CREATE TABLE paises(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome varchar NOT NULL,
    continente varchar NOT NULL
);

CREATE TABLE cidades(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome varchar NOT NULL,
    pais_id integer NOT NULL,
    FOREIGN KEY (pais_id) REFERENCES paises (id),
);

-- testando a associação com alguns inserts --
INSERT INTO paises (nome, continente)
VALUES
    ('Brasil', 'America do Sul'),
    ('Espanha', 'Europa'),
    ('Canada', 'America do Norte');

INSERT INTO cidades (nome, pais_id)
VALUES
    ('Curitiba', 1),
    ('Montreal', 3),
    ('Madrid', 2);

```

## [Códigos vistos em aula](codigos/)

## [Instalação flask](https://github.com/fscheidt/dev/blob/master/flask/setup-projeto-flask.md)

## Instalação do python
No Lab de informática **não** é necessário.

No computador pessoal, precisa instalar o python fazendo download no site:
- https://www.python.org/downloads/ 

baixar última versão: 3.10

## Configuração Python + Visual studio

### Workspace

Criar uma pasta para armazenar os códigos e trabalhos.

Abrir o terminal do linux:

```
mkdir web2
cd web2

# abre o vscode na pasta web2:
code .

```

### Instalar plugin Python
Instalar pelo marketplace a extensão "Python"


### Habilitar opções do vscode:
- AutoSave


---

## Material complementar:
- passo-a-passo: https://code.visualstudio.com/docs/python/python-tutorial
