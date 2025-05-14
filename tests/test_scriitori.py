import pytest
from app.libs.biblioteca_scriitori_opera import magnum_opus
from app.libs.biblioteca_scriitori_gen import genre

def test_magnum_opus():
    assert magnum_opus() == "Les Misérables (1862) este una dintre cele mai cunoscute opere ale lui Victor Hugo."

def test_genre():
    assert genre() == "Victor Hugo este considerat unul dintre cei mai mari autori ai romantismului francez."
