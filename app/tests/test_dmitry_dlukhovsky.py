import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app.libs import biblioteca_scriitori

def test_descriere_dmitry_glukhovsky():
    descriere = biblioteca_scriitori.descriere_dmitry_glukhovsky()
    assert "Dmitry Glukhovsky" in descriere

def test_opere_dmitry_glukhovsky():
    opere = biblioteca_scriitori.opere_dmitry_glukhovsky()
    assert "Metro 2033" in opere  # sau altă lucrare cunoscută
