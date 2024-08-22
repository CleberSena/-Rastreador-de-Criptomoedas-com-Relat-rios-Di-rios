import requests
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Função para obter o preço atual do Bitcoin usando a API CoinGecko
def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl'
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['brl']

# Função para enviar e-mail
def send_email(subject, body, to_email):
    from_email = 'Seu Email Principal'
    from_password = 'Sua senha'

    # Configurando a mensagem do e-mail
    msg = MIMEMultipart()
    msg['Seu Email Principal'] = from_email
    msg['Email Destinatário'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Configurando o servidor SMTP e enviar o e-mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Função para monitorar o preço do Bitcoin
def monitor_price(target_price, user_email):
    current_price = get_bitcoin_price()
    print(f'Preço atual do Bitcoin: R${current_price:.2f}')
    os.system('cls')

    if current_price < target_price:
        subject = 'Alerta de Preço do Bitcoin'
        body = f'O preço do Bitcoin caiu para R${current_price:.2f}.'
        send_email(subject, body, user_email)
        print('E-mail enviado!')

# Configurando o monitoramento
def start_monitoring():
    target_price = float(input('Informe o valor mínimo para o Bitcoin (em BRL): '))
    user_email = input('Informe seu e-mail para receber notificações: ')

    schedule.every(10).minutes.do(monitor_price, target_price, user_email)

    print('Iniciando monitoramento...')

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    start_monitoring()
