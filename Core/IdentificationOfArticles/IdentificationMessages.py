import Data.Config as config
from aiogram import F
from aiogram.types import Message
from Data.DataBase.DataBase.functions.article import Article
from Data.IndentificationOfArticles.IndentificateArticle import HasArticle

@config.dispatcher.message(F.text)
async def IndentificateMessage(message: Message):
    articleValue: (bool, str) = HasArticle(message.text)
    if (articleValue[0] == True):
        article = Article()
        text = article.select_article(articleValue[1])
        await config.bot.send_message(message_thread_id = message.message_thread_id, chat_id= message.chat.id, text=text)


