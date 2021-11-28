# send-email-docker
- Este projeto simula envio de email usando docker para criação dos serviços de front-end, back-end, banco de dados e usando redis para armazenamento em memória, ou seja, é criado uma lista de emails a serem enviados.
- É usado proxy reverso entre o serviço de front-end.
- Foi sobrecarregado o docker-compose.yml para configurar escalonamento do serviço worker.

### Execução do projeto
- Clone o projeto do git;
- Entre dentro da pasta do projeto e rode o comando abaixo para subir todos os serviços:
``` 
docker-compose up -d
```
### Parar execução do projeto
``` 
docker-compose down
```
### Caso tenha erro ao executar o script de init.sql use o comando abaixo:
```
docker-compose down -v
```

### Exibir logs do docker-compose
```
docker-compose logs -f -t
```
