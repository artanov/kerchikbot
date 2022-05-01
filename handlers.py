from main import bot, dp
from aiogram.types import Message # aiogram
from aiogram import types   # aiogram
from configuration import admin_id, url, connectBD # Мой конфиг
import keyboards as kb # Кнпоки
from lxml import etree # Для парсинка валют
import requests 
from weather import classweather # Подключаем прогноз погоды
#import psycopg2 # Модуль для подключения к бд
from Query import Scripts # Скрипты в бд
from mykinopoisk import jekaFilm # апи кинопоиска

# FSM
#from typing import Optional
#import aiogram.utils.markdown as md
from aiogram import  Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
#from aiogram.utils import executor
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# States
class Form(StatesGroup):
    film_name = State()  # Наименование фильма
    task_name = State()  # Описание задачи

# Подключаем БД
connect = connectBD.func_connect_bd()
cursor = connect.cursor()

# Комманла старт
@dp.message_handler(commands=['start'])

async def start_MainKeyboard(message: Message):
            # Проверяем наличие пользователя в БД
    cursor = connect.cursor()
    
    people_id = message.chat.id
    cursor.execute (f"SELECT User_id from users where User_id = {people_id}")
    data = cursor.fetchone()    
    if data is None:
    # Если нет - добавляем!             
        user_id = message.chat.id
        user_name = message.from_user.first_name
        with connect.cursor() as cursor:
            cursor.execute("INSERT INTO users (User_id,User_name) VALUES(%s,%s);",(user_id,user_name))
            connect.commit()

    text = "<b>Главное меню: </b>"
    await bot.send_message(message.from_user.id,text=text,
                        reply_markup=kb.MainKeyboard)

