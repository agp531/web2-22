DROP TABLE IF EXISTS cliente;

CREATE TABLE cliente(
    -- chave primaria --
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    cpf text,
    cep text,
    email text NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- CREATE
INSERT INTO cliente (nome, cpf, cep, email)
VALUES
    ('admin', '1002000', '85850-100', 'admin@test.org'),
    ("Maria Silver", "949.282.111-82", '85850-100', "mariam@test.org"),
    ("Jairo Carlile", "144.217.577-11", '85850-100', "carlile@test.org"),
    ("Marcos Oliva", "433.144.644-52", '85850-100', "marcos@test.org");