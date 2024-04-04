import Core.IdentificationOfArticles.IdentificationMessages
import Data.IndentificationOfArticles.IndentificateArticle

import Data.Config as config
import asyncio
import logging

from Core.Command.CommadsManager import InitCommnads


async def StartBot():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - (filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    await InitCommnads(dispatcher=config.dispatcher)

    try:
        await config.bot.delete_webhook(drop_pending_updates=True)
        await config.dispatcher.start_polling(config.bot, skip_updates=True,
                                              allowed_updates=config.dispatcher.resolve_used_update_types())

    finally:
        await config.bot.session.close()


asyncio.run(StartBot())
