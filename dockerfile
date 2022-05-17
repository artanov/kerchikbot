FROM python:3.8
LABEL  version = "1.0"
#ENV admin="Artanov"
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY . /usr/src/app/
# install dependencies
RUN pip install -U aiogram 
RUN pip install lxml requests requests asyncio psycopg2
RUN pip3 install kinopoisk-api-unofficial-client

# run app
CMD ["python", "main.py"]

#FROM ubuntu:18.04
#COPY . /app
#RUN make /app
#CMD python /app/app.py