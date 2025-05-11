#!/bin/sh

# Activăm mediul virtual
echo " Activare mediu virtual (.venv)"
. .venv/bin/activate

# Setăm variabila de mediu pentru Flask
echo " Setare variabilă de mediu FLASK_APP"
export FLASK_APP=app/443D_scriitori.py

# Afișăm informații despre directorul curent
cale=$(pwd)
echo "CALE: $cale"
echo "CONȚINUT DIRECTOR:"
ls -1

# Pornim serverul Flask
echo "Pornire server Flask"
exec flask run -h 0.0.0.0 -p 5011 --reload

