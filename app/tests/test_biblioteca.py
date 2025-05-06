import  lib.biblioteca_scriitori  as  biblioteca_scriitori

def test_opera_reprezentativa_Caragiale():
    assert biblioteca_scriitori.opera_reprezentativa_Caragiale() == "O scrisoare pierduta"

def test_curent_literar_Caragiale():
    assert biblioteca_scriitori.curent_literar_Caragiale() == "Realism"
