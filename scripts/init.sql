DROP DATABASE IF EXISTS email_sender;

CREATE DATABASE email_sender;

\c email_sender;

CREATE TABLE emails (
    id serial NOT NULL,
    data timestamp NOT NULL default CURRENT_TIMESTAMP,
    assunto varchar(100) NOT NULL,
    mensagem varchar(255) NOT NULL
);