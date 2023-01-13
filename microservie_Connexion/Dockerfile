FROM python:3.8.5-alpine
COPY . /app
WORKDIR /app
RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["connexion.py"]