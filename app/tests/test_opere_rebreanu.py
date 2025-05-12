from app.libs.opere_rebreanu import gaseste_opera_reprezentativa, gaseste_curent_literar

def test_opera_reprezentativa():
    assert gaseste_opera_reprezentativa() == "Ion"

def test_curent_literar():
    assert gaseste_curent_literar() == "Realism"
