import unittest
from app.lib.descriere import get_descriere
from app.lib.carti import get_carti
from app.lib.curent_literar import get_curent_literar

class TestAutorInfo(unittest.TestCase):
    def test_descriere(self):
        descriere = get_descriere()
        self.assertIsInstance(descriere, str)
        self.assertTrue("John Steinbeck" in descriere)

    def test_carti(self):
        carti = get_carti()
        self.assertIsInstance(carti, str)
        self.assertTrue("carti" in carti or "John Steinbeck" in carti)

    def test_curent_literar(self):
        curent_literar = get_curent_literar()
        self.assertIsInstance(curent_literar, str)
        self.assertTrue("realismul social" in curent_literar or "John Steinbeck" in curent_literar)

if __name__ == '__main__':
    unittest.main()