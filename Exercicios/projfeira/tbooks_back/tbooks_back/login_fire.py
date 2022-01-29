from os import link
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from validate_email import validate_email
import json
from urllib.request import urlopen


Key = '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'
#service account credentials
cred = credentials.Certificate('t-book-s-a639d-firebase-adminsdk-errtg-bcf0c87dfc.json')
 
#initializing the app
firebase_admin.initialize_app(cred)

 
email = input('Seu email: ')
is_valid = validate_email(email,verify=True)
try:
  while (is_valid==False):
      email = input('Seu email: ')
      is_valid = validate_email(email,verify=True)

  else:
    user = auth.get_user_by_email(email=email, app=None)
    ic = user.uid
    message = Mail(from_email='tinobooks@gmail.com',
                to_emails=email,
                subject= 'Código/id da conta',
                plain_text_content= f'''Aqui está o seu id:
                                      {ic}''',
                html_content=f'''<p><b>Aqui está o seu id:<b><p>
                               <p><b>{ic}<b><p>'''
                                )
    sg = SendGridAPIClient(Key)
    response = sg.send(message)
    code = input('Código/id que enviamos por email: ')
    while code != ic:
      print('Id incorreto!')
      code = input('Código/id que enviamos por email: ')
    else:
      EnderecoAPI="http://ip-api.com/json"
      JsonResultanteAPI = urlopen(EnderecoAPI).read()
      JsonParseado = json.loads(JsonResultanteAPI)
 
      ipv = JsonParseado["query"]
      cidade = JsonParseado["city"]
      estado = JsonParseado["region"]
      pais = JsonParseado["country"]

      message = Mail(from_email='tinobooks@gmail.com',
                to_emails=email,
                subject= 'Login detectado',
                plain_text_content= f'''Novo login detectado.
                                       Informações do novo login:
                                       - IP da máquina: {ipv}
                                       - Cidade: {cidade}
                                       - Estado: {estado}
                                       - País: {pais}
                                       Foi você? 
                                      ''',
                html_content=f'''<p>Novo login detectado.<p>
                                       <p>Informações do novo login:<p>
                                      <p><b> - IP da máquina: {ipv} <p><b>
                                      <p><b> - Cidade: {cidade} <p><b>
                                       <p><b>- Estado: {estado}<p><b>
                                      <p><b> - País: {pais}<p><b>
                                      <p><b> Foi você?<p><b> 
                                      '''
                                )
      sg = SendGridAPIClient(Key)
      response = sg.send(message)
      print('Usuário logado com sucesso!')
except:
    print('Ocorreu um erro desconhecido') 