FROM python:3.10-alpine

ENV FLASK_APP=scriitori

# Creare utilizator non-root
RUN adduser -D scriitori

# Setare utilizator
USER scriitori

# Setare director de lucru
WORKDIR /home/scriitori

# Copiere fișiere
COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt

# Creare și activare venv
RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

# Configurare port
EXPOSE 5011

# Start server Flask
ENTRYPOINT ["./dockerstart.sh"]

