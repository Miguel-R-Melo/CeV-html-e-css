import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

Key = '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'

email = input('Qual é o seu email: ')
name = str(input('Nome do usuário: '))

message = Mail(from_email='tinobooks@gmail.com',
            to_emails=email,
            subject= 'Reserva de livro',
            plain_text_content= name + ', você reservou o livro teste',
            html_content=name + '<b>, você reservou o livro <b>teste<b>')

message2 = Mail(from_email='tinobooks@gmail.com',
            to_emails='tinobooks@gmail.com',
            subject= 'Reserva de livro',
            plain_text_content= name + ', reservou o livro teste')

sg = SendGridAPIClient(Key)
response = sg.send(message)
response = sg.send(message2)
print('Livro reservado!')

# colocar os inputs do html