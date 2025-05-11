import app.libs.feature as feature

def test_opera_reprezentativa():
    assert feature.gaseste_opera_reprezentativa() == "Stăpânul Inelelor"

def test_curent_literar():
    assert feature.gaseste_curent_literar() == "Fantasy"