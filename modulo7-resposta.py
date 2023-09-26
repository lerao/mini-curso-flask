import unittest

def calcular_comprimento_string(s):
  return len(s)

class TestCalculoComprimentoString(unittest.TestCase):

  def test_comprimento_string_vazia(self):
    self.assertEqual(calcular_comprimento_string(''), 0)

  def test_comprimento_string_nao_vazia(self):
    self.assertEqual(calcular_comprimento_string('Hello, World!'), 13)

if __name__ == '__main__':
  unittest.main()