from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Davi Scholl', cpf='12345678901', email='davis@bandavide.com.br', phone='54 98400-5950')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'davis@bandavide.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['davis@bandavide.com.br', 'davis@bandavide.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Davi Scholl',
            '12345678901',
            'davis@bandavide.com.br',
            '54 98400-5950'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
