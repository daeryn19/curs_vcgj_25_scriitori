FROM python:3.10-alpine

ENV FLASK_APP scriitori

RUN adduser -D scriitori

USER scriitori

WORKDIR /home/scriitori/

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY scriitori.py scriitori.py


RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt


# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh
