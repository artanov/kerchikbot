BOT_TOKEN = "5196220868:AAEZ_m9Bk5MlLAOFoCq4F445Sl3_UIabER8"
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
token_weather    = '3a03ca0ebf39d4b08386f513f98f8bfc'
token_yandex = '852981dc-b0ed-4e59-9dbc-e35bcfbed063'
admin_id = "244420389"

import psycopg2 # Модуль для подключения к бд
# Подключаем БД
class connectBD():
    def func_connect_bd():
        connect = psycopg2.connect(host="127.0.0.1", port = 5432, database="postgres", user="dbuser", password="teremok")
        return connect
