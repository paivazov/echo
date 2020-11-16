from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# засунул токен сразу, не вижу смысла на 1 переменную создавать модуль
TOKEN = '1413691817:AAEVWElmzbS5nSMqCG8AtMQ6HVLDqil_IWc'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Напиши мне, отправлю такое же сообщение")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я бот, который возвращает написанное Вами сообщение")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
