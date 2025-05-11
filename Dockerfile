FROM python:3.8-slim

WORKDIR /app

#Copiere cod sursă
COPY . .

#Instalare dependințe
RUN pip install --no-cache-dir -r quickrequirements.txt

#Expune portul 5000
EXPOSE 5000

#Rulează aplicația
CMD ["python", "popa_adrian_scriitori.py"]