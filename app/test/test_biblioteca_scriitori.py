from app.libs import biblioteca_scriitori_opera
from app.libs import biblioteca_scriitori_gen

def test_magnum_opus():
	assert biblioteca_scriitori_opera.magnum_opus()=="Shatter Me"

def test_genre():
	assert biblioteca_scriitori_gen.genre()=="Romance Young Adult Dystopian"

