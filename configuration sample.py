BOT_TOKEN = ""
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
token_weather    = ''
token_yandex = ''
admin_id = ""
KINOPOISK_TOKEN = ""

import psycopg2 # Модуль для подключения к бд
# Подключаем БД
class connectBD():
    def func_connect_bd():
        connect = psycopg2.connect(host="127.0.0.1", port = 5432, database="postgres", user="", password="")
        return connect
