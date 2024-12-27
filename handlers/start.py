from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    user = message.from_user.first_name
    await message.answer(f'Привееет, {user}. Как дела?')
