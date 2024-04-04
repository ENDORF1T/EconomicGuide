import time

import Data.Config as config
from aiogram import F
from aiogram.types import Message, FSInputFile
from Data.DataBase.DataBase.functions.article import Article
from Data.IndentificationOfArticles.IndentificateArticle import HasArticle


@config.dispatcher.message(F.text)
async def IndentificateMessage(message: Message):
    articleValue: (bool, str) = HasArticle(message.text)
    if articleValue[0]:
        article = Article()
        text = article.select_article(articleValue[1])[0]
        photo_link = article.select_article(articleValue[1])[1]
        print(articleValue)
        print(photo_link)
        if photo_link == '':
            await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                          text=text)
        else:
            photo = FSInputFile(photo_link)
            await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                          text=text)
            time.sleep(1)
            await config.bot.send_photo(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                        photo=photo)
    else:
        text = articleValue[1][0]
        await config.bot.send_message(message_thread_id=message.message_thread_id, chat_id=message.chat.id,
                                      text=text)
