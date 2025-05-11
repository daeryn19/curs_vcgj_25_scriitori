import lib.biblioteca_scriitori as b_Scriitori

def test_biografie_shelley():
    bio = b_Scriitori.biografie_shelley()
    assert "Mary Shelley" in bio
    assert "Frankenstein" in bio

def test_lucrare_celebra_shelley():
    lucrare = b_Scriitori.lucrare_celebra_shelley()
    assert "Frankenstein" in lucrare
    assert "1818" in lucrare

