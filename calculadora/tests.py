from django.test import TestCase

# Create your tests here.
from calculadora.repositories.funciones_repository import FuncionesRepository


class CalculadoraTestCase(TestCase):
	def testSuma(self):
		a = 5
		b = 10
		repo = FuncionesRepository()
		self.assertEqual(repo.suma(a, b), 15, 'la suma debería ser 15')
		self.assertEqual(repo.suma(10, -5), 5, 'La suma debería ser 5')
		self.assertEqual(repo.suma(5, -5), 1, 'La suma debería ser 1')
