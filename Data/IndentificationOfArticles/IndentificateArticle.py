import json
from thefuzz import fuzz

articles = dict()
minRatioAccept = 80

with open("Data/IndentificationOfArticles/IndentificationOfArticles.json", "r", encoding='utf-8') as json_data:
    articles = json.load(json_data)
    print("Article List was loaded")

def HasArticle(text: str) -> (bool, str):
    for key, value in articles.items():
        if fuzz.partial_ratio(text, key) >= minRatioAccept:
            return True, value
    return False, None
