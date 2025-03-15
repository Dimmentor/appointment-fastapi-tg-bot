import time

from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.api.dao import UserDAO
from app.bot.keyboards.kbs import app_keyboard
from app.bot.utils.utils import greet_user, get_about_us_text, get_price_list

user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    Обрабатывает команду /start.
    """
    user = await UserDAO.find_one_or_none(telegram_id=message.from_user.id)

    if not user:
        await UserDAO.add(
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            username=message.from_user.username
        )

    await greet_user(message, is_new_user=not user)


@user_router.message(F.text == '🔙 Назад')
async def cmd_back_home(message: Message) -> None:
    """
    Обрабатывает нажатие кнопки "Назад".
    """
    await greet_user(message, is_new_user=False)

@user_router.message(F.text == "💵️ Цены")
async def price_list(message: Message):
    kb = app_keyboard(user_id=message.from_user.id, first_name=message.from_user.first_name)
    await message.answer(get_price_list(), reply_markup=kb)


@user_router.message(F.text == "ℹ️ О нас")
async def about_us(message: Message):
    kb = app_keyboard(user_id=message.from_user.id, first_name=message.from_user.first_name)
    await message.answer(get_about_us_text(), reply_markup=kb)

@user_router.message(F.text == "📩 Чат с сотрудником")
async def contact_us(message: Message):
    chat_url = "https://t.me/l0ngdl" #чат с админом
    await message.answer(f"Вы можете связаться с нами по следующей ссылке: {chat_url}")

@user_router.message(lambda message: message.text not in ["💵️ Цены", "ℹ️ О нас", "📩 Чат с сотрудником", "🔙 Назад"])
async def echo(message: Message):
    await message.answer("Выберите категорию меню.")
