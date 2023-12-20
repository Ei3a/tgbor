import psutil
from datetime import datetime
import telebot

TOKEN = '6489904660:AAHgsFgOXb_OGd7BsI0ubIYjBIBIZEit93g'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! Я бот для мониторинга системы. Чтобы получить информацию о системе, используйте команду /status")


# Обработчик команды /status
@bot.message_handler(commands=['status'])
def status(message):
    # Загрузка системы
    load_avg = ",".join([str(x) for x in psutil.getloadavg()])
    bot.send_message(message.chat.id, f"Загрузка системы: {load_avg}")

    # Состояние процессора
    cpu_percent = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq().current
    bot.send_message(message.chat.id, f"Использование CPU: {cpu_percent}%")
    bot.send_message(message.chat.id, f"Частота CPU: {cpu_freq} MHz")

    # Использование памяти
    mem_usage = psutil.virtual_memory().percent
    bot.send_message(message.chat.id, f"Использование памяти: {mem_usage}%")

    # Сетевые подключения
    connections = psutil.net_connections()
    bot.send_message(message.chat.id, f"Количество активных сетевых подключений: {len(connections)}")

    # Состояние файловой системы
    disk_usage = psutil.disk_usage('/').percent
    bot.send_message(message.chat.id, f"Использование дискового пространства: {disk_usage}%")

    # Время последнего обновления
    last_update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bot.send_message(message.chat.id, f"Последнее обновление: {last_update_time}")


# Запуск бота
bot.polling()