from aiogram.types import Message
from Data.Config import bot

async def cmd_Test(message: Message):
    await bot.send_message(text="Иди нахуй дебик, с такими высказываниями", chat_id=message.chat.id, message_thread_id=message.message_thread_id)