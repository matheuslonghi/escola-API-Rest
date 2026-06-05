from django.test import TestCase

from escola.models import Estudante, Curso


class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']
    
    def test_carregamento_da_fixtures(self):
        """"Teste que verifica o carregamento da fixtures"""

        estudante = Estudante.objects.get(cpf='35651021019')
        curso = Curso.objects.get(pk=4)
        self.assertEqual (estudante.celular, "65 96184-4510")
        self.assertEqual(curso.codigo, "CPOO1")