from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionConfirmGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Davi Scholl',
            cpf='12345678901',
            email='davis@bandavide.com.br',
            phone='54 984005950'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        """ GET /inscricao/1/ must return status code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Must use subscriptions/subscription_confirm.html """
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_confirm.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionConfirmNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)
