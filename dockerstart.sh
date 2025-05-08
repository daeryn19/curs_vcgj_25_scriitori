#!/bin/sh

# Activăm mediul virtual
. .venv/bin/activate

# Pornim aplicația Flask
exec flask run
#!/bin/sh

echo "🔧 Activare mediu virtual (.venv)"
. .venv/bin/activate

echo "🔧 Setare variabilă de mediu FLASK_APP"
export FLASK_APP=app/443D_scriitori.py

echo "📂 Afișare cale curentă și conținut director"
cale=$(pwd)
echo "CALE: $cale"
echo "CONȚINUT DIRECTOR:"
ls -1

echo "🚀 Pornire server Flask"
exec flask run -h 0.0.0.0 -p 5011 --reload
