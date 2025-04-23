from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


Start = Router()

@Start.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer('Elmurod ZET botga hush kelibsiz! 😁')