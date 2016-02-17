#! python
# -*- encoding: utf-8 -*-
"""
Script that sends an email to my real state agency every month, asking them
to send me an invoice for my rent. They - or whoever designed their system -
are just too dumb or too lazy to generate all of the invoices in advance or
to at least send them to me regularly.
"""
from json import load
from mandrill import Mandrill

def main(receiver, housing_address, api_key):
    mandrill_client = Mandrill(api_key)
    message = {
        'from_email': 'message.from_email@example.com',
        'from_name': 'Example Name',
        'headers': {'Reply-To': 'message.reply@example.com'},
        'html': '<p>Example HTML content</p>',
        'important': False,
        'metadata': {'website': 'www.example.com'},
        'preserve_recipients': None,
        'recipient_metadata': [{
            'rcpt': 'recipient.email@example.com',
            'values': {'user_id': 123456}
        }],
        'return_path_domain': None,
        'signing_domain': None,
        'subaccount': 'customer-123',
        'subject': 'example subject',
        'tags': ['password-resets'],
        'text': 'Example text content',
        'to': [{
            'email': 'recipient.email@example.com',
            'name': 'Recipient Name',
            'type': 'to'
        }],
        'track_clicks': None,
        'track_opens': None,
        'tracking_domain': None,
        'url_strip_qs': None,
        'view_content_link': None
    }
