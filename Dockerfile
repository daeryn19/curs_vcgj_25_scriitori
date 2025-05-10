FROM python:3.10-alpine

# Creează utilizator non-root
RUN adduser -D creanga

# Director de lucru
WORKDIR /home/creanga/app

# Instalăm pip și alte dependențe
RUN apk add --no-cache py3-pip gcc musl-dev libffi-dev

# Copiem toate fișierele proiectului
COPY . .

# Instalăm dependențele (direct, fără .venv)
RUN pip install --upgrade pip && pip install -r requirements.txt

# Setăm utilizatorul non-root
USER creanga

# Deschidem portul aplicației Flask
EXPOSE 5050

# Pornim aplicația cu gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5050", "ion_creanga:app"]
