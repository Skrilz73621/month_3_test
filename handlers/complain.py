from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, default_state, StatesGroup
from bot_config import database

complain_router = Router()

class Complain(StatesGroup):
    name = State()
    phone_number = State()
    complain = State()

@complain_router.message(Command('complain'), default_state)
async def start_complain(message: types.Message, state: FSMContext):
    await message.answer('Как ваше имя?')
    await state.set_state(Complain.name)
    
@complain_router.message(Complain.name)
async def get_user_name(message:types.Message, state:FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Введите ваш номер телефона')
    await state.set_state(Complain.phone_number)
    
@complain_router.message(Complain.phone_number)
async def get_user_phone_number(message:types.Message, state:FSMContext):
    phone_number = message.text
    if not phone_number.startswith('+996') and len(phone_number) != 13:
        await message.answer('Введите корректный номер телефона по типу: "+996123456789".')
        return
    await state.update_data(phone_number=phone_number)
    await message.answer('Введите, пожалуйста, вашу жалобу')
    await state.set_state(Complain.complain)
    
@complain_router.message(Complain.complain)
async def get_user_complain(message: types.Message, state:FSMContext):
    complain = message.text
    await message.answer('Спасибо за жалобу, мы ее обязательно учтем. (нет)')
    await state.update_data(complain = complain)
    data = await state.get_data()
    database.save_complain(data)