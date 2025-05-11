FROM python:3.10-alpine

ENV FLASK_APP scriitori
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
RUN adduser -D scriitori

USER scriitori

WORKDIR /home/scriitori

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY scriitori.py scriitori.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/scriitori/app

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh
