import psycopg2
from bottle import Bottle, route, run, request

#DATA SOURCE NAME
DSN = 'dbname=email_sender user=postgres host=db'

#SQL DE INSERCAO NO BD
SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

#REGISTRAR MENSAGEM 
def registrar_mesagem(assunto, mensagem):
    #conectando ao banco
    connect = psycopg2.connect(DSN)
    #criado cursor
    cursor = connect.cursor()
    #executando sql passando e mensagem
    cursor.execute(SQL, (assunto, mensagem))
    #commitando a execucao no BD
    connect.commit()
    #fechando execucao
    cursor.close()
    #fechando conexao
    connect.close()
    
    print('Mensagem registrada!')

#ROTA DE ENVIO POST
@route('/', method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    registrar_mesagem(assunto, mensagem)
    return 'Enviado! \n Assunto: {assunto}, Mensagem: {mensagem}'.format(
        assunto = assunto,
        mensagem = mensagem
    )
    
#VERIFICANDO SE É O ARQUIVO PRINCIPAL
if __name__ == '__main__':
    run(host = '0.0.0.0', port = 8080, debug = True)