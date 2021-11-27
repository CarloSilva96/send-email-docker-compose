FROM python:3.6
LABEL maintainer 'cjrcordeiro@gmail.com'

# Fazendo print das variáveis sem usar o buffer para evitar problemas
ENV PYTHONUNBUFFERED 1
RUN pip install redis==2.10.5

ENTRYPOINT ["/usr/local/bin/python"]