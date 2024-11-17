from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

token = '7828286437:AAG32lUYszJt6JUm2jbLNX91HNOS671Zo4I'
bot = Bot(token = token)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button_info = KeyboardButton(text = 'Информация')
kb.add(button_info)
button_start = KeyboardButton(text = 'Начало')
kb.add(button_start)

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет!', reply_markup = kb)
    await UserState.age.set()

@dp.message_handler(text = ['Информация'])
async def inform(message):
    await message.answer('Информация о боте!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)