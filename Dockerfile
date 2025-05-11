FROM python:3.8-alpine

ENV FLASK_APP=app.445D_scriitori

RUN adduser -D -h /home/scriitori scriitori

RUN mkdir /home/scriitori/curs_SCC_25_scriitori/ && chown scriitori:scriitori /home/scriitori/curs_SCC_25_scriitori/

WORKDIR /home/scriitori/curs_SCC_25_scriitori/

COPY app app/
COPY dockerstart.sh ./
COPY quickrequirements.txt ./

RUN chmod +x dockerstart.sh

USER scriitori

RUN python3 -m venv venv
RUN venv/bin/pip install -r quickrequirements.txt

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
