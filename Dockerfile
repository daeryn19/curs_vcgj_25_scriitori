FROM python:3.10-alpine

# Setăm variabila de mediu pentru Flask
ENV FLASK_APP=app/443D_scriitori.py
ENV FLASK_RUN_PORT=5011
ENV FLASK_RUN_HOST=0.0.0.0

# Adăugăm un user non-root
RUN adduser -D scriitori
USER scriitori

# Directorul de lucru pentru utilizator
WORKDIR /home/scriitori

# Copiem aplicația și fișierele de configurare
COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt

# Creăm și activăm mediu virtual, apoi instalăm pachetele
RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r quickrequirements.txt

# Expunem portul pentru Flask
EXPOSE 5011

# Asigurăm permisiuni de execuție pe scriptul de pornire
RUN chmod +x dockerstart.sh

# Punctul de intrare în container
ENTRYPOINT ["./dockerstart.sh"]
