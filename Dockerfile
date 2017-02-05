FROM ubuntu:14.04

MAINTAINER efenfauzi

RUN mkdir -p /srv/django_kbbi

ENV DOCKYARD_SRC=.
ENV DOCKYARD_SRVHOME=/srv
ENV DOCKYARD_SRVPROJ=/srv/django_kbbi

RUN apt-get update
RUN apt-get install -y python python-pip

WORKDIR $DOCKYARD_SRVHOME
# RUN mkdir media static logs
# VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]

COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

RUN pip install -r $DOCKYARD_SRVPROJ/requirements.txt

EXPOSE 6565

WORKDIR $DOCKYARD_SRVPROJ
COPY ./docky_entrypoint.sh /
ENTRYPOINT ["/docky_entrypoint.sh"]
