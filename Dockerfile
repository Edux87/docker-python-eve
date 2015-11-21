FROM alpine:3.2

RUN apk add --update musl python3 py-pip && \
    rm /var/cache/apk/*

RUN pip install eve

EXPOSE 5000
COPY ./app /app
CMD ["python", "/app/run.py"]
