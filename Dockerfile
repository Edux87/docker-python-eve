FROM alpine:3.2
MAINTAINER Edux87 "edaniel15@gmail.com"

RUN apk add --update musl python3 py-pip eve wget && \
    rm /var/cache/apk/*

EXPOSE 5000 80 81
COPY ./app /app
CMD ["python", "/app/run.py"]
