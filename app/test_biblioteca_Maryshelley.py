import app.lib.biblioteca_scriitori as bScriitori

def test_biografie_shelley():
    bio = bScriitori.biografie_shelley()
    assert "Mary Shelley" in bio
    assert "Frankenstein" in bio

def test_lucrare_celebra_shelley():
    lucrare = bScriitori.lucrare_celebra_shelley()
    assert "Frankenstein" in lucrare
    assert "1818" in lucrare

