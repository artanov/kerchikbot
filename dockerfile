FROM python:3.8
LABEL  version = "1.0"
ENV admin="Artanov"
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY . /usr/src/app/
# install dependencies
RUN pip install -U aiogram 
RUN pip install lxml
RUN pip3 install kinopoisk-api-unofficial-client
RUN pip install requests
RUN pip install pyowm
RUN pip install asyncio
RUN pip install psycopg2

# run app
CMD ["python", "main.py"]

