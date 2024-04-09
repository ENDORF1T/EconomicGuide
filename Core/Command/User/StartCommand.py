import Data.Config as config
from aiogram.types import Message
from aiogram.filters import CommandStart

async def process_start_command(message: Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")