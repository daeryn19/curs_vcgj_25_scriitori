FROM python:3.10-alpine
#Creează utilizator non-root
RUN adduser -D verne

#Directorul de lucru în container
WORKDIR /home/verne/app

#Instalăm pachete necesare pentru build și rulare
RUN apk add --no-cache py3-pip gcc musl-dev libffi-dev

#Copiem codul sursă în container
COPY . .

#Instalăm dependențele
RUN pip install --upgrade pip && pip install -r requirements.txt

#Trecem la utilizatorul non-root
USER verne

#Deschidem portul aplicației
EXPOSE 5050

#Pornim aplicația Flask prin gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5050", "JulesVerne:app"]
