import psycopg2
import redis
import json
# api que conseguem consumir as variaveis de ambiente
import os 
from bottle import Bottle, request

# Criando Classe Sender que herda de Bottle
class Sender(Bottle):
    # Método de inicialização
    def __init__(self):
        super().__init__()
        # Chamando método de rota da SuperClasse Bottle e chamando método de envio de email
        self.route('/', method='POST', callback=self.send)            
                
        # Acessando variaveis de ambiente da fila caso exista, senao é usado o valor padrao
        redis_host = os.getenv('REDIS_HOST', 'queue')
        
        # Acessando serviço de fila do Redis criado no container
        self.fila = redis.StrictRedis(host=redis_host, port=6379, db=0)
        
        # Acessando variaveis de ambiente do banco caso exista, senao é usado o valor padrao
        db_host = os.getenv('DB_HOST', 'db')
        db_user = os.getenv('DB_USER', 'postgres')
        db_name = os.getenv('DB_NAME', 'sender')
        
        # DATA SOURCE NAME
        dsn = f'dbname={db_name} user={db_user} host={db_host}'
        
        # DATA SOURCE NAME
        # DSN = 'dbname=email_sender user=postgres host=db'        
        # conectando ao banco
        self.connect = psycopg2.connect(dsn)
        
    # REGISTRAR MENSAGEM 
    def registrar_mesagem(self, assunto, mensagem):                
        # SQL DE INSERCAO NO BD
        SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'
        
        # criado cursor
        cursor = self.connect.cursor()
        # executando sql passando e mensagem
        cursor.execute(SQL, (assunto, mensagem))
        # commitando a execucao no BD
        self.connect.commit()
        # fechando execucao
        cursor.close()        
        
        # Formatado mensangem e adicionando na fila do Redis
        msg = {'assunto': assunto, 'mensagem': mensagem}
        # Formato Chave - Valor
        self.fila.rpush('sender', json.dumps(msg))
        
        print('Mensagem registrada!')

    # ROTA DE ENVIO POST
    def send(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')
        self.registrar_mesagem(assunto, mensagem)
        return 'Enviado! \n Assunto: {assunto}, Mensagem: {mensagem}'.format(
            assunto = assunto,
            mensagem = mensagem
        )
    
# VERIFICANDO SE É O ARQUIVO PRINCIPAL
if __name__ == '__main__':
    # Criando instancia de Sender
    sender = Sender()
    sender.run(host = '0.0.0.0', port = 8080, debug = True)