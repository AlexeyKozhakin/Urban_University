from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

class UserState(StatesGroup):
    adress = State()


token = '7828286437:AAG32lUYszJt6JUm2jbLNX91HNOS671Zo4I'
bot = Bot(token = token)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(text = ['Заказать'])
async def buy(message):
    await message.answer("Отправь нам свой адрес, пожалуйста")
    await UserState.adress.set()

@dp.message_handler(state = UserState.adress)
async def fsm_handler(message, state):
    await state.update_data(first = message.text)
    data = await state.get_data()
    await message.answer(f'Доставка будет отправлена на {data["first"]}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)