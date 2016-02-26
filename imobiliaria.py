#! /usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Script that sends an email to my real state agency every month, asking them
to send me an invoice for my rent. They - or whoever designed their system -
are just too dumb or too lazy to generate all of the invoices in advance or
to at least send them to me regularly.
Obs.: There are easier, ready-to-use systems for e-mail scheduling.
I wrote this just for fun.
"""

from json import load
from smtplib import SMTP
from email.mime.text import MIMEText
from datetime import datetime
from os import path

def main(smtp_data, email_data, address):
    """
    Main function
    """
    month = datetime.now().month # Loading the current month
    text = """<p>Olá,<br>
    Vocês poderiam me enviar o boleto do aluguel do mês atual, com vencimento
    no próximo dia 10?
    Meu imóvel é o da <b>{address}</b></p>
    <p>Obrigado!</p>
    """
    subject = "Boleto de aluguel do mês {month}"

    message = MIMEText(text.format(address=address), 'html')
    message['Subject'] = subject.format(month=month)
    message['From'] = email_data['sender']
    message['To'] = email_data['receiver']
    message['Reply-To'] = email_data['reply_to']

    server = smtplib.SMTP(host=smtp_data['server'], port=smtp_data['port'])
    server.ehlo()
    server.starttls()
    server.login(smtp_data['username'], smtp_data['password'])
    server.send_message(message)
    server.close()

if __name__ == "__main__":
    script_dir = path.dirname(__file__)
    config = load(open(path.join(script_dir, 'config.json')))

    smtp_data = {
        'server': config['smtp']['server'].split(':')[0],
        'port': config['smtp']['server'].split(':')[1],
        'username': config['smtp']['username'],
        'password': config['smtp']['password']
    }

    email_data = {
        'sender': config['email']['sender'],
        'reply_to': config['email']['reply_to'],
        'receiver': config['data']['imobiliaria']['receiver']
    }

    address = config['data']['imobiliaria']['address']

    main(smtp_data, email_data, address)
