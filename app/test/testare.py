import unittest
from app.lib.descriere import get_descriere
from app.lib.carti import get_carti

class TestAutorInfo(unittest.TestCase):
    def test_descriere(self):
        descriere = get_descriere()
        self.assertIsInstance(descriere, str)
        self.assertTrue("John Steinbeck" in descriere)

    def test_carti(self):
        culoare = get_carti()
        self.assertIsInstance(carti, str)
        self.assertTrue("carti" in carti or "autor" in carti)

if __name__ == '__main__':
    unittest.main()