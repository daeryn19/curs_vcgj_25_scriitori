# This file should be placed where pytest can discover it,
# typically in a 'tests' directory at your project root.

# Correct import statement to import the functions from the specific module
from app.lib.biblioteca_scriitori import descriere_scurta_autor, carti_autor

def test_locatie():
    # Call the function descriere_scurta_autor()
    # Assert that the string returned by the function contains "Moscova"
    assert "Moscova" in descriere_scurta_autor()

def test_carte():
    # Call the function carti_autor()
    # Assert that the string returned by the function contains "Idiotul"
    assert "Idiotul" in carti_autor()

# Note: These tests check if the specific strings "Moscova" and "Idiotul"
# are present anywhere in the longer strings returned by the functions.
# If you needed more precise checks (e.g., check for exact matches or specific list items),
# you would adjust the functions in biblioteca_scriitori.py to return a list
# or a more structured object, and adjust the test assertions accordingly.
