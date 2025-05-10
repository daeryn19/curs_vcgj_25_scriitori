# Imagine de bază
FROM python:3.10-alpine

# Creează un utilizator non-root
RUN adduser -D arghezi

# Setează directorul de lucru
WORKDIR /home/arghezi/app

# Instalăm pip și alte unelte necesare
RUN apk add --no-cache py3-pip

# Copiem fișierele aplicației în container
COPY . .

# Instalăm dependențele Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Setează utilizatorul non-root pentru rulare
USER arghezi

# Expune portul 5050 (folosit de Flask/Gunicorn)
EXPOSE 5050

# Comanda de pornire a aplicației cu gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5050", "t_arghezi:app"]
