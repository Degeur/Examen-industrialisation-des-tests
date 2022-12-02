from script import charger, extraire 

def test_charger():
    donnee=charger()
    assert isinstance(donnee, list)

def test_extraire():
    donnee=charger()
    donnee2=extraire(donnee)
    assert isinstance(donnee2, list)
    assert len(donnee2) == 10

