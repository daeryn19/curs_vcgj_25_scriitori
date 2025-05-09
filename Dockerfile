FROM python:3.10-alpine

# Creează utilizator non-root
RUN adduser -D stanescu

# Director de lucru
WORKDIR /home/stanescu/app

# Instalăm pip și dependențe sistem
RUN apk add --no-cache py3-pip

# Copiem toate fișierele proiectului
COPY . .

# Instalăm dependințele direct (fără .venv)
RUN pip install --upgrade pip && pip install -r requirements.txt

# Setăm utilizatorul non-root
USER stanescu

# Deschidem portul aplicației Flask
EXPOSE 5050

# Pornim aplicația cu gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5050", "n_stanescu:app"]
