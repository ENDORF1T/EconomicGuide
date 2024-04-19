import json
from thefuzz import fuzz

articles = dict()
minRationForArticle = 50

groupArticles = dict()

groupArticles['Виды теории денег'] = [
    "Функциональная теория денег",
    "Информационная теория денег",
    "Марксистская теория денег",
    "Теория о металлических денег",
    "Номиналистическая теория денег",
    "Количественная теория денег",
    "Кейнсианская теория денег",
    "Государственная теория денег"
]

groupArticles['Деятели'] = [
    "Джон Мейнард Кейнс",
    "Пол Самуэльсон",
    "Джеймс Тобин",
    "Милтон Фридман",
    "Кеннет Эрроу",
    "Джордж Сельгин",
    "Джозеф Шумпетер",
    "Джордж Акерлофф",
    "Джозеф Стиглиц",
    "Дэвид Хьюм",
    "Дэвид Рикардо",
    "Фридрих Энгельс",
    "Фридрих фон Хайек",
    "Ирвинг Фишер",
    "Джон Локк",
    "Джон Стюарт Милль",
    "Карл Маркс",
    "Карл Менгер",
    "Людвиг фон Мизес"
]

with open("Data/IndentificationOfArticles/IndentificationOfArticles.json", "r", encoding='utf-8') as json_data:
    articles = json.load(json_data)
    print("Article List was loaded")

def HasArticle(text: str) -> (bool, str):
    maxRatio = 0
    maxRatioArticle: str = "None"
    for key, value in articles.items():
        currentRatio = fuzz.partial_ratio(text, key)
        if currentRatio >= maxRatio and currentRatio > minRationForArticle:
            maxRatio = currentRatio
            maxRatioArticle = value
    if (maxRatio == 0): return (False, maxRatioArticle)
    return  (True, maxRatioArticle)
