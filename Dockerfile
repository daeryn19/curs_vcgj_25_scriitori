FROM python:3.10-alpine

# Creăm utilizator non-root
RUN adduser -D mihai

# Setăm directorul de lucru
WORKDIR /home/mihai/app

# Instalăm dependențe sistem
RUN apk add --no-cache py3-pip gcc musl-dev libffi-dev

# Copiem doar requirements.txt pentru a putea rula pip install
COPY requirements.txt .

# Instalăm pachetele Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiem restul codului
COPY . .

# Setăm utilizatorul non-root
USER mihai

CMD ["gunicorn", "-b", "0.0.0.0:5050", "MihaiEminescu:app"]


