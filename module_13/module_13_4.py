from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


token = '7828286437:AAG32lUYszJt6JUm2jbLNX91HNOS671Zo4I'
bot = Bot(token = token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text = ['Calories'])
async def buy(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    #Для мужчин: (10 × вес в килограммах) + (6, 25 × рост в сантиметрах) − (5 × возраст в годах) + 5
    calories_man = 10*float(data['weight']) * (6.25 * float(data['growth'])) - (5 * float(data['age'])) + 5
    await message.answer(f'Ваша норма калорий: {calories_man}')
    await UserState.weight.set()
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)