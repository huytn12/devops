FROM python:3

WORKDIR /usr/src/app

#ADD ./ .

RUN pip install lxml

CMD [ "python", "./src/script.py", "pom.xml" ]
