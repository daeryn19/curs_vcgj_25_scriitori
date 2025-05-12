#!/bin/sh
echo "Activare venv:"
#source venv/bin/activate
. venv/bin/activate
echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=app.445D_scriitori
echo "Start server:"
exec flask run -h 0.0.0.0 -p 5011 --reload
