import sys
import os
import unittest

from app.lib import biblioteca_scriitori

class TestMihailSadoveanu(unittest.TestCase):
    def test_descriere_mihail_sadoveanu(self):
        descriere = biblioteca_scriitori.descriere_mihail_sadoveanu()
        assert "scriitor român" in descriere
        assert "istorie" in descriere or "viața rurală" in descriere

    def test_opere_mihail_sadoveanu(self):
        opere = biblioteca_scriitori.opere_mihail_sadoveanu()
        assert "Baltagul" in opere
        assert "Frații Jderi" in opere
        assert "Neamul Șoimăreștilor" in opere

    if __name__ == '__main__':
        unittest.main()
