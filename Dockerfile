    FROM library/python:3.6.3-alpine
    RUN apk update && apk upgrade && apk add --no-cache make g++ bash git openssh postgresql-dev curl
    RUN mkdir -p /usr/src/app
    WORKDIR /usr/src/app
    COPY . /usr/src/app
    RUN ls
    RUN pip install -r requirements.txt
    COPY ./deploy/ /usr/src/deploy
    EXPOSE 80
    CMD sh /usr/src/deploy/run.sh