FROM python:3.11.3-alpine3.17

# Установка пакетов python и зависимостей необходимых для их сборки
RUN apk update && apk upgrade
RUN apk add --update alpine-sdk

# для psycopg3
RUN apk add


RUN apk add --no-cache --virtual build-deps \
    curl `# для установки poetry` \
    make gcc g++ libc-dev python3-dev libffi-dev `# для сборки пакетов` \
    postgresql-dev musl-dev gcc python3-dev libffi-dev `для psycopg3`

# Зависимости необходимые для работы
RUN apk add --no-cache \
    git `# для установки зависимостей из git` \
    jpeg-dev zlib-dev `# для pillow`

## develop
RUN apk add zsh

## Apple silicon
#RUN apk add -u zlib-dev jpeg-dev tzdata
#

RUN mkdir /app
WORKDIR /opt/app
COPY . /opt/app

## poetry
RUN if [ ! -d "/usr/local/bin/poetry" ]; then  \
    pip3 install poetry && \
    poetry config virtualenvs.create false; \
    fi

# SSH
RUN apk update && apk add openssh
RUN adduser -D sshuser
RUN echo 'sshuser:password' | chpasswd
RUN mkdir /home/sshuser/.ssh
RUN echo MaxAuthTries 666 >> /etc/ssh/sshd_config

## Удаление зависимостей для сборки
RUN apk del --no-cache build-deps

CMD ["/bin/sh", "./bin/entrypoint.develop.sh"]
