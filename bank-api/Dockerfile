FROM python:3.8.13-alpine3.16

COPY requirements.txt /home/app/requirements.txt

WORKDIR /home/app/


RUN pip install alembic && \\
    pip3 install -r requirements.txt

COPY . /home/app/

ENV TZ America/Sao_Paulo

EXPOSE 5000

COPY . /home/app

ENTRYPOINT ["sh", "./entrypoint.sh"]