##callback_query_handler перехват кнопок
@dp.callback_query_handler(lambda c: c.data == 'MainKeyboard')
async def MainKeyboard_func(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('<b>Главное меню:</b>', reply_markup=kb.MainKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'keyExchange')
async def keyExchange_func(callback_query: types.CallbackQuery):
    #await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text('<b>Курс валют:</b>', reply_markup=kb.keyExchange)

@dp.callback_query_handler(lambda c: c.data == 'keyUSD')
async def keyUSD_func(callback_query: types.CallbackQuery):
    xml_response = etree.fromstring(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.encode("1251"))
    curs = xml_response.find("Valute[@ID='R01235']/Value").text
    await callback_query.message.edit_text(text = f"1 доллар {curs} рублей", reply_markup=kb.keyUSD)

@dp.callback_query_handler(lambda c: c.data == 'keyEUR')
async def keyUSD_func(callback_query: types.CallbackQuery):
    xml_response = etree.fromstring(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.encode("1251"))
    curs = xml_response.find("Valute[@ID='R01239']/Value").text
    await callback_query.message.edit_text(text = f"1 eвро {curs} рублей", reply_markup=kb.keyEUR)
    
@dp.callback_query_handler(lambda c: c.data == 'keyWeather')
async def keyWeather_func(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('<b>Погода:</b>', reply_markup=kb.keyWeather)

@dp.callback_query_handler(lambda c: c.data == 'weather')
async def weather_func(callback_query: types.CallbackQuery):
    text = classweather.get_weather()
    await callback_query.message.edit_text(text=text, reply_markup=kb.Weather)

@dp.callback_query_handler(lambda c: c.data == 'keyFilms')
async def keyFilms_func(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='<b>Фильмы:</b>', reply_markup=kb.keyFilms)


@dp.callback_query_handler(lambda c: c.data == 'SearchFilms')
async def SearchFilms_func(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='<b>Поиск фильма:</b>', reply_markup=kb.SearchFilms)

@dp.callback_query_handler(lambda c: c.data == 'watchthis')
async def Swatchthis_func(callback_query: types.CallbackQuery):
            cursor = connect.cursor()
            people_id = callback_query.from_user.id
            cursor.execute (f"SELECT User_id from filmsfavorites where User_id = {people_id}")
            data = cursor.fetchone()    
            if data is None:#если нет выводим сообщение с кнопкой 
                await callback_query.message.edit_text(text='<b>Фильмы отсутствуют:</b>', reply_markup=kb.filmfavorites)
            else:
                text = Scripts.select_favoritefilms(people_id)
                await callback_query.message.edit_text(text=text, reply_markup=kb.filmfavorites)

@dp.callback_query_handler(lambda c: c.data == 'addfavorites')
async def addfavorites_func(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Для добавления воспользвуйтесь командой /addfavoritefilm')
    #await bot.send_message( "Для добавления воспользвуйтесь командой /addfavoritefilm",chat_id=message.from_user.id)

@dp.callback_query_handler(lambda c: c.data == 'keyTasks')
async def keyTasks_func(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='<b>Задачи:</b>', reply_markup=kb.keyTasks)

@dp.callback_query_handler(lambda c: c.data == 'keySQL')
async def keySQLfunc(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='<b>SQL:</b>', reply_markup=kb.keySQL)

@dp.callback_query_handler(lambda c: c.data == 'keyFunction')
async def keyFunction_func(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='<b>Функция это...</b>', reply_markup=kb.keyFunction)

@dp.callback_query_handler(lambda c: c.data == 'keyList')
async def keyList_func(callback_query: types.CallbackQuery):
        #проверка, что в таблице есть записи по этому пользователю
            cursor = connect.cursor()
            people_id = callback_query.from_user.id
            cursor.execute (f"SELECT User_id from todo_list where User_id = {people_id}")
            data = cursor.fetchone()    
            if data is None:#если нет выводим сообщение с кнопкой 
                await callback_query.message.edit_text(text='<b>Задачи отсутствуют 🗒</b>', reply_markup=kb.keyList)
                print(people_id)
            else:#если есть выводим все записи через Scripts.all_tasks()
                text = Scripts.all_tasks(people_id)
                await callback_query.message.edit_text(text=text, reply_markup=kb.keyList)
                print(people_id)

@dp.callback_query_handler(lambda c: c.data == 'FindName')                               
async def FindName_Func(callback_query: types.CallbackQuery):
    text = jekaFilm.go_film()
    await callback_query.message.edit_text(text=text, reply_markup=kb.FindName)

@dp.callback_query_handler(lambda c: c.data == 'keyAdd')
async def keyAddFunc(callback_query: types.CallbackQuery): 
    await callback_query.message.edit_text(text="Для добавления воспользвуйтесь командой /addtask")


@dp.callback_query_handler(lambda c: c.data == 'keyDelete')
async def keyDelete_Func(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Вы действительно хотите удалить все задачи?\nБудут удалены только ваши задачи'
    , reply_markup=kb.keyDelete)


@dp.callback_query_handler(lambda c: c.data == 'keydeletealltasks')
async def keydeletealltasksFunc(callback_query: types.CallbackQuery):
    people_id = callback_query.from_user.id
    Scripts.Delete_all_tasks(people_id) # вызов удаление записей
    await callback_query.message.edit_text(text='Все задачи удалены ✅', reply_markup=kb.keydeletealltasks)


@dp.message_handler(commands=['getfilm'])
async def command_weather(message: types.Message):
    people_id = message.from_user.id
    await bot.send_message(message.from_user.id,text =  jekaFilm.go_film(people_id))

@dp.message_handler(commands=['deletefavorites'])
async def command_weather(message: types.Message):
    people_id = message.from_user.id
    Scripts.delete_all_favorites(people_id)
    await bot.send_message(message.from_user.id,text ='Все фильмы удалены ✅')

##fsm
@dp.message_handler(commands=['addfavoritefilm'])
async def cmd_start(message: types.Message):
    # Set state Точка входа в разговор
    await Form.film_name.set()
    await message.answer("Введите название фильма:")

@dp.message_handler(state=Form.film_name)
async def process_name(message: types.Message, state: FSMContext):
    # Процесс названия фильма 
    async with state.proxy() as data:
        data['film_name'] = message.text

        # And send message
        await bot.send_message(message.chat.id, "Фильм добавлен ✅",reply_markup=kb.filmfavorites)
        user_id = message.chat.id
        name = data['film_name']
        Scripts.add_favoritefilm(name,user_id)#вызываем INSERT из функции
        #await bot.send_message(message.chat.id, md.text(md.text('Главное меню:', md.bold(data['name'])),sep='\n'), reply_markup=kb.MainKeyboard)

        # Finish conversation
        data.state = None

#mfsm
@dp.message_handler(commands=['addtask'])
async def cmd_start(message: types.Message):
    # Set state Точка входа в разговор
    await Form.task_name.set()
    await message.answer("Введите описание задачи:")

@dp.message_handler(state=Form.task_name)
async def process_name(message: types.Message, state: FSMContext):
    # Процесс описания задачи
    async with state.proxy() as data:
        data['task_name'] = message.text

        # And send message
        await bot.send_message(message.chat.id, "Задача добавлена ✅",reply_markup=kb.keydeletealltasks)
        user_id = message.chat.id
        name_film = data['task_name']
        Scripts.add_task(name_film,user_id)#вызываем INSERT из функции
        #await bot.send_message(message.chat.id, md.text(md.text('Главное меню:', md.bold(data['name'])),sep='\n'), reply_markup=kb.MainKeyboard)
        # Finish conversation
        data.state = None

