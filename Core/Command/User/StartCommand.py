import Data.Config as config
from aiogram.types import Message
from Data.IndentificationOfArticles.IndentificateArticle import groupArticles

async def process_start_command(message: Message):
    await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id, text="Чтобы начать работу с ботом, просто задайте интересующий вас вопрос или тему, и бот выдаст вам список подходящих материалов. Вы также можете воспользоваться функцией поиска по ключевым словам или датам.")

    text: str
    text = "Список тем, которые можно найти:\n"

    for key in groupArticles:
        text += key + ":\n"
        for value in groupArticles[key]:
            text += "● " + value + "\n"

    await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                  text=text)
