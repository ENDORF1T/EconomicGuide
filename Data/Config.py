import json
from aiogram import Bot, Dispatcher

DebugMode: bool = True

def DebugLog(text: str):
    if DebugMode:
        print(text)

def GetTokenBot() -> str:
    with open("Data/config.json", "r") as json_data:
        data = json.load(json_data)
        return data["TOKEN_BOT"]

def GetCustomPrefix() -> []:
    with open("Data/config.json", "r") as json_data:
        data = json.load(json_data)
        if data["CUSTOM_PREFIX"] is None:
            return data["PREFIX"]
        else:
            return data["CUSTOM_PREFIX"]

bot = Bot(GetTokenBot(), parse_mode="HTML")
dispatcher = Dispatcher()
