import redis
import json
import os
from time import sleep
from random import randint

# Fazendo teste para verificar se é o arquivo principal que está sendo executado
if __name__ == '__main__':
    # Acessando variaveis de ambiente da fila caso exista, senao é usado o valor padrao
    redis_host = os.getenv('REDIS_HOST', 'queue')        
    r = redis.Redis(host=redis_host, port=6379, db=0)
        
    print('Aguardando mensagem ...')
    
    # Laço infinito para envio de mensagens
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        # Simulação de envio do email
        print('Enviando mensagem: ', mensagem['assunto'])
        sleep(randint(5, 10))
        print('Mensagem: ', mensagem['assunto'], ', enviada!!!')