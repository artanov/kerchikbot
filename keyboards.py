from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

##Главное меню
MainKeyboard = InlineKeyboardMarkup(row_width=2)
buttons = [
    InlineKeyboardButton(text="Курс валюты", callback_data="keyExchange"),
    InlineKeyboardButton(text="Погода", callback_data="keyWeather"),
    InlineKeyboardButton(text="Фильмы", callback_data="keyFilms"),
    InlineKeyboardButton(text="Список дел", callback_data="keyTasks"),
    InlineKeyboardButton(text="📚 SQL", callback_data="keySQL"),
]
MainKeyboard = InlineKeyboardMarkup(row_width=2)  # Объявляем клавиатуру, 2 ряда
MainKeyboard.add(*buttons)  # Добавляем кортеж из кнопок

##Кнопка Курс валюты
keyExchange = InlineKeyboardMarkup(row_width=2)
buttons = [
    InlineKeyboardButton(text="💵 USD", callback_data="keyUSD"),
    InlineKeyboardButton(text="💶 EUR", callback_data="keyEUR"),
    InlineKeyboardButton(text="⏮ Назад", callback_data="MainKeyboard"),
]
keyExchange = InlineKeyboardMarkup(row_width=2)  # Объявляем клавиатуру, 2 ряда
keyExchange.add(*buttons)  # Добавляем кортеж из кнопок

##Кнопка USD
keyUSD = InlineKeyboardMarkup(row_width=2)
buttons = [InlineKeyboardButton(text="⏮ Назад", callback_data="keyExchange")]
keyUSD.add(*buttons)  # Добавляем кортеж из кнопок

##Кнопка EUR
keyEUR = InlineKeyboardMarkup(row_width=2)  # Объявляем клавиатуру, 2 ряда
buttons = [InlineKeyboardButton(text="⏮ Назад", callback_data="keyExchange")]
keyEUR.add(*buttons)  # Добавляем кортеж из кнопок

##keyWeather
keyWeather = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton(text="Узнать погоду", callback_data="weather"),
    InlineKeyboardButton(text="⏮ Назад", callback_data="MainKeyboard"),
]
keyWeather.add(*buttons)

##Weather
Weather = InlineKeyboardMarkup()
buttons = [InlineKeyboardButton(text="⏮ Назад", callback_data="MainKeyboard")]
Weather.add(*buttons)

##keyFilms
keyFilms = InlineKeyboardMarkup(row_width=3)
buttons = [
    InlineKeyboardButton(text="Избранное", callback_data="watchthis"),
    # InlineKeyboardButton(text='Мой топ', callback_data='mytop'),
    InlineKeyboardButton(text="🔍 Поиск фильма", callback_data="SearchFilms"),
    InlineKeyboardButton(text="⏮ Назад", callback_data="MainKeyboard"),
]
keyFilms.add(*buttons)

##SearchFilms
#SearchFilms = InlineKeyboardMarkup()
#buttons = [
#    InlineKeyboardButton(text="По имени", callback_data="FindName"),
#    InlineKeyboardButton(text="⏮ Назад", callback_data="keyFilms"),
#]
#SearchFilms.add(*buttons)

##filmfavorites
filmfavorites = InlineKeyboardMarkup()
buttons = [
    InlineKeyboardButton(text="Добавить фильм", callback_data="addfavorites"),
    InlineKeyboardButton(text="⏮ Назад", callback_data="keyFilms"),
]
filmfavorites.add(*buttons)

##keyTasks
keyTasks = InlineKeyboardMarkup()
buttons = [
    InlineKeyboardButton(text="Список задач", callback_data="keyList"),
    InlineKeyboardButton(text="Добавить задачу", callback_data="keyAdd"),
    InlineKeyboardButton(text="Удалить задачу", callback_data="keyDelete"),
    InlineKeyboardButton(text="⏮ Назад", callback_data="MainKeyboard"),
]
keyTasks.add(*buttons)

##keySQL
keySQL = InlineKeyboardMarkup()
buttons = [
    InlineKeyboardButton(text="Функции", callback_data="keyFunction"),
    # InlineKeyboardButton(text='Табличные выражения', callback_data='keyCTE'),
    # InlineKeyboardButton(text='Вложенные запрос', callback_data='keySUBQURIES'),
    InlineKeyboardButton(text="⏮ Назад", callback_data="MainKeyboard"),
]
keySQL = InlineKeyboardMarkup()
keySQL.add(*buttons)

##keyFunction
keyFunction = InlineKeyboardMarkup()
buttons = [InlineKeyboardButton(text="⏮ Назад", callback_data="keySQL")]
keyFunction.add(*buttons)

##keyList
keyList = InlineKeyboardMarkup()
buttons = [InlineKeyboardButton(text="⏮ Назад", callback_data="keyTasks")]
keyList.add(*buttons)

##FindName
FindName = InlineKeyboardMarkup()
buttons = [InlineKeyboardButton(text="⏮ Назад", callback_data="keyFilms")]
FindName.add(*buttons)

keyDelete = InlineKeyboardMarkup()
buttons = [
    InlineKeyboardButton(text="Удалить", callback_data="keydeletealltasks"),
    InlineKeyboardButton(text="⏮ Назад", callback_data="keyTasks"),
]
keyDelete.add(*buttons)

keydeletealltasks = InlineKeyboardMarkup()
buttons = [InlineKeyboardButton(text="⏮ Назад", callback_data="keyTasks")]
keydeletealltasks.add(*buttons)
