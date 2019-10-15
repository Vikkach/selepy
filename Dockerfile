FROM ubuntu:18.04

WORKDIR /app

RUN apt-get -y update; \
    apt-get -y install gnupg2 curl; \
    curl -sL https://deb.nodesource.com/setup_10.x | bash -; \
    apt-get install -y nodejs openjdk-8-jre-headless python3-pip;
COPY ./requirements.txt ./requirements.txt
RUN pip3 install virtualenv; \
    pip3 install -r requirements.txt --no-cache-dir

RUN pyclean /app

CMD [""]