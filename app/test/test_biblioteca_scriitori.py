from app.lib import biblioteca_scriitori_opera
from app.lib import biblioteca_sctiitori_gen

def test_magnum_opus():
	assert biblioteca_scriitori_opera.magnum_opus()=="Shatter Me"

def test_genre():
	assert biblioteca_scriitori_gen.genre()=="Romance Young Adult Dystopian"

