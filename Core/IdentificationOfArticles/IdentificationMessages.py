import time
import Data.Config as config
import os

from Data.Config import DebugLog
from aiogram import F
from aiogram.types import Message, FSInputFile
from Data.DataBase.DataBase.functions.article import Article
from Data.IndentificationOfArticles.IndentificateArticle import HasArticle
from Data.ExceptionTypes import Exception_PhotoDoesntExist

from Core.Command.User.StartCommand import process_start_command

async def CheckIfItCommand(message: Message) -> bool:
    if (message.text == "/start"):
        await process_start_command(message)
        return True
    return False


@config.dispatcher.message(F.text)
async def IndentificateMessage(message: Message):
    if (await CheckIfItCommand(message=message)):
        return

    articleValue: (bool, str) = HasArticle(message.text)
    if articleValue[0]:
        await SendMessage(message, Article().select_article(articleValue[1]))
    else:
        await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                      text="По вашему запросу ничего не найдено")

async def SendMessage(message: Message, article: Article):
        text = article[0]
        photo_link = article[1]
        try:
            if photo_link == '':
                await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                              text=text)
            else:
                photo = FSInputFile(photo_link)

                if not(os.path.isfile(photo_link)):
                    raise Exception_PhotoDoesntExist

                await config.bot.send_photo(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                            photo=photo)

                time.sleep(1)
                await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                              text=text)

        except Exception_PhotoDoesntExist:
            DebugLog("Photo does't exist")
            await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                          text="Произошла ошибка в отправлении")