import unittest

from main import soma_tres

class TestSomaTres(unittest.TestCase):
    def test_soma_tres_inteiros_positivos(self):
        """Testa a soma de três números inteiros positivos."""
        self.assertEqual(soma_tres(1, 2, 3), 6)

    def test_soma_tres_decimais(self):
        """Testa a soma de três números decimais."""
        self.assertEqual(soma_tres(1.5, 2.5, 3.5), 7.5)

    def test_soma_tres_negativos(self):
        """Testa a soma de três números negativos."""
        self.assertEqual(soma_tres(-1, -2, -3), -6)

    def test_soma_tres_mistos(self):
        """Testa a soma de números positivos e negativos."""
        self.assertEqual(soma_tres(-1, 2, -3), -2)

    def test_soma_tres_zeros(self):
        """Testa a soma de três zeros."""
        self.assertEqual(soma_tres(0, 0, 0), 0)

if __name__ == "__main__":
    unittest.main()