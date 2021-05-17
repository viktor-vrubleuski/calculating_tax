FROM python:3.8

RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src


COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
RUN pip install pipenv && pipenv install --system


COPY . /opt/services/djangoapp/src
COPY ./static /opt/services/djangoapp/src/static


EXPOSE 8000

