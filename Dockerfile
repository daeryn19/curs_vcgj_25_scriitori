FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m pip install --upgrade pip

COPY . .

ENV FLASK_APP=app.443D_scriitori

CMD ["flask", "run", "--host=0.0.0.0"]

