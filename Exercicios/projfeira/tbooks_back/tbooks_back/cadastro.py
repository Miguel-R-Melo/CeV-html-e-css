from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from validate_email import validate_email

Key = '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'
#service account credentials
cred = credentials.Certificate('t-book-s-a639d-firebase-adminsdk-errtg-bcf0c87dfc.json')
 
#initializing the app
firebase_admin.initialize_app(cred)

email = input('Seu email: ')
is_valid = validate_email(email,verify=True)
while (is_valid==False):
    email = input('Seu email: ')
    is_valid = validate_email(email,verify=True)
else:
    password = input("Senha: ")
    while password == '':
        print('Senha em branco')
        password = input("Senha: ")
    else:
        try:
            user = auth.create_user(email = email, password = password)
            print('Usuário criado com sucesso!')

            link = auth.generate_email_verification_link(email, action_code_settings=None)
            
            print('Bem Vindo ao App, confirme o seu email através do link que enviamos')
            
            message = Mail(from_email='tinobooks@gmail.com',
                to_emails=email,
                subject= 'Cadastro',
                plain_text_content= '''Você se cadastrou no T-Books!
                                    Esse é o link para confirmar seu email:''' + link,
                html_content='''<p><b>Você se cadastrou no T-Books!<b><p>
                                <p><b>Esse é o link para confirmar seu email: <b><p>''' + f'<p><a href={link}>Verificação</a><p>'
                                )
            sg = SendGridAPIClient(Key)
            response = sg.send(message)
        except:
            print('Usuário já cadastrado, por favor tente outro email!')