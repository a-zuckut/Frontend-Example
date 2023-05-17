# pull image
FROM python:3.11-alpine

# env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUMBUFFERED 1

# work dir
WORKDIR /app

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# depdendencies
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./project/entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# copy
COPY . /app

ENTRYPOINT ["/app/project/entrypoint.sh"]