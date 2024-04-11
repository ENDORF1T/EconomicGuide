import json
from thefuzz import fuzz

articles = dict()
minRationForArticle = 50

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
