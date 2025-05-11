import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app.libs import biblioteca_scriitori

def test_descriere_victor_hugo():
    descriere = biblioteca_scriitori.descriere_victor_hugo()
    assert "Victor Hugo" in descriere

def test_opere_victor_hugo():
    opere = biblioteca_scriitori.opere_victor_hugo()
    assert "Les Misérables" in opere
