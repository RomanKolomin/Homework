from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *
import config


products = get_all_products()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = config.api_key
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True)
kb_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')]
        ]
)
buy_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию.', reply_markup=kb_inline)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'img/image{i}.jpg', "rb") as img:
            await message.answer_photo(img, f'Название: {products[i-1][1]} | Описание: описание {products[i-1][2]} | Цена: {products[i-1][3]}')
    await message.answer("Выберите продукт для покупки:", reply_markup=buy_inline)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def send_formula(call):
    await call.message.answer('10 x вес(кг) + 6.25 х рост(см) - 5 х возраст(г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст.')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(text='Информация')
async def start(message):
    await message.answer('Я бот помогающий твоему здоровью.')


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
