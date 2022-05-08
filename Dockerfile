FROM python:3.10-alpine
#to run python in unbuffered mode
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app

WORKDIR /app
COPY ./behrang /app

# create user as username
# -D create a user to running application only
# we do this for security reason to not have root access to everyone
RUN adduser -D user
USER user