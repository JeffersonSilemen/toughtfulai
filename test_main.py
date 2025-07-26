import unittest
from main import sort

class TestPackageSort(unittest.TestCase):
    
    def test_standard_package(self):
        """Teste para pacote padrão - não é volumoso nem pesado"""
        result = sort(50, 50, 50, 10)
        self.assertEqual(result, "STANDARD")
    
    def test_bulky_package_by_dimension(self):
        """Teste para pacote volumoso por dimensão (uma dimensão >= 150)"""
        result = sort(160, 50, 50, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_package_by_volume(self):
        """Teste para pacote volumoso por volume (volume >= 1.000.000)"""
        result = sort(100, 100, 100, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_heavy_package(self):
        """Teste para pacote pesado (massa >= 20)"""
        result = sort(50, 50, 50, 25)
        self.assertEqual(result, "SPECIAL")
    
    def test_rejected_package(self):
        """Teste para pacote rejeitado - volumoso E pesado"""
        result = sort(160, 50, 50, 25)
        self.assertEqual(result, "REJECTED")


if __name__ == "__main__":
    unittest.main()
