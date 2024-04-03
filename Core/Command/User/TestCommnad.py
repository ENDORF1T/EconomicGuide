from aiogram.types import Message
from Data.Config import bot
from Data.DataBase.DataBase.functions.article import Article

async def cmd_Test(message: Message):
    article = Article()
    text = article.select_article("KEK")
    await bot.send_message(text=text, chat_id=message.chat.id, message_thread_id=message.message_thread_id)