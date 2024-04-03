from aiogram import Dispatcher
from aiogram.filters import Command
import Data.Config as config

from Core.Command.User.TestCommnad import cmd_Test

async def InitCommnads(dispatcher: Dispatcher):
    dispatcher.message.register(cmd_Test, Command(commands=["s", "send"], prefix=config.GetCustomPrefix()))
