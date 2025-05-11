import lib.biblioteca_scriitori as b_scriitori

def test_viata_eminescu():
	v = b_scriitori.viata_eminescu()
	if v == "frumoasa":
		assert True
	else:
		assert False


def test_opera_eminescu():
	o = b_scriitori.opera_eminescu()
	if o == "Luceafarul":
		assert True
	else:
		assert False	
			
	
