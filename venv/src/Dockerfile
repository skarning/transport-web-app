FROM ubuntu:18.04

MAINTAINER Sivert Marius Skarning "sivertskarning@hotmail.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN apt-get install -y python3 python3-pip

RUN apt-get -y  install unixodbc-dev
RUN apt-get -y install curl
RUN su
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN exit
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17

COPY . /src
COPY /transport /src/transport/
COPY /transport/configurations /src/confguration
WORKDIR /src

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "run-transport-app.py" ]