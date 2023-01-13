FROM python:3.8.5-alpine
COPY . /app
WORKDIR /app
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*
ENTRYPOINT ["python"]
CMD ["affichage.py"]