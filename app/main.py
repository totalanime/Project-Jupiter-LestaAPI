from fastapi import FastAPI
import requests

app = FastAPI()

# Укажите id для поиска
variable = "57886125"
# Выберите achievements (награды) или tanks (техника)
selects = "tanks"
# Поиск по игровому id (account_id)
search = "account_id"
# Ключ доступа API
key = "214c61dc71b81996bedc15084ef9673f"

# Просмотр достижений в базе данных Lesta через поиск по id игрока
response = requests.get(
url=f'https://api.tanki.su/wot/account/{selects}/?application_id={key}&{search}={variable}',
)
# Просматриваем значения атрибутов результатов поиска по базе Lesta
json_response = response.json()

@app.get ('/')
def home():
    return response.json()


