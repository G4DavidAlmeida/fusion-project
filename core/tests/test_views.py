from django.test import TestCase, Client
from django.urls import reverse_lazy
from model_mommy import mommy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem',
        }

        features = mommy.make('Features', _quantity=4)

        self.cliente = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Felicity Jones',
            'assunto': 'meu assunto'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)