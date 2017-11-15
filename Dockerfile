FROM python:3.4

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		mysql-client libmysqlclient-dev \
		postgresql-client libpq-dev \
		sqlite3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y git

RUN pip3 install behave

RUN pip3 install selenium

ENV DJANGO_VERSION 1.10.4

RUN pip install mysqlclient psycopg2 django=="$DJANGO_VERSION"

ARG user=django
ARG group=django
ARG uid=1000
ARG gid=1000
ARG http_port=8000

ENV DJANGO_HOME /usr/src/app

RUN groupadd -g ${gid} ${group} \
    && useradd -d "$DJANGO_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

EXPOSE ${http_port}

USER ${user}

#RUN mkdir $DJANGO_HOME

WORKDIR $DJANGO_HOME


