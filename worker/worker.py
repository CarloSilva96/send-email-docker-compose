import redis
import json
from time import sleep
from random import randint

# Fazendo teste para verificar se é o arquivo principal que está sendo executado
if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    
    # Laço infinito para envio de mensagens
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        # Simulação de envio do email
        print('Enviando mensagem: ', mensagem['assunto'])
        sleep(randint(5, 10))
        print('Mensagem: ', mensagem['assunto'], ', enviada!!!')