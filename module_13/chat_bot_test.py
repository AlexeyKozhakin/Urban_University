from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = "7584288754:AAG1AJNdppHncR3wAOvjabCQZF2tsKKnvNE"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb.add(button1)
kb.add(button2)

str_warning = "Задавайте только целые числа"

@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer('Привет!!! Я бот, помогающий твоему здоровью.', reply_markup=kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
