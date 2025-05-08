FROM python:3.10-alpine

# Setăm variabila de mediu pentru Flask
ENV FLASK_APP=app/scriitori.py
ENV FLASK_RUN_PORT=5011
ENV FLASK_RUN_HOST=0.0.0.0

# Schimbăm la root pentru a putea modifica permisiunile
USER root

# Adăugăm un user non-root
RUN adduser -D scriitori

# Setăm directorul de lucru pentru utilizator
WORKDIR /home/scriitori

# Copiem aplicația și fișierele de configurare în container
COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY requirements.txt requirements.txt

# Asigurăm permisiuni de execuție pentru fișierele necesare
RUN chmod +x dockerstart.sh

# Schimbăm înapoi la utilizatorul non-root
USER scriitori

# Creăm și activăm mediul virtual, apoi instalăm pachetele necesare
RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt

# Expunem portul pe care va rula aplicația Flask
EXPOSE 5011

# Punctul de intrare în container - comanda care va fi rulată la pornirea containerului
ENTRYPOINT ["./dockerstart.sh"]

