from bottle import Bottle, route, run, request

#ROTA DE ENVIO POST
@route('/', method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    return 'Enviado! \n Assunto: {assunto}, Mensagem: {mensagem}'.format(
        assunto = assunto,
        mensagem = mensagem
    )
    
#VERIFICANDO SE É O ARQUIVO PRINCIPAL
if __name__ == '__main__':
    run(host = '0.0.0.0', port = 8080, debug = True)