import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Configuração do logger para gravar em arquivo
logging.basicConfig(filename='app.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(message)s')

def enviar_email_erro(subject, body):
    # Configurações do e-mail
    sender_email = 'edson.zongo@netag.ao'
    receiver_email = ['dev.sys@netag.ao']
    smtp_server = 'mail.netag.ao'
    smtp_port = 587
    smtp_username = 'edson.zongo@netag.ao'
    smtp_password = 'Angola2023#'

    # Criar uma mensagem de e-mail
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_email)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Enviar e-mail usando smtplib
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        logging.info("E-mail de erro enviado com sucesso")
    except Exception as e:
        logging.error(f"Falha ao enviar e-mail de erro: {str(e)}")

def save_error(info_error):
    # Registrar o erro no log
    logging.error(f"Ocorreu um erro: {str(info_error)}")
    
    # Enviar e-mail de erro
    subject = 'Erro na Aplicação'
    body = f"Ocorreu um erro na aplicação:\n\n{str(info_error)}\n\n{datetime.datetime.now()}"
    enviar_email_erro(subject, body)