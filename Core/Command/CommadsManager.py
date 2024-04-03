from aiogram import Dispatcher
from Core.Command.User.UserCommand import InitCommnads as InitUserCommnads

async def InitCommnads(dispatcher: Dispatcher):
    await InitUserCommnads(dispatcher=dispatcher)