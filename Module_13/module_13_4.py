from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import config


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = config.api_key
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст.')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост.')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес.')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        Calories = 10*int(data['weight']) + 6.25*int(data['growth']) - 5*int(data['age']) + 5
        await message.answer(f'Ваша норма {Calories} калорий.')
    except:
        await message.answer(f'Данные введены неправильно.')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
