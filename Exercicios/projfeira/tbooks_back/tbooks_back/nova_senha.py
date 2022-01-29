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
    link = auth.generate_password_reset_link(email, action_code_settings=None)

    message = Mail(from_email='tinobooks@gmail.com',
                to_emails=email,
                subject= 'Nova senha',
                plain_text_content= 'Esse é o link para criar sua nova senha: ',
                html_content='<p><b>Esse é o link para criar sua nova senha: <b><p>' + f'<p><a href={link}>Criar nova senha</a><p>'
                                )
    sg = SendGridAPIClient(Key)
    response = sg.send(message)
    print('Link para criar sua nova senha foi enviado para o seu email')